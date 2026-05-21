from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime, timezone

class EventMetadata(BaseModel):
    correlation_id:Optional[str] = None
    trace_id : Optional[str] = None
    headers : Dict[str, Any] = Field(default_factory=dict)
    version : str = "1.0"


class BaseEvent(BaseModel):
    event_id : UUID = Field(default_factory=uuid4)
    event_type : str
    source : str
    timestamp : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    payload: Dict[str, Any]
    metadata: EventMetadata = Field(default_factory=EventMetadata)
   

    @field_validator("source")
    @classmethod
    def validate_source(cls, v: str):
        if not v or not v.strip():
            raise ValueError("source cannot be empty")
        return v.strip()

    @field_validator("event_type")
    @classmethod
    def validate_event_type(cls, v: str):
        if not v or not v.strip():
            raise ValueError("event_type cannot be empty")
        return v.strip()

    @field_validator("payload")
    @classmethod
    def validate_payload(cls, v: Dict[str, Any]):
        if not v:
            raise ValueError("payload cannot be empty")
        return v
    

# An event envelope → metadata + payload together