from selenium import webdriver

from selenium.webdriver.common.by import By

import random

import time

browser = webdriver.Firefox()

# You can change, with you want search motor but if you select Firefox you need geckodriver. geckodriver's github link : https://github.com/mozilla/geckodriver/releases

url = "https://eksisozluk2023.com/'what do you want to call'?p="

pageCount = 1

entries = []

entryCount = 1

while pageCount <= 10:
    randomPage = random.randint(1,92)
    newUrl = url + str(randomPage)
    browser.get(newUrl)

    elements = browser.find_elements(By.CSS_SELECTOR,".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

with open("entries.txt","w",encoding = "UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("*****************************************\n")
        entryCount += 1
        

browser.close()
