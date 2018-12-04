from graphene_sqlalchemy import SQLAlchemyObjectType
from model.department import (Department as DepartmentModel)
from model.employee import (Employee as EmployeeModel)   


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel

