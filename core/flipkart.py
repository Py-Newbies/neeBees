import requests
from bs4 import BeautifulSoup
import utils

url = "https://www.flipkart.com/search?q=mobiles"
data = requests.get(url, headers=utils.my_headers())

# verification step
# file = open('flipkart.html', 'wb')
# file.write(data.content)
# file.close()

# soup generation
soup = BeautifulSoup(data.content, 'html.parser')

# data extraction
name = soup.select("._4rR01T")
price = soup.select("")