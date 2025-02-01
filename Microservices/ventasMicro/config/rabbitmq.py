import pika

def get_rabbitmq_connection():
    try:
        # Establece la conexión con RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        # Declara la cola 'update_stock' (con durable=True para asegurar la persistencia)
        channel.queue_declare(queue='update_stock', durable=True)

        print("Cola 'update_stock' creada exitosamente.")

        # Devuelve la conexión y el canal para que puedan ser usados en otras funciones
        return connection, channel

    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error al conectar con RabbitMQ: {e}")
        return None, None
