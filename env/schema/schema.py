from os import path
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from .query_types import Department, Employee
from .mutations import AddDepartment
from logging.config import fileConfig
import logging

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'myapplog.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)
logger = logging.getLogger()


class Query(graphene.ObjectType):
    all_departments = graphene.List(Department)
    all_employees = graphene.List(Employee)
    department_by_id = graphene.Field(lambda: graphene.List(Department), 
                                      department_id=graphene.String())

    def resolve_all_departments(self, info):
        logger.info("Inside all_departments resolver")
        query = Department.get_query(info)
        return query.all()

    def resolve_department_by_id(self, info, department_id=None):
        logger.info("Inside department_by_id resolver")
        query = Department.get_query(info)
        if department_id:
            query = query.filter_by(department_id=department_id)
        return query.all()

    def resolve_all_employees(self, info, Employee_id=None):
        query = Employee.get_query(info)
        if Employee_id:
            query = query.filter_by(uuid=Employee_id)
        return query.all()


class Mutation(graphene.ObjectType):
    logger.info("Inside mutation class of schema")
    add_dept = AddDepartment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
