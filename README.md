<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/web%20scraping-FFA500?style=for-the-badge&logo=python&logoColor=white">
</p>

# 🔍 AI-Alternance-Finder

> Outil d'automatisation de veille pour la recherche d'alternance.

## 🚀 À propos du projet
Ce projet est un outil de **web scraping** développé pour automatiser la recherche d'offres d'alternance dans les domaines de l'IA, de la Data et du développement. Plutôt que de naviguer manuellement sur les sites, le script analyse les flux et extrait les opportunités pertinentes.

## 🛠️ Stack Technique
- **Langage :** Python
- **Parsing :** BeautifulSoup4, Requests
- **Domaine :** Automatisation & Data Collection

## ⚙️ Fonctionnalités
- ✅ **Collecte automatique** : Récupération en temps réel des offres depuis Remotive.
- ✅ **Filtrage intelligent** : Tri des offres par mots-clés spécifiques au secteur numérique.
- ✅ **Formatage clair** : Affichage lisible des titres de postes avec liens directs vers les annonces.

## 🛠️ Installation et Utilisation

```bash
# 1. Cloner le dépôt
git clone [https://github.com/Denzo92i/ai-alternance-finder.git](https://github.com/Denzo92i/ai-alternance-finder.git)
cd ai-alternance-finder

# 2. Créer l'environnement virtuel
python -m venv venv
# Windows :
.\venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer le scraper
python scraper.py
