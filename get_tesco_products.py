import requests
import time
from bs4 import BeautifulSoup
import csv

# Function to get product details from a single page
def get_product_details(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4533815647682074101 t1691318593685825474 ath1fb31b7a altpriv cvcv=2 smf=0 svfu=1'})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    product_list = soup.find('ul', class_='product-list grid')
    products = []

    try:
        find_all = product_list.find_all('li', class_='product-list--list-item')
    except:
        print('Error getting product details')
        return products

    for li in find_all:
        try:
            title = li.find('h3', class_='styles__H3-oa5soe-0 bCKNNq').find('span').text
            url = li.find('a', class_='styled__Anchor-sc-1xbujuz-0 csVOnh beans-link__anchor')['href']
            price = li.find('p', class_='styled__StyledHeading-sc-119w3hf-2 jWPEtj styled__Text-sc-8qlq5b-1 lnaeiZ beans-price__text').text
            print(f'Found product: {title}')
            products.append([title, url, price])
        except:
            print(f'Error getting product details for {title}')

    print(f'@@ Total found: {len(products)} @@')
    return products

# Function to save product details in a CSV file
def save_to_csv(product_details, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'url', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for detail in product_details:
            writer.writerow({'title': detail[0], 'url': detail[1], 'price': detail[2]})

# Main script
base_url = 'https://www.tesco.ie/groceries/en-IE/shop'
categories = ['fresh-food', 'bakery', 'food-cupboard', 'frozen-food', 'health-and-beauty', 'household']
all_product_details = []

for category in categories:
    for i in range(1, 51): # Assuming a maximum of 100 pages per category, you can adjust this value
        url = f'{base_url}/{category}/all?page={i}&count=48'
        print(f'===== Getting product details from {url} =====')
        product_details = get_product_details(url)
        if product_details:
            # Append the product details to the all_product_details list
            all_product_details.extend(product_details)
            save_to_csv(all_product_details, 'data/tesco_groceries.csv')
        else:
            break

        if i % 25 == 0:
            time.sleep(10)
        else:
            time.sleep(3)

# Save all product details to a CSV file if you want
save_to_csv(all_product_details, 'data/tesco_groceries.csv')