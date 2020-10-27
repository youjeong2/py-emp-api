from flask_restful import Resource
from flask import Response, jsonify
from com_py_emp_api.ext.db import db

class ItemDto(db.Model):
    __tablename__='items'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    id : int = db.Column(db.Integer, primary_key=True, index=True)
    name : str = db.Column(db.String(30))
    price : str = db.Column(db.String(30))
    types : str = db.Column(db.String(30))
    texture : str = db.Column(db.String(30))
    taste : str = db.Column(db.String(30))
    matching : str = db.Column(db.String(30))
    content : str = db. Column(db.String(30))

    dairy = db.relationship('DiaryDto', lazy='dynamic')

    def __init__(self, id, name, price, types, texture, taste, matching, content) : 
        self.id = id
        self.name = name
        self.price = price
        self.types = types
        self.texture = texture
        self.taste = taste
        self.matching = matching
        self.content = content

    def __repr__(self):
        return f'Item(id={self.id}, name={self.name}, price={self.price}, types={self.types}, texture={self.texture}, taste={self.taste}, matching={self.matching}, content={self.content})'

    @property
    def json(self):
        return {'id':self.id, 'name':self.name, 'price':self.price, 'types':self.types, 'texture':self.types, 'taste':self.types, 'matching':self.types, 'content':self.content}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()   


class ItemVo():
    ...

class ItemDao(ItemDto):
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name == name).all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id == id).first()


class Item(Resource):
    ...

class Items(Resource):
    ...    