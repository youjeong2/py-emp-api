import numpy as np
import pandas as pd
from com_cheese_api.util.file import FileReader
from pathlib import Path
from com_cheese_api.ext.db import url, db
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from sqlalchemy.ext.declarative import declarative_base
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold  # k value is understood as count
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm

import os
import json

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
        this.cheese = self.new_model(cheese)
        # print(this.cheese_origin)
        # print(this.cheese)