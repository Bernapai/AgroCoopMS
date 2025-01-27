from rabbitmq import get_rabbitmq_connection
from config.database import productos_collection
import json

def consume_messages():
    connection, channel = get_rabbitmq_connection()

    def callback(ch, method, properties, body):
        message = json.loads(body)
        producto_nombre = message["producto"]
        cantidad_vendida = message["cantidad"]
        
        # Actualizar el stock del producto
        producto = productos_collection.find_one({"nombre": producto_nombre})
        if producto:
            nuevo_stock = producto["stock"] - cantidad_vendida
            productos_collection.update_one(
                {"_id": producto["_id"]},
                {"$set": {"stock": nuevo_stock}}
            )
            print(f"Stock actualizado para {producto_nombre}: {nuevo_stock} unidades restantes.")
        else:
            print(f"Producto {producto_nombre} no encontrado.")

    # Consumir mensajes
    channel.basic_consume(
        queue='ventas_a_productos',
        on_message_callback=callback,
        auto_ack=True
    )

    print("Esperando mensajes...")
    channel.start_consuming()
