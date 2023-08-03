import pandas as pd

test_df = None

async def df_initialize():
    global test_df
    test_df = pd.read_csv("../data/test.csv")
