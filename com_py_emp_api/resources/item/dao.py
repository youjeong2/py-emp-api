from com_emp_api.ext.db import db, openSession
from com_emp_api.item.service import ItemService
from com_emp_api.item.dto import ItemDto
import pandas as pd
import json

class ItemDao(ItemDto):
    
    @classmethod
    def find_all(cls):
        sql = cls.query.all()

    @classmethod
    def find_by_itemid(cls, itemid) :
        return cls.query.file_by(itemid == itemid).all()

      @classmethod
     def find_by_brand(cls, brand) :
         return cls.query.firter_by(brand == brand).all()         
        
     @classmethod
     def find_by_name(cls, name) :
         return cls.query.firter_by(name == name).all()              

    @classmethod
    def find_by_price(cls, price) :
        return cls.query.file_by(price == price).first()
        
     @classmethod
     def find_by_texture(cls, texture) :
         return cls.query.firter_by(texture == texture).first()  

    @classmethod
    def find_by_taste(cls, taste) :
        return cls.query.file_by(taste == taste).first()
        
     @classmethod
     def find_by_matching(cls, matching) :
         return cls.query.firter_by(matching == matching).first()             

      @classmethod
     def find_by_content(cls, content) :
         return cls.query.firter_by(content == content).first()           