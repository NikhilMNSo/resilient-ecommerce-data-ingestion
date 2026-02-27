# src/save_products.py

import os
import pandas as pd


def save_products(df, output_dir="data/processed"):
    """
    Save cleaned product data to CSV and JSON.

    Args:
        df (pandas.DataFrame): Cleaned product data
        output_dir (str): Directory to save files
    """

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    csv_path = os.path.join(output_dir, "products_clean.csv")
    json_path = os.path.join(output_dir, "products_clean.json")

    # Save to CSV
    df.to_csv(csv_path, index=False)

    # Save to JSON
    df.to_json(json_path, orient="records", indent=2)

    print(f"Saved CSV to {csv_path}")
    print(f"Saved JSON to {json_path}")
