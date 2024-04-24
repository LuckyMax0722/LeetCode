import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    res = {}
    name = []
    customer = customer.fillna(0)
    for row in customer.itertuples():
        if row.referee_id != 2:
            name.append(row.name)
    res['name'] = name
    return pd.DataFrame(res)