
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from FACEBOOK.Base_test.locator_signup import *


def test_first():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    driver.find_element(By.XPATH, facebook_page).click()
    sleep(2)

    fname_fieled = driver.find_element(By.XPATH, fname_locater)
    fname_fieled.clear()
    fname_fieled.send_keys("wasse")

    lname_fieled = driver.find_element(By.XPATH, lname_locater)
    lname_fieled.clear()
    lname_fieled.send_keys("Adisu")
    sleep(2)

    email_fieled = driver.find_element(By.XPATH, email_locater)
    email_fieled.clear()
    email_fieled.send_keys("samadis2112@gmail.com")
    sleep(2)

    email_fieled = driver.find_element(By.NAME, "reg_email_confirmation__")
    email_fieled.clear()
    email_fieled.send_keys("samadis2112@gmail.com")
    sleep(2)

    pasword_fieled = driver.find_element(By.XPATH, pasword_locater)
    pasword_fieled.clear()
    pasword_fieled.send_keys("3213213")
    sleep(2)

    driver.find_element(By.ID, "month").send_keys("octo")
    sleep(2)
    driver.find_element(By.ID, "day").send_keys("10")
    sleep(2)
    driver.find_element(By.ID, "year").send_keys("1987")
    sleep(2)
    driver.find_element(By.NAME, "sex").click()
    sleep(2)
    driver.find_element(By.XPATH, signin).click()
    sleep(10)