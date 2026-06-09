from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)
from sqlalchemy.orm import relationship
from config.database import Base


class Client(Base):
    __tablename__ = "Clients"
    
    id = Column(
        "ClientId",
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        "ClientName",
        String(250),
        nullable=False
    )

    phone = Column(
        "ClientPhone",
        String(10),
        nullable=True
    )

    email = Column(
        "ClientEmail",
        String(100),
        nullable=True
    )

    rfc = Column(
        "ClientRfc",
        String(12),
        nullable=False,
        unique=True
    )

    active = Column(
        "ClientActive",
        Boolean,
        nullable=False
    )

    created_at = Column(
        "ClientCreatedAt",
        DateTime,
        nullable=False
    )

    updated_at = Column(
        "ClientUpdatedAt",
        DateTime,
        nullable=False
    )

    # Relation for FK
    locations = relationship(
        "Location",
        back_populates="client"
    )
    