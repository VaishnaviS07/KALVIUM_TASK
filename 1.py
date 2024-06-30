pip install requests beautifulsoup4 pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'table-party'})

parties = []
won = []
leading = []
total = []

for row in table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    parties.append(columns[0].get_text(strip=True))
    won.append(columns[1].get_text(strip=True))
    leading.append(columns[2].get_text(strip=True))
    total.append(columns[3].get_text(strip=True))

df = pd.DataFrame({
    'Party': parties,
    'Won': won,
    'Leading': leading,
    'Total': total
})

df.to_csv('lok_sabha_results_2024.csv', index=False)

print("Election results scraped and saved to lok_sabha_results_2024.csv")
