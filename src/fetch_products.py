# src/fetch_products.py

import requests
import logging
import time

logger = logging.getLogger(__name__)

API_URL = "https://fakestoreapi.com/products"

def fetch_products(retries=3, delay=2):
    attempt = 1

    while attempt <= retries:
        try:
            logger.info(f"Fetching products (Attempt {attempt})")
            response = requests.get(API_URL, timeout=10)
            response.raise_for_status()

            products = response.json()
            logger.info(f"Successfully fetched {len(products)} products")
            return products

        except requests.RequestException as e:
            logger.error(f"Error fetching products: {e}")
            time.sleep(delay)
            attempt += 1

    raise requests.RequestException("Failed to fetch products after retries")
