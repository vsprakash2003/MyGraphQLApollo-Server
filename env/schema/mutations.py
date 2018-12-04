from os import path
import graphene
from graphql import GraphQLError
from sqlalchemy.exc import SQLAlchemyError
from database.database import db_session
from model.department import (Department as DepartmentModel)
from .support_types import NewDeptInput
from .query_types import Department, Employee
import logging

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'myapplog.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)
logger = logging.getLogger()


class AddDepartment(graphene.Mutation):
    logging.info("Inside AddDepartment class of mutation") 

    class Arguments:
        dept_data = NewDeptInput(required=True)

    dept = graphene.Field(Department)

    @classmethod
    def mutate(cls, root, info, dept_data=None):
        logging.info(f"Inside mutate method of mutation and argument is {dept_data}")
        try:
            if dept_data:
                dept_helper = DeptHelper(db_session)
                new_dept = dept_helper.AddDepartment(dept_data) 
            logging.info(f"New department {new_dept} added")    
            db_session.commit()

        except SQLAlchemyError as e:
            raise GraphQLError(e)
        return cls(dept=new_dept)


class DeptHelper:
    db_session = None

    def __init__(self, db_session):
        self.db_session = db_session

    def AddDepartment(self, dept_data):
        logger.info("Inside AddDepartment method of mutation.py")
        new_dept = self.db_session.query(DepartmentModel).filter(
                (DepartmentModel.uuid == dept_data.get('id'))
            ).one_or_none()
        logger.info("query executed inside mutation")    
        if new_dept:
            raise GraphQLError('This department already exists.')

        new_dept = DepartmentModel(
            department_id=dept_data.get('departmentId'),
            department_name=dept_data.get('departmentName'),
        )
        
        try:
            logging.warning('enter')
            self.db_session.add(new_dept)
            logging.warning('exit')
        except Exception as error:
            logging.warning(error)
        logging.warning('fin')
        return new_dept
