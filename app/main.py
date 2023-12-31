import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.api.judge import judge_csv
from app.api.data import df_initialize

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

origins = [
    "http://localhost:3000",
    "https://titanic-checker.pages.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await df_initialize()

@app.get("/")
async def index():
    return {"message": "Hello, Titanic!"}

@app.post("/judge")
async def post_judge(file: bytes = File(...)):
    content = file.decode("utf-8")
    return await judge_csv(content)

def main():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
