from fastapi import FastAPI
from middlewares.error_handler import ErrorHandler
from routes.password import password_router
from config.database import engine, Base
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Password Manager"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(password_router)

Base.metadata.create_all(bind=engine)

@app.get("/", tags=['home'])
def message():
    return HTMLResponse(content="<h1>FastAPI</h1>", status_code=200)