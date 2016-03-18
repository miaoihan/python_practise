# -*- coding:utf-8 -*-
# # 导入
from sqlalchemy import Column, String, create_engine
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


# # 初始化数据库连接:
SQL_URL = 'mysql+pymysql://root:1234@localhost/pythondb'
engine = create_engine(SQL_URL, echo=True)
# print('连接成功')
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)
# # session = DBSession()
# # new_user = Han(id='5', name='Bob')
# # session.add(new_user)
# # session.commit()
# # session.close()
# print('创建成功')


#------------- 数据库表映射 ----------------

class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30)) # or Column(String(30))

class UserData(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30)) 
    data = Column(String(30)) 
#--------- 数据库表映射------ END ----------------

BaseModel = declarative_base()
def init_db():
    BaseModel.metadata.create_all(engine)
def drop_db():
    BaseModel.metadata.drop_all(engine)

class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30)) # or Column(String(30))
init_db()
