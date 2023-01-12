import utils
import logging
import datetime


url = "https://www.trulia.com/for_rent/77447_zip/"
soup = utils.get_soup(url)

apartments = soup.select(".SearchResultsList__WideCell-sc-14hv67h-2")

for prop in apartments:
    try:
        address = prop.select_one('[data-testid="property-address"]').text
        price = prop.select_one('[data-testid="property-price"]').text
        beds = prop.select_one('[data-testid="property-beds"]').text
        baths = prop.select_one('[data-testid="property-baths"]').text
        sqft = prop.select_one('[data-testid="property-floorSpace"]').text

        vals = (address, utils.extract_number(price), utils.extract_number(beds), utils.extract_number(baths),
                utils.extract_number(sqft), 'house', 'Reddy', datetime.date.today())

        for i in vals:
            logging.info(i)

        utils.insert_to_db(vals)
        logging.info("record inserted successfully")
    except:
        logging.error('some exception occurred while parsing the prop')
    logging.info("#" * 90)
