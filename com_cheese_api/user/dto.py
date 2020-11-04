from com_py_emp_api.ext.db import db
# dto => file_handler=> service => dao
class UserDto(db.Model):
    __tablename__ = 'uers'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    userid : str = db.Column(db.String(10), primary_key = True, index = True)
    password : str = db.Column(db.String(1)) # 왜 String(1)?
    name : str = db.Column(db.String(100))
    pclass : int = db.Column(db.Integer)
    gender : int = db.Column(db.Integer)
    age_group : int = db.Column(db.Integer)
    embarked : int = db.Column(db.Integer)
    rank : int = db.Column(db.Integer)

    def __init__(self, userid, password, name, pclass, gender, age_group, embarked, rank):
        self.uerid = userid
        self.password = password
        self.name = name
        self.pclass = pclass
        self.gender = gender
        self.age_group = age_group
        self.embarked = embarked
        self.rank = rank

    def __repr__(self):
        return f'User(id={self.id}, userid={self.userid},\
            password={self.password}, name={self.name}, pclass={self.pclass}, gender={self.gender},\
                age_group={self.age_group}, embarked={self.embarked}, rank={self.rank}'

    @property # search!!!!!
    def json(self):
        return {
            'userid' : self.userid,
            'password' : self.password,
            'name' : self.name,
            'pclass' : self.pclass,
            'gender' : self.gender,
            'age_group' : self.age_group,
            'embarked' : self.embarked,
            'rank' : self.rank
        }

class UserVo:
    userid: str = ''
    password: str = ''
    name : str = ''
    pclass : int = 0
    gender : int = 0
    age_group : int = 0
    embarked : int = 0
    rank  : int = 0


