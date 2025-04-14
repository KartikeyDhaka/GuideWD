import os
import xml.etree.ElementTree as ET
from tqdm import tqdm
from bs4 import BeautifulSoup
import requests

print('''Welcome to GuideWD developed under the guidance of Prof. GPS Raghava''')
print("Enter 'h' for help or 'i' to input URL and Sitemap Generation or 'o' for Output Generation or 'r' for reading Sitemap or 'q' for force quit")

def show_help():
    print("""
Help - Sitemap Generator

This script walks through a given directory and generates a sitemap.xml file
containing URLs for all .html and .php files.

Options:
  h - Show this help message.
  i - Start sitemap generation.
  r - Reads the generated sitemap.
  o - Output generation.
  q - Force quit program.
""")

def generate_sitemap(directory, input_url):
    base_url = input_url
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    # Walk through the directory and find .html and .php files
    print("Scanning files...")
    for root, _, files in tqdm(os.walk(directory), desc=f'Files crawling'):
        for file in files:
            if file.endswith(('.html', '.php')):
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                url = base_url + relative_path.replace(os.path.sep, '/')

                url_element = ET.SubElement(urlset, "url")
                loc_element = ET.SubElement(url_element, "loc")
                loc_element.text = url

    # Generate the XML tree
    tree = ET.ElementTree(urlset)
    with open("sitemap.xml", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

    print("Sitemap generated as sitemap.xml")

def read_sitemap(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print("Reading sitemap...")

        # Display XML structure
        for url in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
            print(url.text)
    except Exception as e:
        print(f"Error reading sitemap: {e}")

def log_and_print(message, log_file):
    log_file.write(message + "\n")

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

input_url = input("Enter a valid base URL: ")
sitemap_file_path = "sitemap.xml"

def main_menu(input_url, sitemap_file_path):
    while True:
        choice = input("Enter your choice: ").lower()
        if choice == 'h':
            show_help()
        elif choice == 'i':
            directory_path = "/home/gpsr/webserver/cgidocs"
            generate_sitemap(directory_path, input_url)
        elif choice == 'r':
            read_sitemap(sitemap_file_path)
        elif choice == 'o':
            log_file = open("output.txt", "a")
            website_url = input_url
            sitemap_file = sitemap_file_path

            sitemap_urls = fetch_sitemap(sitemap_file)
            indexed_urls = fetch_indexed_pages(website_url, tex='lxml')

            extra_in_sitemap = sitemap_urls - indexed_urls
            missing_in_sitemap = indexed_urls - sitemap_urls

            print("URLs in Sitemap but NOT found on the website:")
            log_and_print("URLs in Sitemap but NOT found on the website", log_file)
            for url in extra_in_sitemap:
                print(f"- {url}")
                log_and_print(url, log_file)

            print("URLs on Website but MISSING in Sitemap:")
            log_and_print("URLs on Website but MISSING in Sitemap", log_file)

            for url in missing_in_sitemap:
                print(f"- {url}")
                log_and_print(url, log_file)

            print("Total URLs in Sitemap:", len(sitemap_urls))
            print("Total Indexed URLs:", len(indexed_urls))
        elif choice == 'q':
            break
        else:
            print("Invalid input. Please enter 'h', 'i', 'r', 'o' or 'q'.")

main_menu(input_url, sitemap_file_path)