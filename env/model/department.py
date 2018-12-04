from uuid import uuid4
from database.database import Base
from sqlalchemy import (
    Column,
    String,
    CHAR,
    Integer
)


class Department(Base):
    __tablename__ = 'department'
    uuid = Column(CHAR(36), primary_key=True,
                  nullable=False,
                  default=lambda: str(
                    uuid4()
                )
    )
    department_id = Column("department_id", String, unique=True)
    department_name = Column("department_name", String)
    