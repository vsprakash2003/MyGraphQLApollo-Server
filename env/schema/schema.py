from os import path
import graphene
from model.department import Department as DepartmentModel
from .query_types import Department, Employee
from .mutations import AddDepartment, EditDepartment

import logging

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'myapplog.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)
logger = logging.getLogger()


class Query(graphene.ObjectType):
    all_departments = graphene.List(lambda: graphene.List(Department), 
                                    department_id=graphene.String(),
                                    offset=graphene.Int(),
                                    limit=graphene.Int(),
                                    sort_order=graphene.String(),
                                    sort_field=graphene.String())
    all_employees = graphene.List(Employee)
    department_by_id = graphene.Field(lambda: graphene.List(Department),
                                      department_id=graphene.String(),
                                      offset=graphene.Int(),
                                      limit=graphene.Int(),
                                      sort_order=graphene.String(),
                                      sort_field=graphene.String())

    def resolve_all_departments(self, info, department_id=None, offset=None,
                                limit=None, sort_order='asc',
                                sort_field='deptid'):
        logger.info("Inside all_departments resolver")
        query = Department.get_query(info)

        if sort_field and sort_order:
            if sort_field == 'deptid':
                if sort_order == 'asc':
                    query = query.order_by(DepartmentModel.department_id.asc())
                elif sort_order == 'desc':
                    query = query.order_by(DepartmentModel.department_id.desc()
                                           )

        if limit:
            query = query.limit(limit).offset((offset - 1) * limit)

        return query.all()

    def resolve_department_by_id(self, info, department_id=None, offset=None,
                                 limit=None, sort_order='asc',
                                 sort_field='deptid'):
        logger.info("Inside department_by_id resolver")
        query = Department.get_query(info)
        
        if department_id:
            query = query.filter_by(department_id=department_id)

        if sort_field and sort_order:
            if sort_field == 'deptid':
                if sort_order == 'asc':
                    query = query.order_by(DepartmentModel.department_id.asc())
                elif sort_order == 'desc':
                    query = query.order_by(DepartmentModel.department_id.desc()
                                           )

        if limit:
            query = query.limit(limit).offset((offset - 1) * limit)
        
        return query.all()

    def resolve_all_employees(self, info, Employee_id=None):
        query = Employee.get_query(info)
        if Employee_id:
            query = query.filter_by(uuid=Employee_id)
        return query.all()


class Mutation(graphene.ObjectType):
    logger.info("Inside mutation class of schema")
    add_dept = AddDepartment.Field()
    edit_dept = EditDepartment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
