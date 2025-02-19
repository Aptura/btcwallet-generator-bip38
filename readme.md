# 🚀 Bitcoin Wallet Generator (BIP39 + BIP84 Bech32)

This project is a web application for generating Bitcoin wallets compatible with **BIP39** and **BIP84**, creating **Bech32** addresses (`bc1...`), which are more secure and modern.

## 📌 Features

Use this program **only locally**.

✅ Generate a **BIP39 mnemonic phrase** (with optional passphrase)\
✅ Convert the phrase into a **WIF private key** and Bitcoin Bech32 address (`bc1...`)
<br>
✅ Display and **protect the private key** (clickable to hide/show)\
✅ **Generate QR codes** for the mnemonic phrase, address, and private key\
✅ **Modern and responsive web interface**

## 🖥 Automatic Installation

### 🔹 Linux/macOS

```bash
chmod +x install.sh && ./install.sh
```

### 🔹 Windows

```bat
install.bat
```

## 🔧 Manual Installation and Usage

### 1️⃣ Prerequisites

Before starting, make sure you have installed:

- **Python 3.10+** ([Download here](https://www.python.org/downloads/))
- **pip** (usually included with Python)
- **Git** (optional but recommended for cloning the project)

### 2️⃣ Clone the Project

```bash
git clone https://github.com/your-username/bitcoin_wallet_generator.git
cd bitcoin_wallet_generator
```

(If you don’t have Git, download the ZIP file from GitHub and extract it)

### 3️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash
pip install --no-cache-dir -r requirements.txt
```

### 5️⃣ Run the Application

```bash
python app.py
```

If port 5000 is already in use:

```bash
python app.py --port 5001
```

Then open **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in your browser.

## 🔄 Import Your Wallet into Electrum

If you want to use your wallet in Electrum:

1️⃣ **Open Electrum** and create a **new wallet** <br>
2️⃣ Choose **"Standard Wallet"**, then **"I already have a seed phrase"** <br>
3️⃣ Enter the mnemonic phrase generated by the application <br>
4️⃣ Make sure **BIP39 is detected** and check "BIP39 seed" <br>
5️⃣ Select **"Native SegWit (bech32)"** to generate `bc1...` addresses

## 🔍 Verify Bech32 Address (`verify_bech32.py`)

The script `verify_bech32.py` allows you to verify that a **Bech32 Bitcoin address** correctly corresponds to the mnemonic phrase and its private key.

### 🛠 How It Works

1️⃣ It takes a **BIP39 mnemonic phrase** and an **optional passphrase**.
2️⃣ It derives the **BIP84 (SegWit Bech32) private key and address**.
3️⃣ It compares the generated address to the expected one.
4️⃣ It returns whether they match.

### 🔹 Example Usage

```python
from bip_utils import Bip39SeedGenerator, Bip84, Bip84Coins, Bip44Changes

def verify_address(mnemonic, passphrase, expected_address):
    """ Verifies that the generated Bech32 address matches the private key. """

    # Generate the seed from the mnemonic phrase
    seed = Bip39SeedGenerator(mnemonic).Generate(passphrase)

    # Create the BIP84 structure for Bitcoin (SegWit Bech32)
    bip84 = Bip84.FromSeed(seed, Bip84Coins.BITCOIN)
    bip84_acc = bip84.Purpose().Coin().Account(0)  # Account level
    bip84_chg = bip84_acc.Change(Bip44Changes.CHAIN_EXT)  # External change
    bip84_addr = bip84_chg.AddressIndex(0)  # First address

    # Retrieve the address and private key
    generated_address = bip84_addr.PublicKey().ToAddress()
    private_key_wif = bip84_addr.PrivateKey().ToWif()

    # Verify the address
    match = generated_address == expected_address

    return {
        "mnemonic": mnemonic,
        "private_key_wif": private_key_wif,
        "generated_address": generated_address,
        "expected_address": expected_address,
        "match": match
    }

# Example usage with test values
mnemonic_test = "zone custom next define truth expand version focus gentle immune dumb era kind fire tired uphold trust document pull kitchen decline clay raven menu"
passphrase_test = ""
expected_address_test = "bc1qfprx5kkkmalweumwfyeu0t8lwwntlzmp3vzp7r"  # Replace with your expected address

result = verify_address(mnemonic_test, passphrase_test, expected_address_test)

# Display results
print("📜 Mnemonic Phrase: ", result["mnemonic"])
print("🔑 Private Key (WIF): ", result["private_key_wif"])
print("🏦 Generated Address: ", result["generated_address"])
print("🎯 Expected Address: ", result["expected_address"])
print("✅ Match: ", "Yes" if result["match"] else "No")
```

## 🛠 Troubleshooting

### ❌ **Issue: "ModuleNotFoundError"**

👉 Make sure you have installed the dependencies correctly:

```bash
pip install --no-cache-dir -r requirements.txt
```

### ❌ **Issue: "Address already in use"**

👉 Another process is using port 5000. Try:

```bash
python app.py --port 5001
```

### ❌ **WIF Private Key Rejected by Electrum**

👉 Electrum works with **HD wallets (BIP39/BIP84)**. Importing only a WIF private key creates a wallet limited to a single address.

🔹 **Solution**: Import the **mnemonic phrase** instead of the private key.

## 🤝 Contribution

You can suggest improvements by opening an issue or submitting a pull request.

If you find this project useful, you can donate BTC: **bc1qqjzdu6d7jw6zfl9aplgqpc3x2msjjrpj0spknl**

## 📝 License

This project is under the MIT License. You are free to use, modify, and share it.

