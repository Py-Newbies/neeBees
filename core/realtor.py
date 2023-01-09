import utils
import logging


url = "https://www.realtor.com/apartments/77447"
soup = utils.get_soup(url)

apartments = soup.select(".BasePropertyCard_propertyCardWrap__pblQC")

for prop in apartments[:42]:
    logging.info(prop.select_one(".price-wrapper").text.strip())
    logging.info(prop.select('li')[0].text.strip())
    logging.info(prop.select('li')[1].text.strip())
    logging.info(prop.select('li')[2].select_one("span").text.strip())
    logging.info(" ".join(prop.select_one(".content-col-left").text.strip().split()))
    logging.info(prop.select_one(".message").text.strip())
    logging.info('#'*95)
