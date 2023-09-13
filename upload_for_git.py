# importing selenium webdriver and time 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# data inputs from excel

skuName = []

managePageUrl = []

fileLocation = []

# variable decleration for while loop

i = 0

# chrome driver 

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# user credentials

uName = ""
uPwd = ""

# automation start / get webpage

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.get("")

# find user credential input elements on webpage

driver.find_element().click()

driver.find_element().send_keys(uName)

driver.find_element().send_keys(uPwd)

# time delay for recaptcha

time.sleep(20)

driver.send_keys(Keys.ENTER)

# execution loop

while i < len(skuName):
    
    # upload sequence

    driver.get(managePageUrl[i])
    
    driver.implicitly_wait(10)

    driver.find_element().click()
    
    driver.find_element().clear().send_keys(" " + skuName[i])
    
    driver.find_element().send_keys(fileLocation[i])

    time.sleep(15)
    
    driver.find_element().submit()

    i +=1

print("upload complete")

# driver.close()