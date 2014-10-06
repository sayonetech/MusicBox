#-----------------------------
# kafka_consumer.py
# David Bianco
# October 2014
#-----------------------------

from kafka import KafkaClient, SimpleConsumer
import musicbox

mb_env = musicbox.settings()

kafka = KafkaClient(mb_env['KAFKA_SERVER'])

consumer = SimpleConsumer(kafka, 'my-group', 'my-topic')

for message in consumer:
    print message

kafka.close()

