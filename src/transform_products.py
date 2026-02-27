# src/transform_products.py

import pandas as pd

def transform_products(raw_products):
    """
    Clean and transform raw product data.

    Args:
        raw_products (list): Raw product data from API

    Returns:
        pandas.DataFrame: Cleaned product data
    """

    # Convert raw list of dicts to DataFrame
    df = pd.DataFrame(raw_products)

    # Rename columns
    df = df.rename(columns={
        "id": "product_id"
    })

    # Handle nested rating column
    if "rating" in df.columns:
        df["rating"] = df["rating"].apply(lambda x: x.get("rate") if isinstance(x, dict) else None)
        df["rating_count"] = df["rating"].apply(lambda x: None)

    # Alternative correct handling of rating
    df["rating"] = df["rating"].apply(lambda x: x.get("rate") if isinstance(x, dict) else x)
    df["rating_count"] = df["rating"].apply(lambda x: None)

    # Select only useful columns
    df = df[[
        "product_id",
        "title",
        "price",
        "category",
        "rating",
        "rating_count"
    ]]

    # Handle missing values
    df["rating"] = df["rating"].fillna(0)
    df["rating_count"] = df["rating_count"].fillna(0)

    return df
