from fastapi import FastAPI
from events.base_event import BaseEvent
from events.payments.payment_created_event import payment_created
from events.trade.trade_executed_event import trade_executed
from events.iot.temperature_recorded_event import temperature_recorded
from models.ingestion_response import IngestionResponse
from models.ingestion_status import IngestionStatus

app = FastAPI()

@app.post("/api/v1/events", response_model=IngestionResponse)
def postEvent(e : BaseEvent):
    print(e)
    return IngestionResponse(
        message="Event received",
        event_id=e.event_id,
        event_type=e.event_type,
        ingestion_status=IngestionStatus.RECEIVED
    )