from fastapi import FastAPI
from events.base_event import BaseEvent
from events.payments.payment_created_event import payment_created
from events.trade.trade_executed_event import trade_executed
from events.iot.temperature_recorded_event import temperature_recorded


app = FastAPI()

@app.post("/api/v1/events")
def postEvent(e : BaseEvent):
    print(e)
    return {
  "message": "event received",
  "event_id": str(e.event_id),
  "event_type": e.event_type
}