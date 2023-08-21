from time import sleep
import traceback
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import os
from settings import DOWNLOAD_TORRENT_DIR


def get_webdriver_unix():
    options = Options()
    options.add_argument("--window-size=1366,768")
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/ 537.36(KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"
    )
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    driver.execute_cdp_cmd('Storage.clearDataForOrigin', {
        "origin": '*',
        "storageTypes": 'all',
    })
    return driver


def get_webdriver_nt():
    options = Options()
    options.add_argument("--window-size=1366,768")
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/ 537.36(KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36")
    prefs = {'download.default_directory': 'C:\\Users\\Admin\\PycharmProjects\\bot_fitgirl_repack_portfolio\\core\\static\\media'}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options)
    return driver