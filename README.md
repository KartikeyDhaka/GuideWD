# **GuideWD**
**Why sitemaps are important:**
Sitemaps are crucial in enhancing website visibility by helping search engines index content effectively. They act as a roadmap, guiding search engine crawlers to discover all the relevant pages within a site. This ensures better search engine optimization (SEO) and improves the likelihood of content being ranked higher in search results.

**Instuctions:**
1) Firstly run the sitemap_generator.py file using command python sitemap_generator.py on terminal and give the input as urls for example: "http://webs.iiitd.edu.in/raghava/toxinpred3/" and it will walks through the directory (/home/gpsr/webserver/cgidocs) using os.walk() and identifies .html and .php files. Afterwards it will generates a structured XML sitemap using the XML sitemap schema (http://www.sitemaps.org/schemas/sitemap/0.9) and store the sitemap file output the XML sitemap to sitemap_toxinpred3.xml.

2) Secondly run checker.py file using command python sitemap_generator.py on terminal and give the input as before: "http://webs.iiitd.edu.in/raghava/toxinpred3/" this file reads the generated sitemap using ET.parse(), extracts and prints all URLs within the <loc> tags using root.findall() and handles exceptions with appropriate error messages.
