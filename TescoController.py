import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class TescoController:
    def __init__(self, tesco_auth_token,tesco_refresh_token):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tesco.ie/groceries/")
        self.driver.add_cookie({
            'name': 'OAuth.AccessToken',
            'value': tesco_auth_token})
        self.driver.add_cookie({
            'name': 'OAuth.RefreshToken',
            'value': tesco_refresh_token})
        self.driver.refresh()
    
    def add_to_basket(self, item_url, quantity):
        #navigate to item page
        page = f"https://www.tesco.ie{item_url}"
        print(f"navigating to item {page}")
        self.driver.get(page)
        try:
            self.driver.implicitly_wait(5)
            quantity_input = self.driver.find_element(By.CSS_SELECTOR, 'input[data-auto="product-input"]')
            self.driver.execute_script(f"arguments[0].value = '{quantity}';", quantity_input)
            add_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-auto="add-button"]')
            add_button.click()
        except Exception as e:
            print(e)
            self.driver.close()
            raise e
    
    def empty_basket(self):
        self.driver.get("https://www.tesco.ie/groceries/en-IE/trolley")
        try:
            empty_basket_link = self.driver.find_element(By.CSS_SELECTOR, 'a.trolley--empty-trolley-button[data-auto="full-trolley--empty-button"]')
            empty_basket_link.click()

            self.driver.implicitly_wait(5)

            confirm_empty_button = self.driver.find_element(By.CSS_SELECTOR, 'button.js-empty-trolley-yes.button.button-primary.small')
            confirm_empty_button.click()

            time.sleep(5)
        except Exception as e:
            print(e)
            self.driver.close()
            raise e