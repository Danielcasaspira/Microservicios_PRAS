 
import pika, json

params = pika.URLParameters('amqps://uajfymhk:xd3LzKittZpVEq9mwTG59GTGvkdZpWLL@baboon.rmq.cloudamqp.com/uajfymhk')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)