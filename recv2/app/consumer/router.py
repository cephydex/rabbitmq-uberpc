from fastapi import APIRouter
from fastapi import Depends
from app.config.broker import get_connection

router = APIRouter(
            prefix="/producer",
            tags=["/producer"]
        )


@router.get("/")
def index():
    return {
                "message": "Producers live here"
            }

@router.get("/hello")
def index(conn = Depends(get_connection)):
    channel = conn.channel()
    channel.queue_declare(queue="hello")

    channel.basic_publish(exchange='',
                          routing_key="hello",
                          body="Hello world")
    return {
                "message": "Producers live here"
            }