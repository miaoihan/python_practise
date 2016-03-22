# -*- coding:utf-8 -*-
# # 导入
from sqlalchemy import Column, String, create_engine
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


# # 初始化数据库连接:
SQL_URL = 'mysql+pymysql://root:1234@localhost/pythondb'
engine = create_engine(SQL_URL, echo=True)
# declarative_base() 创建了一个 BaseModel 类，这个类的子类可以自动与一个表关联。
BaseModel = declarative_base()

#------------- 数据库表映射 ----------------

class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30)) # or Column(String(30))


class UserData(BaseModel):
    __tablename__ = 'usersData'
    id = Column(Integer, primary_key=True)
    name = Column(String(30)) 
    data = Column(String(30)) 


class haha(BaseModel):
    __tablename__ = 'haha'
    id = Column(Integer, primary_key=True)
    name = Column(String(30)) 
    data = Column(String(30)) 
#--------- 数据库表映射------ END ----------------


def init_db():
    BaseModel.metadata.create_all(engine)
def drop_db():
    BaseModel.metadata.drop_all(engine)

# 创建表
init_db()
