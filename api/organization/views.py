from flask import request

from api.organization.models import Organization
from common.blueprint import Blueprint
from common.connection import add_item
from common.response import success, failure

org_api = Blueprint('org', __name__, url_postfix='org')


@org_api.route('/addOrg', methods=['POST'])
def create_organization():
    try:
        payload = request.get_json()
        org = Organization(name=payload['name'], display_name=payload['display_name'],
                           efault_password=payload['default_password'],
                           address=payload['address'], state=payload['state'], city=payload['city'],
                           pincode=payload['pincode'], email=payload['email'])
        res = add_item(org)
        if res is None:
            return failure("Oops, Something went wrong.")
        else:
            return success("Address added Successfully", {'company_code': res.company_code})
    except Exception as err:
        return failure(str(err))
