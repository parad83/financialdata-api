from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re

def get_tv(name, statement):
    driver = webdriver.Chrome()
    
    # financials-income-statement
    URL = f'https://www.tradingview.com/symbols/{name}/financials-{statement}/'

    driver.get(URL)
    wait = WebDriverWait(driver, timeout=10)
    
    try:
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tv-main")))
    except Exception as e:
        print(e)

    page_source = driver.page_source

    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')

    statement = {}
    default_fp = ["Q4 2021", "Q1 2022", "Q2 2022", "Q3 2022", "Q4 2022", "Q1 2023", "Q2 2023", 'TTM']

    # fp = []
    # dates = soup.find('div', class_='container-OWKkVLyj').find('div', class_='values-OWKkVLyj').find_all('div', class_='container-OxVAcLqi')
    # for d in dates:
    #     fp.append(d.find('div', class_='value-OxVAcLqi').text)
        
    data = soup.find_all('div', class_='container-C9MdAMrq')
    for row in data:
        title_div = row.find('div', class_='titleWrap-C9MdAMrq').find('div', class_='titleColumn-C9MdAMrq').find('span', class_='title-C9MdAMrq')
        statement[title_div.text] = {}
        value_row = row.find('div', class_='values-C9MdAMrq')
        row_values = value_row.find_all('div', class_='container-OxVAcLqi')
        for count, v in enumerate(row_values):
            row_value = v.find('div', class_='value-OxVAcLqi')
            statement[title_div.text][default_fp[count]] = row_value.text.strip()

    return({
        "content": statement, 
        "status_code": 200
    })
