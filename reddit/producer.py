import pika
import json

def publish_stock(stocks_found):
    # Sends the found stocks to the queue  
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='scraped_data')

    channel.basic_publish(exchange='', routing_key='scraped_data', body=json.dumps(stocks_found))
    #print(stocks_found)
    print(" [x] Sent Stock Data to Queue")
    connection.close()
    return