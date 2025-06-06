from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database.database import Base

class Batch(Base):
    __tablename__ = 'batches'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    tickets = relationship('Ticket', back_populates='batch')

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True)
    guid = Column(String, unique=True, index=True)
    customer_id = Column(Integer, index=True)
    status = Column(String, default='new')
    batch_id = Column(Integer, ForeignKey('batches.id'))

    batch = relationship('Batch', back_populates='tickets')

class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True, index=True)
    ticket_guid = Column(String, index=True)
    action = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
