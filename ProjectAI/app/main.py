from fastapi import FastAPI
from app.routers import auth, chat, payments

app = FastAPI()

app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(payments.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the ChatGPT-like service"}

