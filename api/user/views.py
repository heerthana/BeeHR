from app import db
from common.blueprint import Blueprint
from common.utils.json_utils import query_list_to_dict
from common.utils.number_utils import random_n_digit
from api.user.models import User, Address
from common import strings
from common.connection import add_item, update_item, raw_select
from common.response import success, failure
from flask import request

user_api = Blueprint('user', __name__, url_postfix='user')


@user_api.route('/signUp', methods=['POST'])
def signUp():
    try:
        form = request.get_json()
        phone_no = form["contact"]
        import uuid
        uid = uuid.uuid1()
        uid = uid.hex
        u = User(phone_no=phone_no,uuid=uid)
        db.session.add(u)
        db.session.commit()
        return success('Added','Done')
    except Exception as err:
        return failure(err)


@user_api.route('/verifyOtp', methods=['POST'])
def verifyOTP():
    try:
        form = request.get_json()
        phone_no=form["contact"]
        otp = form["OTP"]
        user = User.query.filter_by(phone_no=phone_no,otp=otp)
        query = "SELECT * from userdata WHERE phone_no = " + str(phone_no) + " AND otp = " + str(otp)
        result = raw_select(query)
        if len(result) > 0:
            return success('SUCCESS',result[0])
        return failure('Not a registered user')
    except Exception as err:
        return failure('Oops, Something went wrong please try again.')


@user_api.route('/addAddress', methods=['POST'])
def addAddress():
    try:
        form = request.get_json()
        uuid = form['uuid']
        address = form["address"]
        landmark = form["landmark"]
        save_as = form["save_as"]
        addressObj = Address()
        addressObj.uuid = uuid
        addressObj.address = address
        addressObj.landmark = landmark
        addressObj.save_as = save_as
        if not add_item(addressObj):
            return failure("Oops, Something went wrong.")
        else:
            return success("Address added Successfully")
    except Exception as err:
        return failure("Failed to add Address")


@user_api.route('/getAddresses', methods=['POST'])
def getAddresses():
    try:
        payload = request.get_json()
        uuid = payload['uuid']
        # result=Address.query.filter_by(uuid=uuid).all()
        query = "select address,landmark,save_as from address where uuid = '" + str(uuid) + "'"
        result=raw_select(query)
        if result is not None:
            # result=query_list_to_dict(result)
            return success('Success',result)
        return failure('No Address found for this user.')
    except Exception as err:
        return failure('Not a valid request')