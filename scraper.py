import requests
from bs4 import BeautifulSoup

url = "https://www.remotive.com"
response = requests.get(url, verify=False)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

titre_page = soup.find("h1").text
print("Titre :", titre_page)

liens = soup.find_all("a")

offres = set()
print("\nOffres Trouvés:")

categories = ["software-development", "ai-ml", "data", "devops"]

for lien in liens:
    href = lien.get("href")
    titre = " ".join(lien.text.split()).split("•")[0]

    if href and href.startswith("https://remotive.com/remote-jobs/"):
        if any(cat in href for cat in categories):
            if titre and "View Job" not in titre:
                offres.add((titre, href))

for titre, lien in offres:
    print(f"{titre} → {lien}")