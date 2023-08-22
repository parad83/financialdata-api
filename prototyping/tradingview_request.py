import requests
from bs4 import BeautifulSoup

url = 'https://www.tradingview.com/symbols/NASDAQ-TSLA/financials-income-statement/'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
}

page = requests.get(url=url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser',  from_encoding='utf-8')


print(page.status_code)
# print(soup.prettify())

# soup.div

# data = soup.find('div', class_='container-Tv7LSjUz')
data = soup.find_all('div', class_="container-C9MdAMrq")
for row in data:
    # title_div = row.find('div', class_='titleWrap-C9MdAMrq').find('div', class_='titleColumn-C9MdAMrq').find('span', class_='title-C9MdAMrq')
    metric_name = row.get('data-name')
    print(metric_name)
    # print(title_div.text)
    # container-OxVAcLqi 
    row_value = row.find('div', class_='values-C9MdAMrq')
    col_values = row_value.find_all('div', class_='container-OxVAcLqi')
    for c in col_values:
        print(c)
        # row_value = c§.find('div', class_='value-OxVAcLqi')
        # print(row_value.text)
    print()
    
    
    
# data = soup.find_all('span', class_="title-C9MdAMrq")
# data = soup.find_all('div', class_="container-C9MdAMrq")
# values = data.find_all('div', class_="container-OxVAcLqi")


# for v in values:
    # print(v.text)

# for row in data:
    # title_div = row.find('div', class_='titleWrap-C9MdAMrq').find('div', class_='titleColumn-C9MdAMrq').find('span', class_='title-C9MdAMrq')
    # print(title_div)
    # print(title_div.text)


'''
divs of rows containing statements --> container-C9MdAMrq

TITLES:
bigger title div --> titleWrap-C9MdAMrq
title column --> titleColumn-C9MdAMrq
title div --> title-C9MdAMrq

'''
