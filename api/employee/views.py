import xlrd
from app import db
from common.blueprint import Blueprint
from common.utils.json_utils import query_list_to_dict
from common.utils.number_utils import random_n_digit
from api.organization.models import Organization
from common import strings
from common.connection import add_item, update_item, raw_select
from common.response import success, failure
from flask import request

from api.employee.models import User

emp_api = Blueprint('emp', __name__, url_postfix='emp')
@emp_api.route('/addemp', methods=['POST'])
def add_user():
    try:
        payload=request.files['file']
        filename=request.files['file'].filename
        company_code=request.headers['company_code']
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        count = 0
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
                    employee=User(emp_id=emp_id,first_name=first_name,last_name=last_name,role=role,
                                  team=team,domain=domain,detail_designation=detail_designation,type=type,
                                  contract=contract,phone_no=phone_no,status =status,company_id=company_code)
                    if not add_item(employee):
                        return failure("provide valid employee details")
        return success("employee details added successfully")
    except Exception as err:
        return failure(str(err))


