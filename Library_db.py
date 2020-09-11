from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    phone = Column(String)
    e_mail = Column(String)


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Date)
    genre = Column(String)
    description = Column(String)


class Book_Resources(Base):
    __tablename__ = 'book_res'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    isbn_num = Column(Integer, nullable=False)
    rented = Column(Boolean, nullable=False)


rental = Table(
    "rental",
    Base.metadata,
    Column('book_id', Integer, ForeignKey("book_res.id")),
    Column('user_id', Integer, ForeignKey("user.id")),
    Column('rent_date', Date, nullable=False)
)



if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)