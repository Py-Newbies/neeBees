import logging
import requests
from bs4 import BeautifulSoup
import mysql.connector


def my_headers():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/81.0.4044.141 Safari/537.36'
    return {
        'User-Agent': user_agent,
        'Accept-Encoding': 'gzip, deflate', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive', 'Accept-Language': 'en-US,en;q=0.5', 'Cache-Control': 'no-cache', 'DNT': '1'}


def get_soup(url):
    src_name = url.split('.')[1]
    logging.basicConfig(filename=f"../logs/{src_name}.log", filemode='w',
                        format='%(asctime)s: %(message)s', level=logging.INFO)
    try:
        logging.info('trying to read localfile')
        with open(f"../localfiles/{src_name}.html", "rb") as f:
            html = f.read()
        logging.info(f"Local file is available {'#' * 18} \n")
    except FileNotFoundError:
        logging.info('we are making a HTTP request')
        data = requests.get(url, headers=my_headers())
        with open(f"../localfiles/{src_name}.html", 'wb') as f:
            f.write(data.content)
        html = data.text
        logging.info('file content written successfully \n')

    return BeautifulSoup(html, "html.parser")


def insert_to_db(vals):
    mydb = mysql.connector.connect(host="sql.freedb.tech",
                                   user="freedb_reddy_root",
                                   password="Y6xY3PUMW?5R36h",
                                   database="freedb_reddy_python")
    mycursor = mydb.cursor()
    sql = "insert into realestate(address,price,beds,baths,sqft,prop_type, written_by, inserted_dt) " \
          "values(%s ,%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, vals)
    mydb.commit()
    mydb.close()


def extract_number(value):
    return int("".join([i for i in value if i.isdigit()]))