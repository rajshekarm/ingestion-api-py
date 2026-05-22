from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime, timezone
from models.ingestion_status import IngestionStatus

class IngestionResponse(BaseModel):
    message: str
    event_id: UUID
    event_type: str
    ingestion_status: IngestionStatus