from bs4 import BeautifulSoup
import requests
import csv

URL = "https://en.wikipedia.org/wiki/Machine_learning"

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
# find the tables in this div
tables = div_contents.find_all("table")
for table in tables:
    rows = table.find_all("tr")
    #count rows that contain actual data
    data_rows = [row for row in rows if row.find_all("td")]

    if len(data_rows) >= 3:
        first_table = table
        break
table_headers = first_table.find_all("th")
if table_headers:
    headers=[th.get_text().strip()for th in table_headers]
else:
    for row in data_rows:
        cols = row.find_all(["td", "th"])
        if len(cols) > max_cols:
            max_cols = len(cols)
    headers = [f"col{i + 1}" for i in range(max_cols)]
table_data = []
for row in first_table.find_all("tr"):
    columns = row.find_all(["td", "th"])
    if not columns:
        continue

    row_data = [column.get_text().strip() for column in columns]
    table_data.append(row_data)

#  Pad rows with fewer columns
max_columns = max(len(r) for r in table_data)

for r in table_data:
    while len(r) < max_columns:
        r.append("")

# Save to CSV
with open("wiki_table.csv", mode="w") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(table_data)

print("Table saved to wiki_table.csv")