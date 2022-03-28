import requests

URL = "http://127.0.0.1:5500/web_content/index.html"

page = requests.get(URL)

# print(page)
print(page.text)