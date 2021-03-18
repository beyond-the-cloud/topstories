import requests, json
from kafka import KafkaProducer

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
ids = json.loads(response.text)

producer = KafkaProducer(bootstrap_servers='kafka-0.kafka-headless.default.svc.cluster.local:9092')

for id in ids:
  print(id)
  producer.send('topstories', str(id).encode())
  producer.flush()