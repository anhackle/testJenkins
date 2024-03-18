#!/usr/bin/env python3

import sys, time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

class AlertModule():
    def __init__(self, url):
        self.url = url
        self.options = Options()
        self.options.add_argument('--headless=new')
        self.service = Service('/home/anle/bb/tools/search-engine/chromedriver')
    
    def check(self):
        driver = webdriver.Chrome(
            service = self.service,
            options = self.options
        )
        driver.get(self.url)
        try:
            element = WebDriverWait(driver, 2).until(
                    EC.alert_is_present()
            )
            print(f"{Color.GREEN}{Color.BOLD}{self.url}{Color.END}")
        except:
            return
def process(data):
    AlertModule(data).check()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for line in sys.stdin:
        executor.submit(process, line.rstrip())
