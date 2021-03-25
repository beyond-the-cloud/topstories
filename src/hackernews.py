import requests, json
from kafka import KafkaProducer
import logging
import sys

logger = logging.getLogger("topstories-logger")
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
ids = json.loads(response.text)
logger.info("got topstories ids from HackerNews")

producer = KafkaProducer(bootstrap_servers='kafka-0.kafka-headless.default.svc.cluster.local:9092')

for id in ids:
  producer.send('topstories', str(id).encode())
  logger.info("kafka producer sending story id: " + str(id))
  producer.flush()