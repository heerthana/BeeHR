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
        company_code=payload['display_name'][:5].upper()+'01'
        org = Organization(name=payload['name'], display_name=payload['display_name'],
                           default_password=payload['default_password'],
                           address=payload['address'], state=payload['state'], city=payload['city'],
                           pincode=payload['pincode'], email=payload['email'], company_code=company_code)
        if add_item(org) is None:
            return failure("Oops, Something went wrong.")
        else:
            return success("Address added Successfully", {'company_code':company_code})
    except Exception as err:
        return failure(str(err))
