from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class BatchBase(BaseModel):
    description: Optional[str] = None

class BatchCreate(BatchBase):
    pass

class BatchUpdate(BatchBase):
    pass

class Batch(BatchBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    customer_id: int
    status: Optional[str] = 'new'

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    status: Optional[str] = None

class Ticket(TicketBase):
    id: int
    guid: str
    batch_id: Optional[int] = None
    class Config:
        orm_mode = True

class History(BaseModel):
    id: int
    ticket_guid: str
    action: str
    timestamp: datetime
    class Config:
        orm_mode = True
