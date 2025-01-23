
# Kafka Cluster with FastAPI Integration

This repository provides a Kafka setup to act as a middle broker and a FastAPI application that publishes messages to Kafka topics and subscribes to topics to process data. A consumer service retrieves data from Kafka and inserts it into a database.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Consumer Workflow](#consumer-workflow)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

- Python 3.9 or later
- Docker and Docker Compose (for Kafka and FastAPI development)
- PostgreSQL or any compatible database
- Kafka
- `confluent-kafka` library

---

## Architecture

1. **Kafka Cluster**:
   - Acts as a middle broker for message exchange.
   - Manages topics for publishing and subscribing.

2. **FastAPI Application**:
   - Publishes messages to Kafka topics.
   - Subscribes to topics and processes incoming messages.

3. **Database Consumer**:
   - Listens to Kafka topics, processes messages, and inserts data into the database.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/kafka-fastapi-integration.git
cd kafka-fastapi-integration
```

### 2. Start Kafka and FastAPI Environment
Use the provided `docker-compose.yml` to start Kafka and FastAPI development environments:
```bash
docker-compose up -d
```

### 3. Set Up the Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Configuration

### Kafka Configuration
Edit the `config/kafka_config.json` file:
```json
{
  "bootstrap_servers": "localhost:9092",
  "topics": ["topic_name"],
  "group_id": "consumer_group"
}
```

### Database Configuration
Edit the `.env` file:
```dotenv
DATABASE_URL=postgresql://user:password@localhost:5432/your_database
```

---

## Usage

### 1. Start FastAPI Application
Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```

### 2. Start the Consumer Service
Run the consumer script:
```bash
python consumer.py
```

---

## API Endpoints

### Publish to Kafka
- **Endpoint**: `POST /publish/{topic}`
- **Description**: Publishes a message to the specified Kafka topic.
- **Request Body**:
  ```json
  {
    "key": "unique_key",
    "value": "message_payload"
  }
  ```

### Subscribe to Kafka Topic
- **Endpoint**: `POST /subscribe/{topic}`
- **Description**: Subscribes to a Kafka topic and processes incoming messages.

---

## Consumer Workflow

1. Listens to the specified Kafka topic.
2. Retrieves messages and transforms them if necessary.
3. Inserts the processed data into the database.

Sample consumer implementation:
```python
from confluent_kafka import Consumer
import json
import psycopg2

DATABASE_URL = "postgresql://user:password@localhost:5432/your_database"

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'consumer_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)

consumer.subscribe(['topic_name'])

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        data = json.loads(msg.value().decode('utf-8'))
        cursor.execute("INSERT INTO your_table (key, value) VALUES (%s, %s)", (data['key'], data['value']))
        connection.commit()

finally:
    consumer.close()
    connection.close()
```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

---

## License

This project is licensed under the Ausweg Info Controls Pvt Ltd License. See the `LICENSE` file for details.
