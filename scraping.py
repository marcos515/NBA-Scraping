import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from selenium.webdriver.common.by import By
import time

url = "https://stats.nba.com/players/traditional"
top10ranking = {}

rankings = {
    '3points': {'field': 'FG3M', 'label': '3PM'},
    'rebounds': {'field': 'REB', 'label': 'REB'},
    'steals': {'field': 'STL', 'label': 'STL'},
    'blocks': {'field': 'BLK', 'label': 'BLK'},
    'points': {'field': 'PTS', 'label': 'PTS'},
    'assistants': {'field': 'AST', 'label': 'AST'},
}


def getRankByType(type):
    field = rankings[type]['field']
    label = rankings[type]['label']

    driver.find_element_by_xpath(
        f"//div[@class='nba-stat-table__overflow']//table//thead//tr//th[@data-field='{field}']").click()

    element = driver.find_element_by_xpath(
        "//div[@class='nba-stat-table__overflow']//table")
    html_content = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    df_full = pd.read_html(str(table))[0].head(10)
    df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
    df.columns = ['pos', 'player', 'team', 'total']
    return df.to_dict('records')


driver = webdriver.Chrome("chrome_driver/chromedriver")
driver.get(url)

driver.implicitly_wait(10)

# wait for popup asking for cookies
time.sleep(3)

# Accept cookies.
driver.find_element(By.ID,"onetrust-accept-btn-handler").click()

for rank_type in rankings:
    top10ranking[rank_type] = getRankByType(rank_type)

driver.quit()


# Save into a file the result
data_file = open('result/data.json', 'w', encoding='utf-8')
data = json.dumps(top10ranking, indent=4)
data_file.write(data)