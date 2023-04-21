from decouple import config
import openai
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Read authentication variables
openai.api_key = config("OPENAI_API_KEY")
tesco_email = config("TESCO_IE_LOGIN_EMAIL")
tesco_password = config("TESCO_IE_LOGIN_PASSWORD")

def generate_grocery_list(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].text.strip()

# Function to parse the generated list
def parse_grocery_list(generated_text):
    # Parse the text and create a list of items
    items = generated_text.split("\n")
    return items

# Function to log in to Tesco.ie
def login_to_tesco(driver, email, password):
    # Navigate to the login page
    driver.get("https://www.tesco.ie/groceries/")

    # Find the login button and click it
    login_button = driver.find_element_by_xpath("//a[@title='Log in']")
    login_button.click()
    time.sleep(2)

    # Enter your email and password
    email_input = driver.find_element_by_id("username")
    email_input.send_keys(email)
    password_input = driver.find_element_by_id("password")
    password_input.send_keys(password)

    # Click the login button
    submit_button = driver.find_element_by_xpath("//button[@type='submit']")
    submit_button.click()
    time.sleep(2)

# Function to add items to cart
def add_items_to_cart(driver, items):
    for item in items:
        # Search for the item
        search_input = driver.find_element_by_id("search")
        search_input.clear()
        search_input.send_keys(item)
        search_input.send_keys(Keys.RETURN)

        # Click the "Add to cart" button for the first result
        try:
            add_to_cart_button = driver.find_element_by_xpath("//button[@title='Add to basket']")
            add_to_cart_button.click()
        except:
            print(f"Couldn't find item: {item}")
        time.sleep(2)

# Main function
def main():
    # Generate a grocery list
    prompt = "Generate a cost-effective grocery list"
    generated_list = generate_grocery_list(prompt)
    items = parse_grocery_list(generated_list)

    # Set up Selenium
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # Log in to Tesco.ie
    email = "your_email"
    password = "your_password"
    login_to_tesco(driver, email, password)

    # Add items to cart
    add_items_to_cart(driver, items)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
