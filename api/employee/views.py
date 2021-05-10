import xlrd
from flask import request

from api.employee.models import Employee
from common.blueprint import Blueprint
from common.connection import add_item
from common.response import success, failure
from werkzeug.utils import secure_filename

emp_api = Blueprint('emp', __name__, url_postfix='emp')


@emp_api.route('/addEmp', methods=['POST'])
def add_user():
    try:
        file=request.files['file']
        import os
        import xlwt
        import xlrd
        file_path ='/home/divum/learning_project/beehr/file/'
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(file_path,filename))
            name=file_path+filename
        book = xlrd.open_workbook(name)
        sheet = book.sheet_by_index(0)
        company_code = request.headers['company_code']
        count = 0
        for rx in range(0, sheet.nrows):
            if sheet.row(rx)[0].value != "":
                if count >0:
                    emp_id = str(sheet.row(rx)[0].value)
                    first_name = str(sheet.row(rx)[1].value)
                    last_name = str(sheet.row(rx)[2].value)
                    role = str(sheet.row(rx)[3].value)
                    team = str(sheet.row(rx)[4].value)
                    domain = str(sheet.row(rx)[5].value)
                    detail_designation = str(sheet.row(rx)[6].value)
                    type = str(sheet.row(rx)[7].value)
                    contract = str(sheet.row(rx)[8].value)
                    phone= str(sheet.row(rx)[9].value)
                    phone_no=phone.split(".")
                    status = str(sheet.row(rx)[10].value)
                    employee = Employee(emp_id=emp_id, first_name=first_name, last_name=last_name, role=role,
                                        team=team, domain=domain, detail_designation=detail_designation, type=type,
                                        contract=contract, phone_no=phone_no[0], status=status, company_id=company_code)
                    if not add_item(employee):
                        return failure("provide valid employee details")
            count=count+1
        return success("success","employee details added successfully")
    except Exception as err:
        return failure(str(err))
