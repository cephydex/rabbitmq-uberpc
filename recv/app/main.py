from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
# from app.consumer.router import router as consumer_router
from app.config.settings import settings
from app.config.broker import get_connection
from pika import BlockingConnection
from app.consumer.greetings_topic import process_greet_topics, process_hello_topics
from app.consumer.register_topic import process_register_topics, process_register_topics_extra

def create_app():
    app = FastAPI(title=settings.app_name, version=settings.app_version)
    
    # handle CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_credentials=True,
        allow_headers=["*"],
    )

    return app

# init app
app = create_app()
# app.include_router(consumer_router)

@app.get('/')
def app_index():
    return {"server": "I'm alive"}

@app.get('/ping')
def ping():
    return {"message": "pong"}

# def consume(conn: BlockingConnection = Depends(get_connection)):
def consume():
    conn: BlockingConnection = get_connection()
    channel = conn.channel()

    # declare queues
    channel.queue_declare(queue="hello")
    channel.queue_declare(queue="greet")
    channel.queue_declare(queue="register")

    # Handle message from hello queue topic
    channel.basic_consume(queue='hello',
                          on_message_callback=process_hello_topics,
                          auto_ack=True
                        )

    # Handle message from greet queue topic
    channel.basic_consume(queue='greet',
                          on_message_callback=process_greet_topics,
                          auto_ack=True
                        )
    
    # Handle message from register queue topic
    channel.basic_consume(queue='register',
                          on_message_callback=process_register_topics,
                          auto_ack=True
                        )
    
    # Handle message from register queue topic
    channel.basic_consume(queue='register',
                          on_message_callback=process_register_topics_extra,
                          auto_ack=True
                        )
    

    channel.start_consuming()


consume()


