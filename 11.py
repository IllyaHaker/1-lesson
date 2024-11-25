import requests

responce = requests.get("https://coinmarketcap.com/")

# coin_list = []
# responce_text = responce.text.split("<span>")
# for elem in responce_text:
#     if elem.startswith("$"):
#         for elem2 in elem.split("</span>"):
#             if elem2.startswith("$"):
#                 coin_list.append(float(elem2.replace("$", "").replace(",", "")))
#
# print("BTC -", coin_list[0])

from bs4 import BeautifulSoup
soup = BeautifulSoup(responce.text, features='html.parser')
soup_list = str(soup.find("div", {"class", "sc-b3fc6b7-0"}).find_all("span")[0]).split("$")[1].split("</span>")[0]
print(soup_list)
