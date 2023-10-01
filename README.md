# confluent-kafka-Pipline 
![pipeline](https://github.com/Rohii1515/kafka-sensor-pipeline/assets/101645749/db5bf214-0ac1-47e9-a44f-0ce664205cf3)

# Overview
This project is designed to demonstrate how to build a Confluent Kafka Pipeline that facilitates the collection, transformation, and storage of sensor data using Kafka and MongoDB. It provides a step-by-step guide on how to publish sensor data to Kafka topics, stream and transform the data using Confluent Kafka Streams, and finally, consume and store the data in a MongoDB database.

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
To consume confluent kafka data we need following details from MongoDB Atlas.
```
MONGO_DB_URL = "mongodb+srv://Rohii:<password>@cluster9.fgrr4ct5.mongodb.net/?retryWrites=true&w=majority"
```
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
step 5: 
```
Run producer_main.py to prdouce data from data source to topics in json
```

step 6:
```
Run consumer_main.py to consume data from Confluent Kafka to MongoDB in json format
```
#### Contributing
If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive messages.
- Push your branch to your fork.
- Create a pull request to merge your changes into the main branch of this repository.
#### License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.
