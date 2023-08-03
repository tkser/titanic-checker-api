import uvicorn
from fastapi import FastAPI

from api.judge import judge_csv
from api.data import df_initialize

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await df_initialize()

@app.get("/")
async def index():
    return {"message": "Hello, Titanic!"}

@app.post("/judge")
async def judge(csv_data: str):
    return await judge_csv(csv_data)

def main():
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
