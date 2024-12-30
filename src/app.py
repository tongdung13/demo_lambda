from mangum import Mangum
from fastapi import FastAPI
from routes import demo, profile

app = FastAPI()
app.include_router(demo.router, prefix="/demo", tags=["Demo"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])


handler = Mangum(app)