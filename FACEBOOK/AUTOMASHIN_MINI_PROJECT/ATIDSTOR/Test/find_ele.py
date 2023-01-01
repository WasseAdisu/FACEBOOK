
from selenium import webdriver
from time import sleep
import pytest

NAV = '//nav[1]/div[1]/ul[1]'
NAV_IL = 'li'
PRODUCT = '//main[1]/div[1]/ul[1]/li[1]/'


def find():
    driver = webdriver.Chrome()
    driver.get("https://atid.store")
    driver.maximize_window()
find()


from time import sleep
from selenium.webdriver.common.by import By
from ATIDSTOR.BestTest.user_selected_materialPath import *
import pytest

men_store = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
men_page ="//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[9]/div[1]/a[1]/img[1]"
men_addcart = "//button[contains(text(),'Add to cart')]"
men_jacke_name ="//h1[contains(text(),'Black Hoodie')]"
def test_first():
    driver = webdriver.Chrome()
    driver.get("https://atid.store")
    driver.maximize_window()
    driver.find_element(By.XPATH, men_store).click()
    sleep(2)
    hoodie = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[5]/div[1]/a[1]/img[1]")
    hod = hoodie.find_elements(By.TAG_NAME, "h2")
    for h in hod:
        if h.text == "ATID Green Tshirt":
            h.click()

    sleep(4)

    driver.find_element(By.XPATH, men_addcart).click()
    sleep(2)
    prduct_name = driver.find_element(By.XPATH, men_jacke_name).text
    assert "Black Hoodie" == prduct_name