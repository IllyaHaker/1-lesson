

import requests

responce = requests.get("https://bank.gov.ua/ua/markets/exchangerates")

from bs4 import BeautifulSoup
soup = BeautifulSoup(responce.text, features="html.parser")
soup_list = str(soup.find("td", {"data-label", "41,5035"}).find_all("span")[0]).split[1].split("</span>")[0]
#soup_list = soup.find_all("span", {"data-label", "Офіційний курс"})
print(soup_list)