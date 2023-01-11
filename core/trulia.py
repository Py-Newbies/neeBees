import utils
import logging


url = "https://www.trulia.com/for_rent/77447_zip/"
soup = utils.get_soup(url)

apartments = soup.select(".SearchResultsList__WideCell-sc-14hv67h-2")

for prop in apartments:
    try:
        logging.info(prop.select_one(".enhvQK").text)
        logging.info(prop.select(".csrRqu")[0].text)
        logging.info(prop.select(".csrRqu")[1].text)
        logging.info(prop.select(".csrRqu")[2].text)
        logging.info(prop.select(".csrRqu")[3].text)
        logging.info('#'*95)
    except:
        pass
