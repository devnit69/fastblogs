# from sqlalchemy import Column, String, Boolean, DateTime, UUID, ForeignKey
# from sqlalchemy.sql import func
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# from src.db.database import Base

# class Blog(Base):
#     __tablename__ = "blogs"

#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     content = Column(String, unique=True, nullable=False)
#     user_id = Column(UUID(), ForeignKey('users.id'))
