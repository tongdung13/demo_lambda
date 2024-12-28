from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def hello():
    return {"hello": "world"}

@app.get("/hello/{name}")
async def hello_name(name: str):
    return {"hello": name}