from typing import List
from flask import request
from sqlalchemy import func
from sqlalchemy import and_, or_
from flask import Response, jsonify
from flask_restful import Resource, reqparse
from sklearn.ensemble import RandomForestClassifier 


# from com_cheese_api.ext.db import db, openSession
# from com_cheese_api.ext.db import db
from com_cheese_api.util.file import FileReader
from pathlib import Path
import pandas as pd
import numpy as np
import json
import os
import sys

class CheeseDf():
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/data')
        self.odf = None

    def new_model(self, payload):
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{this.data}')
        print(f'this.fname.')
        return pd.read_csv(Path(this.data, this.fname))
        
    def cheese_create(self):
        this = self.fileReader
        cheese_origin = 'cheese_list.csv' 
        cheese = 'cheese_data.csv'    
        # this.user_origin = self.new_model(user_origin) #payload
        this.cheese_origin = self.new_model(cheese_origin)
        this.cheese = self.new_model(cheese)
        # print(this.cheese_origin)
        # print(this.cheese)

        print(this)

        @staticmethod
        def df_category() :
                df = cheese_data = pd.read_csv('data/cheese_data.csv', encoding = 'utf-8')
                cheese_data = df.drop(cheese_data.columns[[0]], axis='columns')
                category_map = {
                        '모짜렐라' : 0,
                        '블루치즈' : 1,
                        '리코타' : 2,
                        '체다' : 3 ,
                        '파르미지아노 레지아노' : 4,
                        '고다' : 5,
                        '까망베르' : 6,
                        '브리' : 7,
                        '만체고' : 8,
                        '에멘탈' : 9,
                        '부라타' : 10
                }
                cheese_data['category'] = cheese_data['category'].map(category_map)
                print(cheese_data)
                return this

if __name__ == '__main__':
    c = CheeseDf()
    c.df_category()
    