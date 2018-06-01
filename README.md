# KrigingExample

A demo of using Frost-Server and Kafka to generate air temperature sensor data streaming, which is then processed with Kriging algorithm.
The example has four stages:
1. *RawData*: Air temperature data from Weather Underground
2. *Frost-Server*: An implementation of SensorThings API
3. *Kafka*: A message streaming system
4. *KrigingResult*: Visuallisation of Kriging Algorithum

This Repo mainly concerns:
* *RawData* which is stored as Parquet,

and implements interfaces between stages:
* ParquetToFrostServer(1.\*.ipynb)
* FrostServerToKafka(2.\*.ipynb)
* KafkaToKafka(3.\*.ipynb) which utilizes KafkaStreaming to concatenate any number of Kafka Cluster
* KrigingClient(4.\*.ipynb) which applies Kriging on Streaming data in parallel
