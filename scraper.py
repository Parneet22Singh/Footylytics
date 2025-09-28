from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup, Comment
import pandas as pd
import os
import time

def scrape_fbref_stats_auto(url):
    dataset_dir = "dataset"
    output_csv = os.path.join(dataset_dir, "fbref_stats_auto.csv")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    print("Launching headless Chrome")
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)

        time.sleep(7)  # wait for page & JS to load

        html = driver.page_source
    except Exception as e:
        print(f"Webdriver error: {e}")
        return pd.DataFrame()
    finally:
        driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    for c in comments:
        if '<table' in c:
            comment_soup = BeautifulSoup(c, "html.parser")
            table = comment_soup.find("table")
            if table:
                headers = [th.get_text(strip=True) for th in table.find_all('th')]
                if any(h in headers for h in ["Player", "Squad"]):
                    print("Found table with relevant headers:", headers)
                    rows = []
                    for row in table.find_all("tr"):
                        cols = row.find_all("td")
                        if cols:
                            rows.append([col.get_text(strip=True) for col in cols])
                    if rows:
                        os.makedirs(dataset_dir, exist_ok=True)
                        df = pd.DataFrame(rows, columns=headers[:len(rows[0])])
                        df.to_csv(output_csv, index=False)
                        print(f"Scraped {len(df)} rows. Saved to {output_csv}")
                        print(df.head())
                        return df

    print("No suitable table found.")
    return pd.DataFrame()

if __name__ == "__main__":
    url = "https://fbref.com/en/comps/9/2024-2025/stats/2024-2025-Premier-League-Stats"
    scrape_fbref_stats_auto(url)
