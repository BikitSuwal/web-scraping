import requests
from bs4 import BeautifulSoup

url = requests.get("https://quotes.toscrape.com/")

response = url

soup = BeautifulSoup(response.text, "html.parser")

print("Title:",soup.title.string)

quotes = soup.find_all("div",class_='quote')
for q in quotes:
    text = q.find('span',class_='text').text
    author = q.find('small',class_='author').text
    print(f"{text}-{author}")

