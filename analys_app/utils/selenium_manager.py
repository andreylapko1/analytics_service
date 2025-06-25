from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium import webdriver
import logging
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import time

import undetected_chromedriver as uc

def pars_pages(url, pages=3):
    pars_data_dict = {}

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
    driver = uc.Chrome(options=options,
                       use_custom_patch=True)
    stealth(driver,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    try:
        for i in range(1, pages + 1):
            new_url = url + '&page=' + str(i)
            driver.get(new_url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.product-card__wrapper'))
            )

            product_cards = driver.find_elements(By.CSS_SELECTOR, '.product-card__wrapper')
            for card in product_cards:
                try:

                    price = card.find_element(By.CSS_SELECTOR, '.price__wrap')
                    product_brand = card.find_element(By.CSS_SELECTOR, '.product-card__brand-wrap')
                    product_rate_re_count = card.find_element(By.CSS_SELECTOR, '.product-card__rating-wrap')

                    product_rate_str = product_rate_re_count.text.replace(',','.').split('\n')
                    product_rate = float(product_rate_str[0]) if product_rate_str[0].replace('.', '').isdigit() else  0
                    if product_rate != 0:
                        reviews = (char for char in product_rate_str[1] if char.isdigit())
                        reviews = int(''.join(reviews))
                    else:
                        reviews = 0

                    price = price.text.replace('₽', '').replace('\n', ' ').split()
                    pars_data_dict[product_brand.text] = (product_rate, reviews, price)

                except WebDriverException  as e:
                    logging.warning(f'Web driver error: ', e)

        logging.info('Все элементы загружены и обработаны.')
    except WebDriverException as e:
        logging.warning(f'Web driver error: ', e)

    finally:
        driver.quit()

    return pars_data_dict