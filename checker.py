import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

log_file = open("output.txt", "a")

def log_and_print(message):
    log_file.write(message + "\n")

website_url = "https://webs.iiitd.edu.in/"

def fetch_sitemap(sitemap_path):
    try:
        with open(sitemap_path, "r", encoding="utf-8") as file:
            tree = ET.parse(file)
            root = tree.getroot()
            urls = [elem.text for elem in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
            return set(urls)
    except Exception as e:
        print(f"Error reading sitemap: {e}")
        return set()

def fetch_indexed_pages(website_url, tex):
    try:
        response = requests.get(website_url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, tex)

        indexed_urls = set()
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if href.startswith("http"):  # Absolute URL
                indexed_urls.add(href)
            elif href.startswith("/"):  # Relative URL
                indexed_urls.add(website_url.rstrip("/") + href)
        return indexed_urls
    except requests.RequestException as e:
        print(f"Error fetching website index: {e}")
        return set()

sitemap_file = "sitemap_toxinpred3.xml"

sitemap_urls = fetch_sitemap(sitemap_file)
indexed_urls = fetch_indexed_pages(website_url, tex='lxml')

extra_in_sitemap = sitemap_urls - indexed_urls
missing_in_sitemap = indexed_urls - sitemap_urls

print("URLs in Sitemap but NOT found on the website:")
log_and_print("URLs in Sitemap but NOT found on the website")
for url in extra_in_sitemap:
    print(f"- {url}")
    log_and_print(url)

print("URLs on Website but MISSING in Sitemap:")
log_and_print("URLs on Website but MISSING in Sitemap")
for url in missing_in_sitemap:
    print(f"- {url}")
    log_and_print(url)

print("Total URLs in Sitemap:", len(sitemap_urls))
print("Total Indexed URLs:", len(indexed_urls))