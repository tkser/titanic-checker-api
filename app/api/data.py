import os
import pandas as pd

test_df = None

async def df_initialize():
    global test_df
    data_path = os.path.join(os.path.dirname(__file__), "../../data/test_true.csv")
    test_df = pd.read_csv(data_path)
