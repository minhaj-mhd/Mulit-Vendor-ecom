from kafka import KafkaProducer
import json
from app.config import settings

producer = KafkaProducer(
    bootstrap_servers=[settings.KAFKA_BOOTSTRAP_SERVERS],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_event( topic: str, event: dict):
    producer.send(topic,event)
    producer.flush()