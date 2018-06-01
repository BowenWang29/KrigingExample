# KrigingExample

A demo of using Frost-Server and Kafka to generate air temperature sensor data streaming, which is then processed with Kriging algorithm. The goal is to demostrate a geodata processing use case on the infrastructure introduced in [SmartAirQuality Network Project](http://smartaq.net/).
There are four stages in the *KrigingEample*:
1. *RawData*: Observations of air temperature, humidity and precessure observed by private weather stations from [Weather Underground](https://www.wunderground.com/).
2. [*FROST-Server*](https://github.com/FraunhoferIOSB/FROST-Server): An implementation of [SensorThings API](http://www.opengeospatial.org/standards/sensorthings). Currently the FROST-Server only implements the first part of the API: Sensing and is maintained ragularly.
3. *Apache Kafka*: A message streaming system that acts as a persistance layer for storing and and retrieving data. All data analysis and data transformations should be carried on data outstreams from Kafka.
4. *KrigingResult*: The result of a demostration of data analysis using the infrastructure. It's produced with Kriging in Spark and visualized with [Folium](https://github.com/python-visualization/folium). The Kriging mention here refer to using GPR from sklearn http://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html in a parallel manner on Apache Spark

This Repo mainly concerns:
* *RawData* which is stored as Parquet,

and implements interfaces between stages:
* ParquetToFrostServer(1.\*.ipynb) loads parquet from local disk and posts observations via REST to the FROST-Server.
* FrostServerToKafka(2.\*.ipynb) obtains SensorThings objects(Things, DataStreams, Observations and so on) over MQTT and publishes them to the Kafka Cluster. Topics are organized the same entities SensorThings API and the messages are filled with corresponding informations in JSON.
* KafkaToKafka(3.\*.ipynb) utilizes KafkaStreaming to concatenate any number of Kafka Cluster. 
* KrigingClient(4.\*.ipynb) applies Kriging algorithm on the data obtained from Kafka in parallel. 
