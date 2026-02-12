from bs4 import BeautifulSoup
import requests


URL = "https://en.wikipedia.org/wiki/Data_science"

#I get this header from CPSC 217 as I cannot access to the Wikipedia by using simple requests.get(URL)
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, like Gecko) "
"Chrome/124.0.0.0 Safari/537.36"
}
wikipedia_html = requests.get(URL, headers=headers).text
parsed_html_document = BeautifulSoup(wikipedia_html,"html5lib")
#find the main content div id mw-content-text
div_contents = parsed_html_document.find("div", id="mw-content-text")

h2_headings = div_contents.find_all("h2")

clean_headings = []
for h2 in h2_headings:
    heading_text = h2.get_text().strip()
    heading_text = heading_text.replace("[edit]", "").strip()
    if ("References" in heading_text or
        "External links" in heading_text or
        "See also" in heading_text or
        "Notes" in heading_text):
        continue
    clean_headings.append(heading_text)

with open(file="C:/Users/thanh/PycharmProjects/DATA 221/Assignment2/headings.txt", mode="w") as file:
    for heading in clean_headings:
        file.write(heading + "\n")
file.close()
