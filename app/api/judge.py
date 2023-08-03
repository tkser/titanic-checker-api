import pandas as pd
from sklearn.metrics import accuracy_score

from io import StringIO

from app.api.data import test_df

async def judge_csv(csv_data: str):
    try:
        data = StringIO(csv_data)
        df = pd.read_csv(data)

        if not isinstance(df, pd.DataFrame):
            raise Exception("Invalid data type")

        if df.columns.tolist() != test_df.columns.tolist():
            raise Exception("Invalid columns")
        
        if df.shape != test_df.shape:
            raise Exception("Invalid shape")
        
        if df.isnull().sum().sum() > 0:
            raise Exception("Invalid data")
        
        y_true = test_df["target"]
        y_pred = df["target"]

        score = accuracy_score(y_true, y_pred)

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
