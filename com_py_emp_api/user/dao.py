from com_py_emp_api.ext.db import db, openSession
from com_py_emp_api.user.service import UserService
from com_py_emp_api.user.dto import UerDto
import pandas as pd
import json

class UserDao(UserDto):
    
    @classmethod
    def find_all(cls):
        sql = cls.query
        df pd.read_sql(sql.statement, sql.session.bind)
        return json.loads(df.to_json(orient='records')

    @classmethod
    def find_by_name(cls, name)
        return cls.query.file_by(name == name).all()
        
     @classmethod 
     def find_by_id(cls, userid):
         return cls.query.firter_by(userid == userid).first()

     @classmehod
     def login(cls, user):
         sql = cls.query\
             .filter(cls.userid.like(user.userid))\
             .filter(cls.password.like(user.password))\
        df = pd.read_sql(sql.statement, sql.session.bind)
        print('=========================') 
        print(json.loads(df.to_json(orient='records')))     
        return json.loads(df.to_json(orient='records'))                     

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def insert_many():
        service  = UserService()
        Sessioin = openSession()
        session = Session()
        df = service.hook()
        print(df.head())
        session.bulk_insert_mappings(UserDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def modify_user(user):
        db.session.add(user)
        db.session.commit()

    @ classmethod 
    def delete__user(cls, id)
        data = cls.query.get(id)
        db.session.delete(data)
        db.session.commit()      