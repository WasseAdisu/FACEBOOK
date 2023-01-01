from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from FACEBOOK.Base_test.forgetPassword_locater import *


def test_first():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    driver.find_element(By.XPATH, facebook_locater).click()
    sleep(2)

    email_fieled = driver.find_element(By.XPATH, email_locater)
    email_fieled.clear()
    email_fieled.send_keys("samadis2112@gmail.com")
    sleep(2)

    driver.find_element(By.XPATH, search_locater).click()
    sleep(2)

    driver.find_element(By.XPATH, contunue1_locater).click() # continue
    sleep(2)

    driver.find_element(By.XPATH, contunue2_locater).click()  # continue
    sleep(2)

    driver.find_element(By.XPATH, newPw_locater).click()  # new pw
    sleep(12)

    driver.find_element(By.XPATH, newPw_locater_button).click()  # new pw
    sleep(2)

    driver.find_element(By.XPATH, newPw_locater_choice).click()  # new pw
    sleep(12)