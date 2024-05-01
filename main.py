from requests import post
from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def forward(data: dict):
    res = post(url=data["URL"], data=data["DATA"], params=data["PARAMS"], headers=data["HEADERS"])
    return res.text

