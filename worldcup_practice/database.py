# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# 定义 Team 类
class Team(Base):

    __tablename__ = 'teams'

    team_id = Column('TeamId', Integer, primary_key=True)
    name = Column('Name', String)
    code = Column('Code', String)
    rank = Column("Rank", Integer)

    def __init__(self, id, name, code, rank):
        self.team_id =id
        self.name = name
        self.code = code
        self.rank = rank

    def __repr__(self):
        return "<Team(TeamId= '%d', name='%s', code='%s', rank='%d')>" % (self.team_id, self.name, self.code, self.rank)

# 初始化数据库的连接
engine = create_engine('sqlite:///world_cup.db')
Session = sessionmaker(bind=engine)
session = Session()

# 读取所有的 team 信息
teams = session.query(Team).all()
print(teams)

# 增加一个新的 team 进入数据库
italy = Team(43954, "Italy", "ITA", 19)
session.add(italy)
session.commit()
session.close()