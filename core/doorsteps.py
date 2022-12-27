import requests
from bs4 import BeautifulSoup
import utils


url = "https://www.doorsteps.com/search/77447"
data = requests.get(url, headers=utils.my_headers())

try:
    print('trying to read localfile')
    with open("../localfiles/doorsteps.html") as f:
        html = f.read()
    print('Local file is available', '#'*18)
except FileNotFoundError:
    print('we are making a HTTP request')
    data = requests.get(url, headers=utils.my_headers())
    with open("doorsteps.html", 'wb') as f:
        f.write(data.content)
    html = data.text
    print('file content written successfully')


soup = BeautifulSoup(html, "html.parser")


for prop in soup.select(".srp-list__item"):
    print(prop.select_one("h3").text)
    print(prop.select(".listing-item__text")[0].text)
    print(prop.select(".listing-item__text")[1].text)
    print(prop.select(".listing-item__text")[2].text)
    print(prop.select(".listing-item__text")[3].text)
    print('#'*120)
