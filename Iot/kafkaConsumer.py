from kafka import KafkaConsumer
import json

BROKER = "localhost:9092"
TOPIC = "spaceship_telemetry"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BROKER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print(f"Listening for telemetry data on topic: {TOPIC}")
"""
    telemetry_data = {
        "sensor_id": "temp_sensor_1",
        "temperature": round(random.uniform(-80, 100), 2),
        "pressure": round(random.uniform(0.1, 1.5), 2),
        "radiation_level": round(random.uniform(0.01, 0.5), 3),
        "timestamp": time.time()
    }
"""

for message in consumer:
    data = message.value

    data["sensor_id"]
    data["temperature"]
    data["pressure"]
    data["radiation_level"]
    data["timestamp"]

    print(f"Received: {data}")
