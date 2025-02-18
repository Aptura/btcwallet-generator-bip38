@echo off
echo 📦 Installation de l'environnement virtuel et des dépendances...

:: Vérifier si Python est installé
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python 3 n'est pas installé. Installez-le avant de continuer.
    exit /b
)

:: Créer un environnement virtuel
python -m venv venv

:: Activer l'environnement virtuel
call venv\Scripts\activate

:: Mettre à jour pip
python -m pip install --upgrade pip

:: Installer les dépendances
pip install --no-cache-dir -r requirements.txt

echo ✅ Installation terminée. Pour lancer l'application, exécutez :
echo venv\Scripts\activate && python app.py
pause
