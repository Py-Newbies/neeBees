import utils
import logging


url = "https://www.doorsteps.com/search/77447"
soup = utils.get_soup(url)

apartments = soup.select(".srp-list__item")

for prop in apartments:
    logging.info(prop.select_one("h3").text)
    logging.info(prop.select(".listing-item__text")[0].text)
    logging.info(prop.select(".listing-item__text")[1].text)
    logging.info(" ".join(prop.select(".listing-item__text")[2].text.replace('\n', '').split()))
    logging.info(prop.select(".listing-item__text")[3].text)
    logging.info('#'*95)

# logging.getLogger().handlers[0].close()
logging.shutdown()