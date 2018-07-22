#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import data_exporter as de
import model as md
from datetime import datetime
import sys

HELP_MSG = '''
    欢迎你来到小白看球, 你可以输入:
    1. help - 获取帮助信息
    2. ranking - 获取所有排名
    3. select {type} {num} - 获取第 N 位的排名信息 type = uncertainty / goal / fame
    4. ranking type {type} - 获取分类排名 type = uncertainty / goal / fame
    5. date {date} - 获取某一天值得推荐的, 默认是当天
    6. quit - 退出
'''

def help():
    print(HELP_MSG)

def key_word_handler(str):
    # print('输入 %s' %(str))
    str = str.strip()
    result_details = md.moding()
    if str == 'help':
        help()
    elif str == 'ranking':
        # 调用 ranking 的模块函数
        de.ranking_by_type(result_details)
    elif str.startswith('ranking type '):
        ty = str.split(' ')[2]
        print("type %s" %ty)
        # 按照不同的 type 进行排序
        de.ranking_by_type(result_details, ty)
    elif str.startswith('select '):
        ty = str.split(' ')[1]
        num = int(str.split(' ')[2])
        # 获取排位中的某一个排位的比赛
        de.get_certain_ranking(result_details, ty, num)
    elif str.startswith("date"):
        if(str == "date" or str.strip() == 'date'):
            print('获取当天时间')
            date_str = datetime.now().strftime('%Y-%m-%d')
        else:
            date_str = str.split(" ")[1]
        print('查询时间为 %s' %date_str)
        de.get_certain_date(result_details, date_str)
    elif str == 'quit':
        sys.exit()
    else:
        pass
    
def main():
    help()
    while True:
        str = input('主人请输入命令: ')
        key_word_handler(str)

if __name__ == '__main__':
    main()