from sqlalchemy import Column, String, Boolean, DateTime, UUID, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.db.database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(String, unique=True, nullable=False)
    user_id = Column(UUID(), ForeignKey('users.id'))



class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    blog = relationship('Blog', backref='User')




