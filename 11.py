import requests

responce = requests.get("https://bank.gov.ua/ua/markets/exchangerates")

from bs4 import BeautifulSoup
soup = BeautifulSoup(responce.text, features="html.parser")
#soup_list = str(soup.find("div", {"class", "sc-b3fc6b7-0"}).find_all("span")[0]).split("$")[1].split("</span>")[0]
soup_list = soup.find_all("span", {"class", "sc-b3fc6b7-0"})
print(soup_list)