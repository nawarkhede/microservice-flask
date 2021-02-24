import pika

params = pika.URLParameters(
    "amqps://mhxyppjb:VwK96Emr2dpRfbmiPFcLNoVKecyQQy8o@lionfish.rmq.cloudamqp.com/mhxyppjb"
)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()


channel.queue_declare(queue="flaskadmin")


def callback(ch, method, properties, body):
    print("Recieved in flaskadmin")
    print(body)


channel.basic_consume(queue="flaskadmin", on_message_callback=callback)

print("started consuming")

channel.start_consuming()

connection.close()
