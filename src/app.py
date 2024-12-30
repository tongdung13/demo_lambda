from mangum import Mangum
from fastapi import FastAPI
from routes import demo, profile

app = FastAPI()
app.include_router(profile.router, prefix="/profile", tags=["Profile"])


@app.get("/")
async def read_root():
    return await demo.hello()


handler = Mangum(app)
