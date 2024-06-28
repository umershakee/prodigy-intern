import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce site (example: a page with a list of products)
url = 'https://example-ecommerce-site.com/products'

# Send a request to the website
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the webpage.")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract product information
products = []
for product in soup.find_all('div', class_='product-item'):
    name = product.find('h2', class_='product-title').text.strip()
    price = product.find('span', class_='product-price').text.strip()
    rating = product.find('span', class_='product-rating').text.strip() if product.find('span', class_='product-rating') else 'No rating'
    products.append([name, price, rating])

# Write the data to a CSV file
with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Rating'])
    writer.writerows(products)

print("Product information has been written to products.csv")
