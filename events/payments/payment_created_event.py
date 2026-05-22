from events.base_event import BaseEvent


payment_created = BaseEvent(
    event_type="payment.created",
    source="banking-service",
    payload={
        "payment_id": "PAY-1001",
        "customer_id": "CUST-501",
        "amount": 2500.75,
        "currency": "USD"
    })