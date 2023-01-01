from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from FACEBOOK.Base_test.login_locater import *

def test_first():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    sleep(2)

    emal = driver.find_element(By.NAME, emal_path)
    emal.clear()
    emal.send_keys("samadis2112@gmail.com")
    sleep(2)

    password = driver.find_element(By.NAME, pw_path)
    password.clear()
    password.send_keys("9879879")
    sleep(2)

    login = driver.find_element(By.NAME, log_path).click()
    sleep(12)