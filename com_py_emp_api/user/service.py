import os

from com_py_emp_api.util_file_handler import FileReader
import pands as pd
import numpy as mp
from skleran.ensemble import RandomForestClassfier 
from skleran.ensemble import DecisionTreeClassfier
from sklearn.naive_bayes import GaussianNB
from skleran.neighbors import KNneighborsClassifier 
from skleran.svm import SVC
from skleran.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection improt cross_val_score

from pathlib import path

# service는 전처리하는 곳
# hook = 아래의 순서대로 하겠다.
# 'userid' : this.train.PassengerId = train에 있는 Pclass를 가져와서 userid로 바꾼다
# odf 랑 df 를 따로 만들어서 axis =1 로 양옆으로 둘을 붙일 수 있게(concat) 함
# staticmethod는  self가 없음 create_train같은 함수를 가져다 쓸 수 있게함

class UserService:
    def__init__(self):
    self.fileReader = FileReader()

    self.odf = None

    def hook(self):
        train: = 'train.csv'
        test = 'text.csv'
        this = self.fileReader
        this = self.new_model(train)
        this = self.new_model(test)
        
        # Original Model Generaion

        self.odf = pd.DataFrame(

            {
                'userid' : this.train.PassengerId,
                'password' : '1',
                'name' : this.train.Name
            }

        )

        this.id = this.test['PassengerId']
        this = self.drop_feature(this, 'Cabin')
        this = self.drop_feature(this, 'Ticket')
        this = self.embarked_norminal(this)
        this = self.title_norminal(this)

        # The name is unnecessary because we extracted the Title from the name variable.

        this = self.drop_feature(this, 'Name')
        this = self.drop_feature(this, 'PassengerId')
        this = self.age_oridinal(this)
        this = self.drop_feature(this, 'SibSp')
        this = self.sex_norminal(this)
        this = self.fareBand_nominal(this)
        this = self.drop_feature(this, 'Fare')
        this.lable = self.create_label(this)
        this.train = self.create_train(this)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)

        df = pd.DataFrame(

            {
            'pclass': this.train.Pclass,
            'gender': this.train.Sex,
            'age_group': this.train.AgeGroup,
            'embarked' : this.train.Embarked,
            'rank' :  this.train.Title
            }
        )

        sumdf = pd.concat({self.odf, df}, axis=1)

        return sumdf

        def new_model(self, payload) -> object:
            this = self.fileReader
            this.data = self.data
            this.fname = payload
            print(f'{self.data}')
            print(f'{this.fname}')
            return pd.read_csv(Path(self.data, this.fname))

        @staticmethod
        def create_train(this) -> object:
            return this.train['Survied']

        @staticmethod
        def drop_feature(this, feature) -> object:
            this.train = this.train.drop([feature], axis = 1) 
            this.test = this.test.drop([feature], axis = 1) 
            return this         