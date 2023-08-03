import os
import pandas as pd

import app.api as api

async def df_initialize():
    api.test_df = None
    data_path = os.path.join(os.path.dirname(__file__), "../../data/test_true.csv")
    api.test_df = pd.read_csv(data_path)
