from uuid import uuid4
from database.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    CHAR,
    DateTime,
    func,
    ForeignKey
)
from sqlalchemy.orm import (relationship, backref)
from .department import Department


class Employee(Base):
    __tablename__ = 'employee'
    uuid = Column(CHAR(36),
                  primary_key=True,
                  nullable=False,
                  default=lambda: str(
                      uuid4()
                  )
                  )
    Employee_id = Column("Employee_id", String, nullable=False)
    Employee_Name = Column("Employee_Name", String)
    Hired_On = Column("Hired_On", DateTime, default=func.now())
    department_id = Column(String, 
                            ForeignKey('department.department_id',
                                        name='Department id'
                                        )
                             )
    department = relationship(
                 Department, 
                 backref=backref('employees',
                                 uselist=True,
                                 cascade='delete,all'))
