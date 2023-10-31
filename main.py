import requests
from bs4 import BeautifulSoup

def load_links():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
    return lines

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    price = soup.find('p', class_='product-price__big product-price__big-color-red').text
    price = price.replace('₴', ' грн.')

    title = soup.find('h1', class_='product__title-left product__title-collapsed ng-star-inserted').text
    print(price, title)


if __name__ == '__main__':
    links = load_links()
    for i in links:
        get_data(i.strip())

    i = input('press any key to exit')
