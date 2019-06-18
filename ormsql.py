# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,Boolean
Base=declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer,primary_key=True)
    title = Column(String(200),nullable=False)
    author = Column(String(200),)

engine=create_engine('mysql+pymysql://root:@localhost:3306/test?charset=utf8',echo=True)
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
  

class OrmTest(object):
    def __init__(self):
         self.session=Session()

    def add_one(self):
        new_obj = Book(
            title=u'liter_king',
            author=u'不晓得'
        ) 
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        return self.session.query(Book).get(1)

    def get_more(self):  
        return self.session.query(Book).filter_by(author=u'123')

    def update_onedata(self):
        new_obj=self.session.query(Book).get(1)
        print new_obj.title
        if new_obj:
            new_obj.title='111'
            self.session.add(new_obj)
            self.session.commit()
            return True
        return False  
    def update_moredata(self):
        data_list=self.session.query(Book).filter_by(author=u'赵勤')  
        for item in data_list:
            item.author = '123'
            self.session.add(item)
        self.session.commit()      

    def delete_one(self):
        new_obj=self.session.query(Book).get(2)  
        self.session.delete(new_obj)
        self.session.commit()


if __name__ == "__main__":
   
    use = OrmTest()
    user_list = use.get_more()
    for us in user_list:
        print us.title
  
  
