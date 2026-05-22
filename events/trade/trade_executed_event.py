from events.base_event import BaseEvent


trade_executed = BaseEvent(
    event_type="trade.executed",
    source="trading-engine",
    payload={
        "trade_id": "TRD-9001",
        "symbol": "AAPL",
        "quantity": 100,
        "price": 210.55
    }
)