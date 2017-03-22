__author__ = "Richard Johnston"
__copyright__ = "Copyright 2017, RJ Hobbies"
__credits__ = ["Richard Johnston"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Richard Johnston"
__email__ = "r.johnston085@gmail.com"
__status__ = "Development"

# Imports
import string
import requests
from bs4 import BeautifulSoup

# TODO - capture data from multiple cities
r = requests.get("https://www.domain.com.au/auction-results/canberra/")
soup = BeautifulSoup(r.content)

auction_data = soup.find_all("div", {"class": "auction-listings__wrap"})

auction_date = soup.find_all("h2", {"class": "sales-results-hero-content__heading"})[0].text
suburbs = auction_data[0].find_all("div", {"class" : "suburb-listings"})
for suburb in suburbs:
    suburb_data = suburb.find_all("h6", {"class" : "suburb-listings__heading"})
    suburb_str = suburb_data[0].text

    dwellings = suburb.find_all("a", {"class": "auction-details"})
    for dwelling in dwellings:
        dwe_address = dwelling.find_all("span", {"class" : "auction-details__address"})[0].text
        dwe_price = dwelling.find_all("span", {"class": "auction-details__price"})[0].text
        dwe_priceLb = dwelling.find_all("span", {"class": "auction-details__price-label"})[0].text
        dwe_bedroom = dwelling.find_all("span", {"class": "auction-details__bedroom"})[0].text
        dwe_propType = dwelling.find_all("span", {"class": "auction-details__property-type"})[0].text
        dwe_agent = dwelling.find_all("span", {"class": "auction-details__agent"})[0].text

        print(auction_date + "\t" + suburb_str + "\t" + dwe_address + "\t" + dwe_priceLb + "\t" + dwe_price + "\t" + dwe_bedroom + "\t" + dwe_propType + "\t" + dwe_agent)

        # TODO - Enter property web page to gather more data on the house

        dwe_address = ""
        dwe_price = ""
        dwe_priceLb = ""
        dwe_bedroom = ""
        dwe_propType = ""
        dwe_agent = ""
    suburb_str = ""
    # TODO - report tally of errors occuring from missing data when searching HTML - Potentially sort the patients HTML code

# TODO - read existing DB and check for repeating or missing data (CSV at first)

# TODO - Add data to csv

