import requests
from bs4 import BeautifulSoup
import os


file = open("database.csv", "w")

URL = "http://127.0.0.1:5500/web_content/index.html"

page = requests.get(URL)

# create soup
soup = BeautifulSoup(page.content, "html.parser")


table = soup.find("table", class_="table")
# print(table)

table_head = table.find_all("thead")[0]
# print(table_head)

table_body = table.find_all("tbody")[0]
# print(table_body)

table_head_rows = table_head.find_all("tr")
# print(table_head_rows)

table_body_rows = table_body.find_all("tr")
# print(table_body_rows)


column_names = ""
column_headings = table_head_rows[0].find_all("th")[1:]

for i, row in enumerate(column_headings):
    # print(row.text.strip())
    if i != len(column_headings) - 1:
        column_names += row.text.strip() + ","
    else:
        column_names += row.text.strip()


file.write(column_names)

for row in table_body_rows:
    table_data = row.find_all("td")
    # print(table_data)

    new_row_data = "\n"
    for i, td in enumerate(table_data):
        # print(td.text.strip())

        if i != len(table_data) - 1:
            new_row_data += td.text.strip() + ","
        else:
            new_row_data += td.text.strip()
    # new_row_data += "\n"
    file.write(new_row_data)


file.close()
