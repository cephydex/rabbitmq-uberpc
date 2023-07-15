import pika
from app.config.settings import settings

RABBITMQ_HOST = settings.rabbitmq_host
RABBITMQ_USER = settings.rabbitmq_user
RABBITMQ_PASSWORD = settings.rabbitmq_password

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)

def get_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)
    )

    try:
        yield connection
    finally:
        connection.close()
