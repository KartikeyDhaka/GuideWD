# **GuideWD**
**Why sitemaps are important:**
Sitemaps are crucial in enhancing website visibility by helping search engines index content effectively. They act as a roadmap, guiding search engine crawlers to discover all the relevant pages within a site. This ensures better search engine optimization (SEO) and improves the likelihood of content being ranked higher in search results.

****Instuctions:****
1) Firstly run the sitemap_generator.py file using command python sitemap_generator.py on terminal and give the input as urls for example: "http://webs.iiitd.edu.in/raghava/toxinpred3/" and it will walks through the directory (/home/gpsr/webserver/cgidocs) using os.walk() and identifies .html and .php files. Afterwards it will generates a structured XML sitemap using the XML sitemap schema (http://www.sitemaps.org/schemas/sitemap/0.9) and store the sitemap file output the XML sitemap to sitemap_toxinpred3.xml.

2) Secondly run checker.py file using command python sitemap_generator.py on terminal and give the input as before: "http://webs.iiitd.edu.in/raghava/toxinpred3/" this file reads the generated sitemap using ET.parse(), extracts and prints all URLs within the <loc> tags using root.findall() and handles exceptions with appropriate error messages.

****Work done:****
1) **Sitemap generation and security analysis.** For sitemap generation, two approaches are used. First, with lxml and html.parser, the HTML content is fetched using the requests library, then parsed and tagged using BeautifulSoup. Non-standard or private tags are removed, and valid URLs are extracted to generate an XML sitemap. The sitemap is compared for structural differences using difflib, and its accuracy is evaluated by intersecting generated URLs with indexed ones. The second approach uses server files, where the os.walk() method traverses the server directory to identify .html and .php files, converting paths to URLs. These URLs are used to generate a structured XML sitemap, which is saved as sitemap_toxinpred3.xml. The generated sitemap is then parsed using xml.etree.ElementTree to extract URLs.

2)  **security analysis:** The HTML content is fetched and parsed using requests and BeautifulSoup (with both lxml and html.parser). User-agent headers are included to simulate browser requests. The script detects and removes custom or deprecated HTML tags, and displays differences between the original and cleaned HTML using difflib.unified_diff. SEO checks are performed to verify the presence of critical tags such as <title>, meta descriptions, h1 tags, alt attributes, and mobile responsiveness. Additionally, the script scans for security threats by detecting malicious patterns (e.g., eval(), document.write()), flags deprecated HTML tags, and checks for outdated libraries like jQuery and Bootstrap.
