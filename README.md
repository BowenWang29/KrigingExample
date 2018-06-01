# KrigingExample

A demo of using Frost-Server and Kafka to generate air temperature sensor data streaming, which is then processed with Kriging algorithm.
There are four stages in the *KrigingEample*:
1. *RawData*: Air temperature data from Weather Underground
2. *Frost-Server*: An implementation of SensorThings API
3. *Kafka*: A message streaming system
4. *KrigingResult*: Visuallisation of Kriging algorithm

This Repo mainly concerns:
* *RawData* which is stored as Parquet,

and implements interfaces between stages:
* ParquetToFrostServer(1.\*.ipynb) loads parquet from local disk and posts observations via REST to the FROST-Server.
* FrostServerToKafka(2.\*.ipynb) obtains SensorThings objects(Things, DataStreams, Observations and so on) over MQTT and publishes them to the Kafka Cluster. Topics are organized the same entities SensorThings API and the messages are filled with corresponding informations in JSON.
* KafkaToKafka(3.\*.ipynb) utilizes KafkaStreaming to concatenate any number of Kafka Cluster. 
* KrigingClient(4.\*.ipynb) applies Kriging algorithm on the data obtained from Kafka in parallel.
