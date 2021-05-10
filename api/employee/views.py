import xlrd
from flask import request

<<<<<<< HEAD
from api.employee.models import User
from xlsxwriter import workbook
=======
from api.employee.models import Employee
from common.blueprint import Blueprint
from common.connection import add_item
from common.response import success, failure
>>>>>>> 3abaa36a8970ccba5812770932285f8ad4d26198

emp_api = Blueprint('emp', __name__, url_postfix='emp')


@emp_api.route('/addEmp', methods=['POST'])
def add_user():
    try:
        import os
        import openpyxl
        payload=request.files['file']
        filename=request.files['file'].filename
        wb = openpyxl.Workbook()
        file_path = 'home/divum/learning_project/file'
        name=wb.save(os.path.join(file_path,filename))
        book = xlrd.open_workbook(name)
        sheet = book.sheet_by_index(0)
        count = 0
        company_code = request.headers['company_code']
        for rx in range(0, sheet.nrows):
            if count > 0:
                if sheet.row(rx)[0].value != "":
                    emp_id = str(sheet.row(rx)[0].value)
                    first_name = str(sheet.row(rx)[1].value)
                    last_name = str(sheet.row(rx)[2].value)
                    role = str(sheet.row(rx)[3].value)
                    team = str(sheet.row(rx)[4].value)
                    domain = str(sheet.row(rx)[5].value)
                    detail_designation = str(sheet.row(rx)[6].value)
                    type = str(sheet.row(rx)[7].value)
                    contract = str(sheet.row(rx)[8].value)
                    phone_no = str(sheet.row(rx)[9].value)
                    status = str(sheet.row(rx)[10].value)
                    employee = Employee(emp_id=emp_id, first_name=first_name, last_name=last_name, role=role,
                                        team=team, domain=domain, detail_designation=detail_designation, type=type,
                                        contract=contract, phone_no=phone_no, status=status, company_id=company_code)
                    if not add_item(employee):
                        return failure("provide valid employee details")
        return success("employee details added successfully")
    except Exception as err:
        return failure(str(err))
