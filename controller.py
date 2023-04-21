import openai
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TescoController:
    def __init__(self, openai_api_key, tesco_email, tesco_password):
        openai.api_key = openai_api_key
        self.tesco_email = tesco_email
        self.tesco_password = tesco_password
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)