from analys_app.utils.selenium_manager import pars_pages
from analys_app.models import Product

WB_URL = 'https://www.wildberries.ru/catalog/0/search.aspx?search='

def wb_category_parser(category_name, pages):
    url = WB_URL + category_name
    pars_data = pars_pages(url, pages=pages)
    for product in pars_data:
        try:
            product_info = {
                'product_name': product.split('/')[1] if len(product.split('/')) > 1 else product,
                'product_price': float(pars_data.get(product)[2][1]),
                'product_discount_price': float(pars_data.get(product)[2][0]),
                'product_rate': pars_data.get(product)[0],
                'review_count': pars_data.get(product)[1],
            }
            product_instance = Product(**product_info)
            product_instance.save()
        except IndexError:
            print(product.split('/'), 'EXCEPT!!!!!!!!!!!!!!!',
                  )

        # print(pars_data.get(product))
