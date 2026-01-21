"""
1. Добавление комметария
2. Получение всех комментов опреленного поста
3. Получение всех комментов
4. Получение всех комментов полльзователя
5. Изменения коммента
6. уделение коммента

"""


from database import get_db
from database.models import Comment
from schemas import CommentSchema


def add_comment_db(comment: CommentSchema):
    db = next(get_db())
    comment_data = comment.model_dump()
    comment = Comment(**comment_data)
    db.add(comment)
    db.commit()
    return True


def get_all_comments_exact_post_db(pid):
    db = next(get_db())
    comments = db.query(Comment).filter_by(Comment.pid == pid).all()
    if comments:
        return comments
    return False


def get_all_comments_db():
    db = next(get_db())
    all_comments = db.query(Comment).all()
    return all_comments


def get_all_comments_exact_user_db(uid):
    db = next(get_db())
    comments = db.query(Comment).filter_by(Comment.uid == uid).all()
    if comments:
        return comments
    return False


def get_exact_comment_db(cid):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(Comment.id == cid).first()
    if exact_comment:
        return exact_comment
    return False


def delete_comment_db(cid):
    db = next(get_db())
    exact_comment = get_exact_comment_db(cid)
    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return True
    return False


def edit_comment_db(cid: int, new_text: str):
    db = next(get_db())
    comment = db.query(Comment).filter_by(Comment.id == cid).first()
    if comment:
        comment.text = new_text
        db.commit()
        return comment
    return False