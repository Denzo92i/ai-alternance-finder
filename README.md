# 🔍 AI-Alternance-Finder

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/web%20scraping-FFA500?style=for-the-badge&logo=python&logoColor=white">
</p>

> Outil d'automatisation de veille pour la recherche d'alternance en informatique.

## 🚀 À propos du projet
Ce projet est un outil de **web scraping** conçu pour automatiser la collecte d'offres d'alternance dans les domaines de l'IA, de la Data et du développement. Il permet de pallier la navigation manuelle fastidieuse sur les plateformes d'emploi en extrayant et listant les opportunités en temps réel.

## 🛠️ Stack Technique
- **Langage** : Python
- **Bibliothèques** : `Requests`, `BeautifulSoup4`
- **Domaine** : Automatisation, Data Collection, Veille technologique

## ⚙️ Fonctionnalités
- ✅ **Collecte automatique** : Récupération ciblée des offres sur Remotive.
- ✅ **Filtrage intelligent** : Extraction automatique des titres de postes et des liens directs.
- ✅ **Formatage clair** : Affichage structuré des résultats dans le terminal pour une lecture rapide.

## 📸 Aperçu du résultat
![Résultat du scraper](Capture%20d'écran%202026-06-22%20071815.png)

## 🛠️ Installation et Utilisation

```bash
# 1. Cloner le dépôt
git clone [https://github.com/Denzo92i/ai-alternance-finder.git](https://github.com/Denzo92i/ai-alternance-finder.git)
cd ai-alternance-finder

# 2. Créer et activer l'environnement virtuel
python -m venv venv
.\venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer le scraper
python scraper.py
