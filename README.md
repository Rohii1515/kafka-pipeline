# confluent-kafka-Pipline 
![pipeline](https://github.com/Rohii1515/kafka-sensor-pipeline/assets/101645749/db5bf214-0ac1-47e9-a44f-0ce664205cf3)

this repo help us to know how to publish and consume data to end from kafka confluent in json format.

![download](https://user-images.githubusercontent.com/34875169/169837256-b5cce5b4-0b10-4a5b-82b7-926f10690437.png)
***
# High Level Architecture 🪢📈
![image](assets/high-level.png)
***
How to setup confluent Kafka.
1. [Account Setup](Confluent%20Account.md)
2. [Cluster Setup](ConfluentClusterSetup.md)
3. [Kafka Topic](Confluent%20Topic%20Creation.md)
4. [Obtain secrets](Kafka%20key%20and%20secrets.md)
***
To use confluent kafka we need following details from Confluent dashboard.

```
confluentClusterName = ""
confluentBootstrapServers = ""
confluentTopicName = ""
confluentApiKey = ""
confluentSecret = ""
confluentSchemaApiKey = ""
confluentSchemaSecret = ""
endpoint = ""
```
***
## Tech Stack Used ![karate_chop](https://github.com/Rohii1515/kafka-sensor-pipeline/assets/101645749/20f15e4d-a46b-43d1-84b0-e68dfc4aeb14)

1. Python 
2. Bash
3. MongoDB
***
Step 1: Create a conda environment
```
conda --version
```

Step 2: Create a conda environment
```
conda create -p venv python==3.10 -y
```

step 3: 
```
conda activate venv/
```
Step 4:
```
pip install -r requirements.txt
```
