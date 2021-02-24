import pika

params = pika.URLParameters(
    "amqps://mhxyppjb:VwK96Emr2dpRfbmiPFcLNoVKecyQQy8o@lionfish.rmq.cloudamqp.com/mhxyppjb"
)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="admin", body="hello")
