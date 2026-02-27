# src/main.py

import json
from fetch_products import fetch_products
from transform_products import transform_products
from save_products import save_products
import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log", mode="a"),
        logging.StreamHandler()
    ],
    force=True  # 🔥 THIS IS THE KEY LINE
)


def main():
    # Step 1: Fetch raw data
    raw_products = fetch_products()

    if not raw_products:
        print("No data fetched. Pipeline stopped.")
        return

    # Step 2: Save raw data
    with open("data/raw/products_raw.json", "w") as f:
        json.dump(raw_products, f, indent=2)

    # Step 3: Transform data
    clean_df = transform_products(raw_products)

    # Step 4: Save clean data
    save_products(clean_df)


if __name__ == "__main__":
    main()
