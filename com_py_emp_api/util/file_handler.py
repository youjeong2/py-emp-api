# csv파일을 dframe 으로 넣고 
#  파이썬 타입의 object를  json 문자열로 변경(json인코딩) 

import os
import pandas as pd
import xlrd
import googlemaps
import json

from dataclasses import dataclass
@dataclass
class FileReader: 
        # def __init__(self, context, fname, train, test, id, label):
    #     self._context = context  # _ 1ea default access, _ 2ea private access

    # 3.7부터 간소화되서 dataclass 데코 후, key: value 형식으로 써도 됨 (롬복 형식)
        context : str = ''
        fname : str = ''
        train : object = None
        test : object = None
        id : str = ''
        label : str = ''

        def_newfile(self) -> str:
            return os.path.join(self.context, self.fname)

        def csv_to_dframe(self, header, usecols) -> object:
            return pd.read_csv(self.new_file(), enxcoding='UTF-8', thousands=',')

        def xls_to_dframe(self, header, usecols) -> object:
            print(f'PANDAS VERSION: {pd.__version__}')
            return pd.read_excel(self.new_file(), header = header, usecols= usecols)

         def create_gmaps(self):
             return googlemaps.Client(key='')

        def json_load(self):
            return json.load(open(self.new_file(), encoding = 'UTF-8')
