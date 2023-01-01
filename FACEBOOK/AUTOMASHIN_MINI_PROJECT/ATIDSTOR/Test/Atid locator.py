from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from ATIDSTOR.BestTest.user_selected_materialPath import *
import pytest


def test_second():
    driver = webdriver.Chrome()
    driver.get("https://atid.store")
    driver.maximize_window()
    driver.find_element(By.XPATH, stores_shoes).click()
    sleep(2)
    driver.find_element(By.XPATH, stores_page).click()
    sleep(2)
    driver.find_element(By.XPATH, stores_add).click()
    sleep(2)
    prduct_name = driver.find_element(By.XPATH, shoes_name).text
    assert "ATID Black Shoes" == prduct_name

test_second()

def test_third():
    driver = webdriver.Chrome()
    driver.get("https://atid.store")
    driver.maximize_window()
    driver.find_element(By.XPATH, men_Tshirt).click()
    sleep(2)
    driver.find_element(By.XPATH, man_Tpath).click()
    sleep(2)
    driver.find_element(By.XPATH, addd).click()
    sleep(2)
    prduct_name = driver.find_element(By.XPATH, man_Tname).text
    assert "ATID Green Tshirt" == prduct_name

test_third()

def test_fourth():
    driver = webdriver.Chrome()
    driver.get("https://atid.store")
    driver.maximize_window()
    driver.find_element(By.XPATH, women_fation).click()
    sleep(2)
    driver.find_element(By.XPATH, women_fpage).click()
    sleep(2)
    driver.find_element(By.XPATH, women_fadd).click()
    sleep(2)
    prduct_name = driver.find_element(By.XPATH, women_fname).text
    assert "Blue Denim Shorts" == prduct_name
test_fourth()


def test_fifth():
    driver = webdriver.Chrome()
    driver.get("https://atid.store")
    driver.maximize_window()
    driver.find_element(By.XPATH, trouther).click()
    sleep(2)
    driver.find_element(By.XPATH, trouther_page).click()
    sleep(2)
    driver.find_element(By.XPATH, trouther_add).click()
    sleep(2)
    prduct_name = driver.find_element(By.XPATH, trouther_name).text
    assert "Dark Blue Denim Jeans" == prduct_name
test_fifth()

def test_six():
    driver = webdriver.Chrome()
    driver.get("https://atid.store")
    driver.maximize_window()
    driver.find_element(By.XPATH, accesory).click()
    sleep(2)
    driver.find_element(By.XPATH, accesory_page).click()
    sleep(2)
    driver.find_element(By.XPATH, accesory_add).click()
    sleep(2)
    prduct_name = driver.find_element(By.XPATH, accesory_name).text
    assert "Buddha Bracelet" == prduct_name
test_six()

def test_s():
    driver = webdriver.Chrome()
    driver.get("https://atid.store")
    driver.maximize_window()
    driver.find_element(By.XPATH, accesory).click()
    sleep(2)




