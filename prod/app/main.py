from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.producer.router import router as producer_router
from app.config.settings import settings

def create_app():
    app = FastAPI(
                    title=settings.app_name, 
                    version=settings.app_version
                )
    
    return app

# init app
app = create_app()
app.include_router(producer_router)

@app.get('/')
def app_index():
    return {"server": "I'm alive"}

@app.get('/ping')
def ping():
    return {"message": "pong"}


