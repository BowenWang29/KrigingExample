# KrigingExample

A demo of using Frost-Server and Kafka to generate air temperature sensor data streaming, which is then processed with Kriging algorithm.
The example has four stages:
1. *RawData*
2. *Frost-Server*
3. *Kafka*
4. *KrigingResult*

This Repo mainly concerns *RawData* which is stored as Parquet, interfaces between stages: ParquetToFrostServer(1.<pre>*</pre>), FrostServerToKafka(2.<pre>*</pre>), KafkaToKafka(3.<pre>*</pre>) which utilizes KafkaStreaming to concatenate any number of Kafka Cluster and KrigingClient(4.<pre>*</pre>).
