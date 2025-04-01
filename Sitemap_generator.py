import os
import xml.etree.ElementTree as ET

def generate_sitemap(directory):
    base_url = input()
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.html', '.php')):
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                url = base_url + relative_path.replace(os.path.sep, '/')

                url_element = ET.SubElement(urlset, "url")
                loc_element = ET.SubElement(url_element, "loc")
                loc_element.text = url

    # Generate the XML tree
    tree = ET.ElementTree(urlset)
    with open("sitemap_toxinpred3.xml", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

    print("Sitemap generated as sitemap.xml")

directory_path = "/home/gpsr/webserver/cgidocs"
generate_sitemap(directory_path)

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

sitemap_file_path = "sitemap_toxinpred3.xml"
read_sitemap(sitemap_file_path)