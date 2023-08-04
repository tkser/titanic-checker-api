import pandas as pd
from sklearn.metrics import accuracy_score

from io import StringIO

import app.api as api

async def judge_csv(csv_data: str):
    try:
        data = StringIO(csv_data)
        df_pred = pd.read_csv(data)
        df = api.test_df.copy()

        if not isinstance(df_pred, pd.DataFrame):
            raise Exception("Invalid data type")

        if df.columns.tolist() != df_pred.columns.tolist():
            raise Exception("Invalid columns")
        
        if df.shape != df_pred.shape:
            raise Exception("Invalid shape")
        
        if df_pred.isnull().sum().sum() > 0:
            raise Exception("Invalid data")
        
        df = pd.merge(df, df_pred, on="PassengerId", how="inner", suffixes=("_true", "_pred"))

        if df["Survived_pred"].isnull().sum() > 0:
            raise Exception("Invalid data")

        score = accuracy_score(df["Survived_true"], df["Survived_pred"])

        return {
            "status": "success",
            "score": round(score, 5)
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "score": -1
        }
