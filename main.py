import uvicorn
# from app.api import app

if __name__ == "__main__":
    uvicorn.run(app='app.api:app', host="127.0.0.1", port=8080, reload=True)