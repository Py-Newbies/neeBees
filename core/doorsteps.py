import requests
from bs4 import BeautifulSoup
import utils
import logging


logging.basicConfig(filename="../logs/doorsteps.log", filemode='w',
                    format='%(asctime)s: %(message)s', level=logging.INFO)


url = "https://www.doorsteps.com/search/77447"

try:
    logging.info('trying to read localfile')
    with open("../localfiles/doorsteps.html") as f:
        html = f.read()
    logging.info(f"Local file is available {'#'*18} \n")
except FileNotFoundError:
    logging.info('we are making a HTTP request')
    data = requests.get(url, headers=utils.my_headers())
    with open("../localfiles/doorsteps.html", 'wb') as f:
        f.write(data.content)
    html = data.text
    logging.info('file content written successfully \n')


soup = BeautifulSoup(html, "html.parser")

for prop in soup.select(".srp-list__item"):
    logging.info(prop.select_one("h3").text)
    logging.info(prop.select(".listing-item__text")[0].text)
    logging.info(prop.select(".listing-item__text")[1].text)
    logging.info(" ".join(prop.select(".listing-item__text")[2].text.replace('\n', '').split()))
    logging.info(prop.select(".listing-item__text")[3].text)
    logging.info('#'*95)

# logging.getLogger().handlers[0].close()
logging.shutdown()