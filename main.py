from events.payments.payment_created_event import payment_created
from events.trade.trade_executed_event import trade_executed
from events.iot.temperature_recorded_event import temperature_recorded



print("\n===== PAYMENT EVENT =====")
print(payment_created.model_dump_json(indent=2))

print("\n===== TRADE EVENT =====")
print(trade_executed.model_dump_json(indent=2))

print("\n===== TEMPERATURE EVENT =====")
print(temperature_recorded.model_dump_json(indent=2)) 