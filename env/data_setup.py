from ast import literal_eval
from database import database
from model import employee, department
import logging
import sys
import json
import datetime

Logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                   format=
                        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def insertDepartmentDate():
    Logger.info('Inserting data into department table')
    try:
        with open('data/department.json', 'r') as json_data:
            records = literal_eval(json_data.read())
    except IOError as e:
        Logger.info('Exception while opening the department file. Error ({0}): {1}'. format(e.errno, e.strerrno))
    for record in records['Details']:
        departmentdata = department.Department(**record)
        database.db_session.add(departmentdata)
    database.db_session.commit()


def insertEmployeeDate():
    Logger.info('Inserting data into employee table')
    try:
        with open('data/employee.json', 'r') as json_data:
            records = literal_eval(json_data.read())
    except IOError as e:  
        Logger.info('Exception while opening the employee file. Error ({0}): {1}'. format(e.errno, e.strerrno))  
    for record in records['Details']:
        record['Hired_On'] = datetime.datetime.strptime(record['Hired_On'], '%Y-%m-%d %H:%M:%S') #convert string datetime to python datetime
        employeedata = employee.Employee(**record)
        database.db_session.add(employeedata)
    database.db_session.commit()


if(__name__) == '__main__':
    insertDepartmentDate()
    insertEmployeeDate()