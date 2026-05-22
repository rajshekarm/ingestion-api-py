from events.base_event import BaseEvent

temperature_recorded = BaseEvent(
    event_type="temperature.recorded",
    source="iot-sensor-network",
    payload={
        "sensor_id": "SENSOR-77",
        "temperature": 24.8,
        "unit": "Celsius",
        "location": "Warehouse-A"
    }
)