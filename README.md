<h1>GuideWD</h1>
<h2>Why sitemaps are important:</h2>
Sitemaps are crucial in enhancing website visibility by helping search engines index content effectively. They act as a roadmap, guiding search engine crawlers to discover all the relevant pages within a site. This ensures better search engine optimization (SEO) and improves the likelihood of content being ranked higher in search results.

<h2>Instructions:</h2>

**At Server End:**
1) Firstly run the `sitemap_generator.py` file using the command:

   ```bash
   python sitemap_generator.py
   ```

   Provide the input as URLs, for example:

   ```bash
   http://webs.iiitd.edu.in/raghava/toxinpred3/
   ```

   The script will walk through the directory `/home/gpsr/webserver/cgidocs` using `os.walk()` and identify `.html` and `.php` files. It will then generate a structured XML sitemap using the XML sitemap schema (http://www.sitemaps.org/schemas/sitemap/0.9) and store the sitemap file as `sitemap_toxinpred3.xml`.

2) Secondly, run the `checker.py` file using the following command:

   ```bash
   python checker.py
   ```

   Provide the same input URL:

   ```bash
   http://webs.iiitd.edu.in/raghava/toxinpred3/
   ```

   This file reads the generated sitemap using `ET.parse()`, extracts and prints all URLs within the `<loc>` tags using `root.findall()`, and handles exceptions with appropriate error messages.

**At Local Machine End:**
1) In the file Sitemap_Generator_and_Comparision.ipynb, the process begins by fetching HTML content from a specified URL using the requests library. After downloading the HTML, the script proceeds with tag identification, where BeautifulSoup is used to parse and classify HTML tags, identifying standard, deprecated, and custom/private tags. Next, the script performs HTML cleaning, removing any private tags to ensure the HTML is free of unnecessary elements. Following this, sitemap generation takes place, where all valid URLs from the website are extracted and compiled into an XML sitemap. The sitemaps are then compared using difflib to detect any structural differences between the two sitemaps or web pages. Finally, sitemap accuracy calculation is performed by measuring the coverage of the generated sitemap, evaluating the intersection between the generated URLs and the indexed URLs.

2) In the file **Sitemap_Generator_Threats_and_Security.ipynb**, the script performs comprehensive **security analysis** on the HTML content. It starts by **extracting and parsing** the HTML using the `requests` library to fetch the content from the given URL, with `BeautifulSoup` used for parsing the HTML through both `lxml` and `html.parser`. To simulate browser behavior, headers with a user-agent are included in the requests, and appropriate error messages are displayed in case of failed requests. The script then moves on to **private tag detection and HTML cleaning**, where custom or non-standard tags are identified by comparing them against a set of standard tags, and deprecated tags (such as `<font>`, `<marquee>`, and `<center>`) are flagged. Private tags are removed using regex patterns, and a clean version of the HTML is regenerated. The differences between the original and cleaned HTML are displayed using the `difflib.unified_diff` method. For **SEO analysis**, the script checks for key components such as the presence of a `<title>` tag (limited to 60 characters), the existence and length of meta descriptions, the presence of `<h1>` tags, the availability of a `robots.txt` file, missing alt attributes in `<img>` tags, and mobile responsiveness via the viewport meta tag. Lastly, for **threat detection**, the script scans the HTML for potential malicious patterns using regex (such as `eval()` and `document.write()`), flags deprecated HTML tags as security risks, and checks for outdated versions of commonly used libraries like jQuery and Bootstrap.

<h2>Work done:</h2>

1) **Sitemap generation and security analysis.** For sitemap generation, two approaches are used. First, with lxml and html.parser, the HTML content is fetched using the requests library, then parsed and tagged using BeautifulSoup. Non-standard or private tags are removed, and valid URLs are extracted to generate an XML sitemap. The sitemap is compared for structural differences using difflib, and its accuracy is evaluated by intersecting generated URLs with indexed ones. The second approach uses server files, where the os.walk() method traverses the server directory to identify .html and .php files, converting paths to URLs. These URLs are used to generate a structured XML sitemap, which is saved as sitemap_toxinpred3.xml. The generated sitemap is then parsed using xml.etree.ElementTree to extract URLs.

2)  **Security analysis:** The HTML content is fetched and parsed using requests and BeautifulSoup (with both lxml and html.parser). User-agent headers are included to simulate browser requests. The script detects and removes custom or deprecated HTML tags, and displays differences between the original and cleaned HTML using difflib.unified_diff. SEO checks are performed to verify the presence of critical tags such as <title>, meta descriptions, h1 tags, alt attributes, and mobile responsiveness. Additionally, the script scans for security threats by detecting malicious patterns (e.g., eval(), document.write()), flags deprecated HTML tags, and checks for outdated libraries like jQuery and Bootstrap.
