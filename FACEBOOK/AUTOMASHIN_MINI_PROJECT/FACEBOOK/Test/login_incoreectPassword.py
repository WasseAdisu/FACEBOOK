from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from FACEBOOK.Base_test.login_incorrect_locater import *

def test_first():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    sleep(2)

    emal_correct = driver.find_element(By.NAME, email_incorrectXpath)
    emal_correct.clear()
    emal_correct.send_keys("samadis2112@gmail.com")
    sleep(2)

    password_incorrect = driver.find_element(By.NAME, incorrect_pwXpath)
    password_incorrect.clear()
    password_incorrect.send_keys("321321") #3
    sleep(2)

    login_button = driver.find_element(By.NAME, incorrect_pwXpath).click()
    sleep(2)

    # error_message = driver.find_element(By.XPATH, "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348042").text
    # assert  "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]" == error_message
