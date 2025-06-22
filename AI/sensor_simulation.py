import json
import time
import random


# Simulate spaceship sensor data in real-time
def simulate_spaceship_sensor_data():
    # Generate random sensor data as an example
    sensor_data = {

        "engine_temperature": random.uniform(500, 1200),  # °C
        "fuel_pressure": random.uniform(30, 100),  # bar
        "thrust_output": random.uniform(100, 500),  # kN

        "oxygen_level": random.uniform(19, 21),  # %
        "co2_concentration": random.uniform(300, 1000),  # ppm
        "cabin_temperature": random.uniform(18, 30),  # °C

        "battery_voltage": random.uniform(20, 30),  # V
        "solar_panel_efficiency": random.uniform(50, 100),  # %

        "gyroscope_drift": random.uniform(0, 0.05),  # °/s
        "gps_signal_strength": random.uniform(-50, -20),  # dB

        "heat_shield_integrity": random.uniform(60, 100),  # %
        "external_temperature": random.uniform(-100, 150),  # °C

        "signal_strength": random.uniform(-40, -10),  # dB
        "latency": random.uniform(50, 1000),  # ms

        "hull_stress": random.uniform(10, 70),  # MPa
        "micro_meteoroid_impact": random.randint(0, 10)  # Count/min
    }
    
    return sensor_data

