<h1>GuideWD</h1>
<h2>Why sitemaps are important:</h2>
Sitemaps are crucial in enhancing website visibility by helping search engines index content effectively. They act as a roadmap, guiding search engine crawlers to discover all the relevant pages within a site. This ensures better search engine optimization (SEO) and improves the likelihood of content being ranked higher in search results.

<h2>Instructions:</h2>

**At Server End:**

<h3>Description:</h3>
GuideWD is a Python utility that generates a sitemap.xml from all .html and .php files within a web directory, compares it against a live website's indexed pages, and outputs a report of discrepancies. It is helpful for developers and web admins to ensure consistency between their sitemap and actual site structure.

<h3>How to Run:</h3>

1) Firstly run the `sitemap_generator_final1.py` file using the command:

   ```bash
   python sitemap_generator_final1.py.py
   ```

   Provide the input as URLs, for example:

   ```bash
   http://webs.iiitd.edu.in/raghava/clbtope/
   ```

2) Options:

h – Show help message describing available options.

i – Generate sitemap.xml from the local directory /home/gpsr/webserver/cgidocs using the base URL you input at the beginning.

r – Reads and displays the contents of the generated sitemap.xml.

o – Compares the URLs in sitemap.xml with the actual URLs found on the live website:
'''Lists URLs present in the sitemap but missing from the site.
Lists URLs present on the site but not included in the sitemap.
Saves the report in output.txt.'''

q – Exit the program.

   The script will walk through the directory `/home/gpsr/webserver/cgidocs` using `os.walk()` and identify `.html` and `.php` files. It will then generate a structured XML sitemap using the XML sitemap schema (http://www.sitemaps.org/schemas/sitemap/0.9) and store the sitemap file as `sitemap.xml` and `output.txt` will contain the comparison report of sitemap vs website URLs.
   
3) Example Flow:

Launch script.

Input your website’s base URL.

Press i to generate the sitemap.

Press r to review it.

Press o to compare with the website and generate the output log.

Press q to quit the from the running code

## At Local Machine End:

- *Fetching HTML Content:* The process begins in `Sitemap_Generator_and_Comparision.ipynb` by retrieving HTML content from a specified URL using the `requests` library.  
- *Tag Identification:* `BeautifulSoup` is used to parse and classify HTML tags into standard, deprecated, and custom/private categories.  
- *HTML Cleaning:* Private tags are removed to ensure a clean HTML structure without unnecessary elements.  
- *Sitemap Generation:* Extracts all valid URLs from the website and compiles them into an XML sitemap.  
- *Sitemap Comparison:* Uses `difflib` to detect structural differences between the generated sitemaps or web pages.  
- *Sitemap Accuracy Calculation:* Evaluates sitemap coverage by measuring the intersection between generated URLs and indexed URLs.  

## At Local Machine End: Security Analysis

- *Fetching and Parsing HTML:*  
  - The process begins in `Sitemap_Generator_Threats_and_Security.ipynb`, where HTML content is fetched using the `requests` library.  
  - `BeautifulSoup` is used to parse HTML via both `lxml` and `html.parser`.  
  - To simulate browser behavior, user-agent headers are included, and appropriate error messages are displayed for failed requests.  

- *Private Tag Detection & HTML Cleaning:*  
  - Custom or non-standard tags are identified by comparing them with a predefined set of standard tags.  
  - Deprecated tags such as `<font>`, `<marquee>`, and `<center>` are flagged.  
  - Private tags are removed using regex, and a clean version of the HTML is generated.  
  - Differences between original and cleaned HTML are displayed using `difflib.unified_diff`.  

- *SEO Analysis:*  
  - Checks for the presence of a `<title>` tag (ensuring it is within 60 characters).  
  - Evaluates the existence and length of meta descriptions.  
  - Confirms the presence of `<h1>` tags and a `robots.txt` file.  
  - Detects missing `alt` attributes in `<img>` tags.  
  - Verifies mobile responsiveness through the viewport meta tag.  

- *Threat Detection:*  
  - Scans for potential malicious patterns in the HTML using regex (e.g., `eval()`, `document.write()`).  
  - Flags deprecated HTML tags that may pose security risks.  
  - Checks for outdated versions of commonly used libraries like jQuery and Bootstrap.

## Installation
   ```bash
git clone https://github.com/your-username/GuideWD.git
cd GuideWD
pip install -r requirements.txt
   ```

<h2>Work done:</h2>

1) **Sitemap generation and security analysis.** For sitemap generation, two approaches are used. First, with lxml and html.parser, the HTML content is fetched using the requests library, then parsed and tagged using BeautifulSoup. Non-standard or private tags are removed, and valid URLs are extracted to generate an XML sitemap. The sitemap is compared for structural differences using difflib, and its accuracy is evaluated by intersecting generated URLs with indexed ones. The second approach uses server files, where the os.walk() method traverses the server directory to identify .html and .php files, converting paths to URLs. These URLs are used to generate a structured XML sitemap, which is saved as sitemap_toxinpred3.xml. The generated sitemap is then parsed using xml.etree.ElementTree to extract URLs.

2)  **Security analysis:** The HTML content is fetched and parsed using requests and BeautifulSoup (with both lxml and html.parser). User-agent headers are included to simulate browser requests. The script detects and removes custom or deprecated HTML tags, and displays differences between the original and cleaned HTML using difflib.unified_diff. SEO checks are performed to verify the presence of critical tags such as <title>, meta descriptions, h1 tags, alt attributes, and mobile responsiveness. Additionally, the script scans for security threats by detecting malicious patterns (e.g., eval(), document.write()), flags deprecated HTML tags, and checks for outdated libraries like jQuery and Bootstrap.
