import requests
from bs4 import BeautifulSoup
import warnings

# Masquer les avertissements de sécurité (pour la sortie propre en console)
warnings.filterwarnings("ignore")

def run_scraper():
    url = "https://www.remotive.com"
    
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status() # Vérifie si la page répond bien
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la connexion : {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Titre de la page
    header = soup.find("h1")
    titre_page = header.text.strip() if header else "Page d'accueil"
    print(f"--- Scraping de : {titre_page} ---")

    liens = soup.find_all("a")
    offres = set()
    categories = ["software-development", "ai-ml", "data", "devops"]

    # Traitement et filtrage
    for lien in liens:
        href = lien.get("href")
        titre = " ".join(lien.text.split()).split("•")[0].strip()

        if href and href.startswith("https://remotive.com/remote-jobs/"):
            if any(cat in href for cat in categories):
                if titre and "View Job" not in titre:
                    offres.add((titre, href))

    # Affichage soigné
    print(f"\n{'='*80}")
    print(f"📦 {len(offres)} OFFRES D'ALTERNANCE/EMPLOI TROUVÉES :")
    print(f"{'='*80}\n")

    for titre, lien in offres:
        print(f"🔹 {titre}")
        print(f"   {lien}\n")

if __name__ == "__main__":
    run_scraper()