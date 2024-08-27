import requests
from bs4 import BeautifulSoup

url = "https://thegreatdevices.com/product/%d9%85%d9%83%d9%8a%d9%81-%d8%b3%d8%a8%d9%84%d8%aa-%d8%aa%d9%84%d9%8a%d8%b2%d9%88%d9%86-22000-%d9%88%d8%ad%d8%af%d8%a9-%d8%b1%d9%88%d8%aa%d8%a7%d8%b1%d9%8a-%d8%a8%d8%a7%d8%b1%d8%af-%d9%88-%d8%ad/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title.text)
