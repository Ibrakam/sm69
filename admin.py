from sqladmin import ModelView
from database.models import User, UserPost


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email]
    column_searchable_list = [User.username, User.email]


class UserPostAdmin(ModelView, model=UserPost):
    column_list = [UserPost.id, UserPost.main_text]
    