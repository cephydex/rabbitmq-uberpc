from fastapi import APIRouter
from fastapi import Depends
from app.config.broker import get_connection
from app.producer.schema import GreetMessage, DataMessage
import json

router = APIRouter(
            prefix="/producer",
            tags=["/producer"]
        )


@router.get("/")
def index():
    return {
                "message": "Producers live here"
            }

@router.post("/hello")
def index(msg: str, conn = Depends(get_connection)):
    channel = conn.channel()
    channel.queue_declare(queue="hello")

    channel.basic_publish(exchange='',
                          routing_key="hello",
                          body=msg)
    return {
                "success": True,
                "message": "message sent successfully",
                "data": msg,
            }

@router.post("/greet")
def greet(msg: GreetMessage, conn = Depends(get_connection)):
    channel = conn.channel()
    channel.queue_declare(queue="greet")

    channel.basic_publish(exchange='',
                          routing_key="greet",
                          body=msg.message)
    return {
                "success": True,
                "message": "message sent successfully",
                "data": dict(msg),
            }

@router.post("/register")
def register(data: DataMessage, conn = Depends(get_connection)):
    channel = conn.channel()
    channel.queue_declare(queue="register")
    success = False
    try:
        channel.basic_publish(exchange='',
                            routing_key="register",
                            body=json.dumps(data.dict()))
        success = True
    except Exception as ex:
        print('Error', str(ex))
    
    return {
                "success": success,
                "message": "message sent successfully",
                "data": dict(data),
            }