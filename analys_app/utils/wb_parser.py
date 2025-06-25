import logging

from analys_app.utils.selenium_manager import pars_pages
from analys_app.models import Product, ProductCategory

WB_URL = 'https://www.wildberries.ru/catalog/0/search.aspx?search='

def wb_category_parser(category_name, pages):
    url = WB_URL + category_name
    pars_data = pars_pages(url, pages=pages)
    for product in pars_data:
        try:
            if not ProductCategory.objects.filter(category_name=category_name).exists():
                category = ProductCategory(category_name=category_name)
                category.save()
            else:
                category = ProductCategory.objects.get(category_name=category_name)
            try:
                product_info = {
                    'product_name': product.split('/')[1] if len(product.split('/')) > 1 else product,
                    'product_price': float(pars_data.get(product)[2][0]) if float(pars_data.get(product)[2][0])!= 'от' else float(''.join(pars_data.get(product)[2][1:3])),
                    'product_discount_price':float(pars_data.get(product)[2][0]) if float(pars_data.get(product)[2][0])!= 'от' else float(''.join(pars_data.get(product)[2][3:])),
                    'product_rate': pars_data.get(product)[0],
                    'category': category,
                    'review_count': pars_data.get(product)[1],
                }
            except Exception as e:
                logging.exception(f'Error! {e}')
            product_instance = Product(**product_info)

            product_instance.save()
        except IndexError as e:
            logging.exception(f'Error! {e}')

