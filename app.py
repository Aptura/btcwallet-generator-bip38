from flask import Flask, render_template, request
import os
import qrcode
from bip_utils import Bip39SeedGenerator, Bip84, Bip39MnemonicGenerator, Bip84Coins, Bip44Changes

app = Flask(__name__)

# Dossier pour stocker les QR codes
QR_FOLDER = "static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

def generate_mnemonic():
    """Génère une phrase mnémonique BIP39"""
    return Bip39MnemonicGenerator().FromWordsNumber(24)

def mnemonic_to_seed(mnemonic, passphrase=""):
    """Convertit une phrase mnémonique en seed BIP39"""
    return Bip39SeedGenerator(mnemonic).Generate(passphrase)

def generate_wallet(mnemonic, passphrase=""):
    """Génère une adresse Bech32 (bc1) et sa clé privée à partir d'une phrase mnémonique"""
    seed = mnemonic_to_seed(mnemonic, passphrase)
    bip84 = Bip84.FromSeed(seed, Bip84Coins.BITCOIN)
    bip84_acc = bip84.Purpose().Coin().Account(0)  # Niveau compte
    bip84_chg = bip84_acc.Change(Bip44Changes.CHAIN_EXT)  # Change externe
    bip84_addr = bip84_chg.AddressIndex(0)  # Première adresse

    address = bip84_addr.PublicKey().ToAddress()
    private_key = bip84_addr.PrivateKey().ToWif()  # Clé privée en hexadécimal
    return address, private_key

def generate_qr_code(data, filename):
    """Génère un QR code et retourne le chemin"""
    img = qrcode.make(data)
    path = os.path.join(QR_FOLDER, filename)
    img.save(path)
    return f"/{path}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        passphrase = request.form.get('passphrase', "")
        mnemonic = generate_mnemonic()
        address, private_key = generate_wallet(mnemonic, passphrase)
        
        mnemonic_qr_path = generate_qr_code(mnemonic, "mnemonic_qr.png")
        address_qr_path = generate_qr_code(address, "address_qr.png")
        private_key_qr_path = generate_qr_code(private_key, "private_key_qr.png")
        
        return render_template('index.html', mnemonic=mnemonic, address=address, private_key=private_key,
                               mnemonic_qr=mnemonic_qr_path, address_qr=address_qr_path, private_key_qr=private_key_qr_path)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
