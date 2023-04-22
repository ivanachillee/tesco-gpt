import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class TescoController:
    def __init__(self, tesco_auth_token):
        #openai.api_key = openai_api_key
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

        #navigate to the tesco groceries page
        self.driver.get("https://www.tesco.ie/groceries/")

        #logs in to your account using your auth token
        self.driver.add_cookie({
            'name': 'OAuth.AccessToken',
            'value': tesco_auth_token})

        #refresh the page to load the cookies
        self.driver.refresh()