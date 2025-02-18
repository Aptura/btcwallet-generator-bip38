# 🚀 Bitcoin Wallet Generator (BIP39 + BIP84 Bech32)

Ce projet est une application web permettant de générer des wallets Bitcoin compatibles avec **BIP39** et **BIP84**, créant ainsi des adresses **Bech32** (`bc1...`), plus sécurisées et modernes.

## 📌 Fonctionnalités

Utiliser ce programme uniquement en local.

✅ Génération d'une **phrase mnémonique BIP39** (avec passphrase optionnelle)\
✅ Conversion de la phrase en **clé privée WIF** et adresse Bitcoin Bech32 (`bc1...`)
<br>
✅ Affichage et **protection de la clé privée** (cliquable pour masquer/afficher)\
✅ **Génération de QR codes** pour la phrase mnémonique, l'adresse et la clé privée\
✅ **Interface web moderne et responsive**

## 🖥 Installation automatique

### 🔹 Linux/macOS

```bash
chmod +x install.sh && ./install.sh
```

### 🔹 Windows

```bat
install.bat
```

## 🔧 Installation et utilisation manuelle

### 1️⃣ Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.10+** ([Télécharger ici](https://www.python.org/downloads/))
- **pip** (normalement inclus avec Python)
- **Git** (optionnel, mais recommandé pour cloner le projet)

### 2️⃣ Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/bitcoin_wallet_generator.git
cd bitcoin_wallet_generator
```

(Si vous n'avez pas Git, téléchargez le projet en ZIP depuis GitHub et extrayez-le)

### 3️⃣ Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

### 4️⃣ Installer les dépendances

```bash
pip install --no-cache-dir -r requirements.txt
```

### 5️⃣ Lancer l'application

```bash
python app.py
```

Si le port 5000 est déjà utilisé :

```bash
python app.py --port 5001
```

Ensuite, ouvrez **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** dans votre navigateur.

## 🔄 Importer votre wallet dans Electrum

Si vous souhaitez utiliser votre wallet dans Electrum :

1️⃣ **Ouvrir Electrum** et créer un **nouveau portefeuille** <br>
2️⃣ Choisir **"Standard Wallet"** puis **"Je possède déjà une phrase mnémonique"** <br>
3️⃣ Entrer la phrase mnémonique générée par l'application <br>
4️⃣ Vérifier que **BIP39 est détecté** et cocher "BIP39 seed" <br>
5️⃣ Sélectionner **"Native SegWit (bech32)"** pour générer des adresses `bc1...`

## 🛠 Dépannage

### ❌ **Problème : "ModuleNotFoundError"**

👉 Assurez-vous d'avoir installé les dépendances correctement :

```bash
pip install --no-cache-dir -r requirements.txt
```

### ❌ **Problème : "Address already in use"**

👉 Un autre processus utilise déjà le port 5000. Essayez :

```bash
python app.py --port 5001
```

### ❌ **Clé privée WIF rejetée par Electrum**

👉 Electrum fonctionne avec des portefeuilles **HD (BIP39/BIP84)**. Importer uniquement une clé privée WIF créera un portefeuille limité à une seule adresse.

🔹 **Solution** : Importez **la phrase mnémonique** au lieu de la clé privée.

## 🤝 Contribution

Vous pouvez proposer des améliorations en ouvrant une issue ou en faisant une pull request.

Si vous trouvez ce projet utile, vous pouvez faire une donation BTC : **bc1qqjzdu6d7jw6zfl9aplgqpc3x2msjjrpj0spknl**

## 📝 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le partager.
