from bs4 import BeautifulSoup
import requests

from Assignment2.Data221_Assignment2_Question8 import clean_headings

URL = "https://en.wikipedia.org/wiki/Data_science"

#I get this header from CPSC 217 as I cannot access to the Wikipedia by using simple requests.get(URL)
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, like Gecko) "
"Chrome/124.0.0.0 Safari/537.36"
}
wikipedia_html = requests.get(URL, headers=headers).text
parsed_html_document = BeautifulSoup(wikipedia_html,"html5lib")

#extract and print the page title
titleTag = parsed_html_document.find("title")
print("Page title: ", titleTag.text.strip())

#find the main content div id mw-content-text
div_contents = parsed_html_document.find("div", id="mw-content-text")

#find the first paragraph in the div_content
paragraphs_in_div = div_contents.find_all("p")

for p in paragraphs_in_div:
    text = p.get_text().strip()
    if len(text)>=50:
        print(text)
        break

