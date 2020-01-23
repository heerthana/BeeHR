from api.user.models import User


def get_user_by_id(_id):
    try:
        obj = User.query.get(_id)._asdict()
        return obj
    except Exception as err:
        print("get_user_by_id", str(err))
        return None
