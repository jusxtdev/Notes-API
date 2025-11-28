# Import statements
import uvicorn
from fastapi import FastAPI 
from routers import notes

app = FastAPI()

app.include_router(notes.router)

if __name__ == "__main__":
    uvicorn.run(app=app, host='127.0.0.1', port=8000)