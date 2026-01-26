from database.models import User
from database import get_db
from schemas import UserSchema

def get_all_or_exact_user(uid=0):
    db = next(get_db())
    if uid:
        exact_user = db.query(User).filter_by(id=uid).first()
        if exact_user:
            return exact_user
        return False
    all_users = db.query(User).all()
    return all_users


def get_user_by_username_db(username):
    db = next(get_db())
    user = db.query(User).filter_by(username=username).first()
    if user:
        return user
    return False


def create_user_db(user: UserSchema):
    db = next(get_db())
    user_data = user.model_dump()
    new_user = User(**user_data)
    if get_all_or_exact_user(new_user.id):
        return False
    db.add(new_user)
    db.commit()
    return True



def delete_user_db(uid):
    db = next(get_db())
    user_to_delete = get_all_or_exact_user(uid)
    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()
        return True
    return False


def update_user_db(uid, change_data, new_data):
    db = next(get_db())
    exact_user = get_all_or_exact_user(uid)
    if exact_user:
        if change_data == "name":
            exact_user.name = new_data
        elif change_data == "surname":
            exact_user.surname = new_data
        elif change_data == "phone_number":
            exact_user.phone_number = new_data
        elif change_data == "email":
            exact_user.email = new_data
        elif change_data == "password":
            exact_user.password = new_data
        elif change_data == "username":
            exact_user.username = new_data
        elif change_data == "city":
            exact_user.city = new_data
        elif change_data == "birthday":
            exact_user.date_of_birth = new_data
        else:
            return False
        db.commit()
        return True
    return False