import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ecomm.settings")

import django
django.setup()

from django.core.management import call_command
from django.core.files import File
from bs4 import BeautifulSoup
from pathlib import Path
from product.models import Category, Product
import requests
import time



class GetData:
    def __init__(self):
        self.categories = Category.objects.all()
        self.home = Path.cwd() / 'static' / 'images' / 'products'
        if not Path.exists(self.home):
            Path.mkdir(self.home)
        self.main()

    def get_page(self, url, file):
        res = requests.get(url)
        page = BeautifulSoup(res.content, 'html.parser')
        div = page.find_all('div', {'class': 'KZmu8e'})[:3]
        for key, product in enumerate(div):
            filename = file
            img = product.find('img')   
            title = product.find('div', {'class': 'sh-np__product-title'})
            price = product.find('span', {'class': 'T14wmb'})
            img = requests.get(img['src'])
            filename += f"{key}.jpg"
            with open(self.home / filename, 'wb') as f:
                for chunk in img.iter_content(1024):
                    f.write(chunk)

    def main(self):
        for cat in self.categories:
            url = f"https://www.google.com/search?q={cat.name.replace(' ', '+')}&source=lnms&tbm=shop&sa=X&ved=2ahUKEwiu6_CU3JTyAhVxzTgGHafJCQIQ_AUoAnoECAIQBA&biw=1422&bih=1014"
            title, img, price = self.get_page(url, cat.name)
            p = Product(
                    name=title.text,
                    description=title.text,
                    price=int(price.text[1:-3].replace(',', ''      )),
                    pic=str(self.home / filename),
                )
            p.pic.save(filename, File(open(self.home / filename, 'rb')))
            p.category = cat
            p.save()
            # break


if __name__ == '__main__':
    GetData()

