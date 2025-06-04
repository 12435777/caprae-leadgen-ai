import requests
from bs4 import BeautifulSoup
import sqlite3

def fetch_leads():
    url = "https://example.com/leads"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    leads = []
    for item in soup.select(".lead-card"):
        name = item.select_one(".name").text.strip()
        email = item.select_one(".email").text.strip()
        leads.append((name, email))

    conn = sqlite3.connect("lead_demo.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS leads (name TEXT, email TEXT)")
    c.executemany("INSERT INTO leads VALUES (?, ?)", leads)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    fetch_leads()
