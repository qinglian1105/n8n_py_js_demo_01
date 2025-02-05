"""
go_selenium.py

Python 3.10.16
Selenium 4.28.1
"""

import os
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


ETFS = ["0050", "00878", "0056", "00919", "00929", "006208", "00940", "00713"]
T_URL = "https://www.pocket.tw/etf/tw/{}/fundholding?page&parent&source="
XPH_NAME = '//*[@id="__layout"]/div/div/div[2]/main/div/div[1]/div/div/article/div[1]/div[1]/h1'
XPH_DATE = '//*[@id="__layout"]/div/div/div[2]/main/div/div[4]/section/div[3]'
XPH_TB = '//*[@id="__layout"]/div/div/div[2]/main/div/div[4]/section/div[2]/div/table/tbody/tr'
XPH_HOLDING = '//*[@id="__layout"]/div/div/div[2]/nav/div/div/div[2]/div[1]/div/div[4]/span/a'
PATH_DRIVER = "/usr/bin/chromedriver"
PATH_OUTPUT = "/data/files"


def create_driver():
    service = Service(executable_path=PATH_DRIVER)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def parse_table(driver):
    rows = len(driver.find_elements(By.XPATH, XPH_TB))
    cols = len(driver.find_elements(By.XPATH, f"{XPH_TB}[1]/td"))
    etf_holding = []
    for r in range(1, rows + 1):
        s_info = dict()
        for p in range(1, cols + 1):
            value = driver.find_element(By.XPATH, f"{XPH_TB}[{r}]/td[{p}]").text
            if p == 1:
                s_info["s_code"] = value
            elif p == 2:
                s_info["s_name"] = value
            elif p == 3:
                s_info["holding_percentage"] = (
                    float(value.replace("%", ""))
                    if len(value.replace("%", "")) > 1
                    else 0
                )
            elif p == 4:
                s_info["holding_amount"] = int(value.replace(",", ""))
            else:
                s_info["unit"] = value.replace(" ", "")
        etf_holding.append(s_info)
    return etf_holding


def scraping(etf_code):
    driver = create_driver()
    driver.get(T_URL.format(etf_code))
    time.sleep(1)
    holding_btn = driver.find_element(By.XPATH, XPH_HOLDING)
    holding_btn.click()
    time.sleep(1.5)
    ele_date = driver.find_element(By.XPATH, XPH_DATE)
    holding_date = ele_date.text.split("：")[1]
    ele_names = driver.find_element(By.XPATH, XPH_NAME)
    list_names = ele_names.text.split()
    etf_code = list_names[1]
    etf_name = list_names[0]
    etf = dict()
    etf["etf_code"] = etf_code
    etf["etf_name"] = etf_name
    etf["scraping_time"] = time.strftime("%Y-%m-%d %H:%M:%S")
    etf["etf_holding"] = parse_table(driver)
    driver.close()
    time.sleep(1)
    return [holding_date, etf]


def get_daily_efts():
    etfs = dict()
    etf_data = []
    for etf_code in ETFS:
        ds = scraping(etf_code)
        etf_data.append(ds[1])
    etfs["holding_date"] = ds[0].replace("/", "-")
    etfs["etf_data"] = etf_data
    return etfs


def main():
    try:
        daily_etfs = get_daily_efts()
        print(json.dumps(daily_etfs, ensure_ascii=False))
        file_name = os.path.basename(__file__).replace(".py", ".json")
        with open(f"{PATH_OUTPUT}/{file_name}", "w", encoding="utf-8") as fp:
            json.dump([daily_etfs], fp, ensure_ascii=False, indent=4)
    # For n8n
    except Exception as e:
        print("")


if __name__ == "__main__":
    main()
