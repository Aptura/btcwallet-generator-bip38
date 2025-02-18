#!/bin/bash

echo "📦 Installation de l'environnement virtuel et des dépendances..."

# Vérifier si Python 3 est installé
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 n'est pas installé. Installez-le avant de continuer."
    exit 1
fi

# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate

# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances
pip install --no-cache-dir -r requirements.txt

echo "✅ Installation terminée. Pour lancer l'application, exécutez :"
echo "source venv/bin/activate && python app.py"
