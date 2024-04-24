import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    res = {}
    p_id = []

    for row in products.itertuples():
        if row.low_fats == 'Y' and row.recyclable == 'Y':
            p_id.append(row.product_id)

    res['product_id'] = p_id

    return pd.DataFrame(res)