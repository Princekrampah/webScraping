import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:5500/web_content/index.html"

page = requests.get(URL)


# create soup
soup = BeautifulSoup(page.content, "html.parser")


# print the soup object
# print(soup)


# print the prettified version of soup object
# print(soup.prettify())


# find element by ID

result = soup.find(id="page-heading")

# print(result)

# print(result.prettify())

result = soup.find_all("div", class_="row")

# print(result)

# for row in result:
#     print(row, end="\n"*4)


# for row in result:
#     row_heading = row.find("h3", id="page-heading")
#     print(row_heading)


# Extract text

# for row in result:
#     row_heading = row.find("h3", id="page-heading")
#     if row_heading is not None:
#         # print(row_heading.text)

#         # drop all the extra spaces around the text
#         print(row_heading.text.strip())


# Find by string
# h3_header = soup.find_all("h3", string="Welcome to my NFT market place..!!")
# print(h3_header)

# h3_header = soup.find_all(
#     "h3", string=lambda text: "welcome" in text.lower()
# )
# print(h3_header)

# Finding Parent elements
# rows = soup.find_all("div", class_="row")
# row_parents = [row_element.parent.parent.parent for row_element in rows]
# print(row_parents)


# find a given tag
a_tags = soup.find_all("a")
print(a_tags)

for a_tag in a_tags:
    print(a_tag["href"])

