from flask import Flask, render_template, request
import os
import ecdsa
import hashlib
import base58
import qrcode
from bip38 import BIP38
from bip38.cryptocurrencies import Bitcoin as Key
from bitcoin import encode_privkey  # Assurez-vous d'avoir la bibliothèque `bitcoin` installée

app = Flask(__name__)

# Dossier pour stocker les QR codes
QR_FOLDER = "static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

def encrypt_bip38(password, private_key):
    """Chiffre la clé privée avec BIP38"""
    bip38 = BIP38(Key)
    return bip38.encrypt(private_key, password)

def generate_private_key():
    """Génère une clé privée Bitcoin (256 bits)"""
    return os.urandom(32)

def private_key_to_wif(private_key):
    """Convertit la clé privée en format WIF"""
    extended_key = b'\x80' + private_key
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    return base58.b58encode(extended_key + checksum).decode()

def private_key_to_public_key(private_key):
    """Génère une clé publique à partir d'une clé privée"""
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    return b'\x04' + sk.verifying_key.to_string()

def public_key_to_address(public_key):
    """Convertit une clé publique en adresse Bitcoin"""
    ripemd160_bpk = hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()
    extended_ripemd160 = b'\x00' + ripemd160_bpk
    checksum = hashlib.sha256(hashlib.sha256(extended_ripemd160).digest()).digest()[:4]
    return base58.b58encode(extended_ripemd160 + checksum).decode()

def generate_qr_code(data, filename):
    """Génère un QR code et retourne le chemin"""
    img = qrcode.make(data)
    path = os.path.join(QR_FOLDER, filename)
    img.save(path)
    return f"/{path}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form.get('password', None)
        private_key = generate_private_key()

        wif_key = private_key_to_wif(private_key)

        if password:
            wif_key = encrypt_bip38(password, encode_privkey(private_key.hex(), 'wif'))

        public_key = private_key_to_public_key(private_key)
        address = public_key_to_address(public_key)

        private_qr_path = generate_qr_code(wif_key, "private_qr.png")
        address_qr_path = generate_qr_code(address, "address_qr.png")

        return render_template('index.html', address=address, wif_key=wif_key, 
                               private_qr=private_qr_path, address_qr=address_qr_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
