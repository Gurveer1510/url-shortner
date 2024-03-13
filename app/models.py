from .database import Base
from sqlalchemy import String, Column


class Url(Base):
    __tablename__ = "url"

    original_url = Column(String, nullable=False)
    short_url = Column(String, primary_key=True, nullable=False)