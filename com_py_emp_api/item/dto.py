from com_py_emp_api.ext.db import db
from flask import Response, jsonify
from flask_restful import Resource, reqparse
import json

class ItemDto(db.Model):
    __tablename__='items'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    itemid : int = db.Column(db.Integer, primary_key=True, index=True)
    name : str = db.Column(db.String(30))
    price : str = db.Column(db.String(30))
    types : str = db.Column(db.String(30))
    texture : str = db.Column(db.String(30))
    taste : str = db.Column(db.String(30))
    matching : str = db.Column(db.String(30))
    content : str = db. Column(db.String(30))

    #dairy = db.relationship('DiaryDto', lazy='dynamic')
    orders = db.relationship('OrderDto', back_populates='item', lazy='dynamic')
    prices = db.relationship('PriceDto', back_populates='item', lazy='dynamic')

    def __init__(self, itemid, name, price, types, texture, taste, matching, content) : 
        self.id = itemid
        self.name = name
        self.price = price
        self.types = types
        self.texture = texture
        self.taste = taste
        self.matching = matching
        self.content = content

    def __repr__(self):
        return f'Item(itemid={self.itemid}, name={self.name}, price={self.price}, types={self.types}, texture={self.texture}, taste={self.taste}, matching={self.matching}, content={self.content})'

    @property
    def json(self):
        return {'itemid':self.itemid, 'name':self.name, 'price':self.price, 'types':self.types, 'texture':self.types, 'taste':self.types, 'matching':self.types, 'content':self.content}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()   