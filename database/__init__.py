from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Какой тип бд будем использовать(postgres, sqlite)
SQL_DATABASE = "sqlite:///sm69.db"

# Создаем бд
engine = create_engine(SQL_DATABASE)

# Подключаем сессии к бд
SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

