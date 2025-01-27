import pika

def get_rabbitmq_connection():
    # Establece la conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declara la cola 'ventas_a_productos'
    channel.queue_declare(queue='update_stock', durable=True)

    print("Cola 'update_stoc' creada exitosamente.")
    return connection, channel
