from enum import Enum

class IngestionStatus(str, Enum):
    RECEIVED  = "received"
    REJECTED  = "rejected"
    PROCESSING  = "processing"
    PROCESSED = "processed"
    FAILED  = "failed"