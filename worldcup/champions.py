# -*- coding: utf-8 -*-

import csv

# 读取csv数据文件
with open("WorldCups.csv","r") as f:
    csv_reader = csv.DictReader(f)
    competitions = []
    for row in csv_reader:
        competitions.append(row)

# print(competitions)

# 初始化计数器
champions = dict()
for competition in competitions:
    winner = competition["Winner"]
    if winner == "Germany FR":
        winner = 'German'
    # 统计当前比赛的冠军
    if winner in champions:
        count = champions[winner]
        champions[winner] = count + 1
    else:
        champions[winner] = 1

# 输出
for champion in champions:
    print(champion + ' - ' + str(champions[champion]))
