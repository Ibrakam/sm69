"""
1. Добавления поста
2. получение всех постов пользователя(uid)
3. получение всех постов
4. получение определенного поста(pid)
5. изменение поста
6. удаление поста

"""

from database.models import UserPost, PostPhoto
from schemas import UserPostSchema, PhotoPostSchema
from database import get_db


def get_exact_post_db(pid):
    db = next(get_db())
    post = db.query(UserPost).filter_by(id = pid).first()
    if post:
        return post
    return False


def create_post_db(post: UserPostSchema):
    db = next(get_db())
    post_data = post.model_dump()
    new_post = UserPost(**post_data)
    db.add(new_post)
    db.commit()
    return True




def get_all_user_posts_db(uid):
    db = next(get_db())
    user_posts = db.query(UserPost).filter_by(uid = uid).all()
    if user_posts:
        return user_posts
    return False

def add_photo_post_db(photo: PhotoPostSchema):
    db = next(get_db())
    photo_data = photo.model_dump()
    exact_post = get_exact_post_db(photo_data.get("pid"))
    if exact_post:
        photo = PostPhoto(**photo_data)
        db.add(photo)
        db.commit()
        return True
    return False


def get_all_posts_db():
    db = next(get_db())
    posts = db.query(UserPost).all()
    return posts


def delete_post_db(pid):
    db = next(get_db())
    post_to_delete = get_exact_post_db(pid)
    if post_to_delete:
        db.delete(post_to_delete)
        db.commit()
        return True
    return False


def edit_post_db(pid, change_data, new_data):
    db = next(get_db())
    exact_post = get_exact_post_db(pid)
    if exact_post:
        if change_data == "text":
            exact_post.main_text = new_data
        # elif change_data == "photo":
        #     exact_post.photo_path = new_data
        else:
            return False
        db.commit()
        return True
    return False