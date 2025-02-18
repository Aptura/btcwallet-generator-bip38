# Bitcoin Wallet Generator

Ce projet est une application web permettant de générer des wallets Bitcoin en toute simplicité, avec une option de chiffrement BIP38.

## 📌 Fonctionnalités

- Génération d'une paire de clés Bitcoin (privée/publique)
- Chiffrement de la clé privée avec un mot de passe (BIP38)
- Génération de QR codes pour la clé privée et l'adresse Bitcoin
- Interface web simple et intuitive

## 🚀 Installation automatique

### 🔹 Linux/macOS

```bash
chmod +x install.sh && ./install.sh
```

### 🔹 Windows

```bat
install.bat
```

## 🔧 Installation et utilisation manuelle

### 1⃣ Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.10+** ([Télécharger ici](https://www.python.org/downloads/))
- **pip** (normalement inclus avec Python)
- **Git** (optionnel, mais recommandé pour cloner le projet)

### 2⃣ Cloner le projet

Ouvrez un terminal (ou PowerShell sous Windows) et exécutez :

```bash
# Clonage du repo
git clone https://github.com/votre-utilisateur/bitcoin_wallet_generator.git
cd bitcoin_wallet_generator
```

(Si vous n'avez pas Git, téléchargez le projet en ZIP depuis GitHub et extrayez-le)

### 3⃣ Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

### 4⃣ Installer les dépendances

```bash
pip install --no-cache-dir -r requirements.txt
```

### 5⃣ Lancer l'application

```bash
python app.py
```

Si le port 5000 est déjà utilisé :

```bash
python app.py --port 5001
```

Le serveur se lance et affiche un message du type :

```html
* Running on http://127.0.0.1:5000/
```

Ouvrez votre navigateur et allez sur **<http://127.0.0.1:5000/>**.

## 🛠 Dépannage

### ❌ **Problème : "command not found" ou "python n'est pas reconnu"**

👉 Solution :

- Vérifiez que Python est bien installé et ajouté au PATH.
- Essayez `python3` à la place de `python`.

### ❌ **Problème : "ModuleNotFoundError"**

👉 Solution : Assurez-vous d'avoir installé les dépendances correctement :

```bash
pip install --no-cache-dir -r requirements.txt
```

### ❌ **Problème : "Address already in use"**

👉 Solution : Un autre processus utilise déjà le port 5000. Essayez :

```bash
python app.py --port 5001
```

### ❌ **Problème : "qrcode" ne fonctionne pas sous Windows**

👉 Solution : Installer `pillow` manuellement :

```bash
pip install pillow
```

## 🤝 Contribution

Vous pouvez proposer des améliorations en ouvrant une issue ou en faisant une pull request.

## 📝 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le partager.
