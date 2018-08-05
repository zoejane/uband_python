# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def parse_data(path):
    lst = []
    match_file_path = path

    with open(match_file_path, "r+", encoding='utf-8') as file:
        lines = csv.DictReader(file)
        for line in lines:
            lst.append(dict(line))
    return lst

def add_record(name, side , goal_scored, goal_against):
    record = {
        'name': name,
        'side': side,
        'goal_scored': int(goal_scored),
        'goal_against': int(goal_against)
    }
    return record

if __name__ == "__main__":
    # 读取数据
    history_matches = parse_data('sc_data/history_matches.csv')
    teams = parse_data('sc_data/team_info.csv')

    # 数据清晰
    team_names = set()
    for team in teams:
        team_names.add(team['Name'])

    simple_matches = []
    for match in history_matches:
        if match['Home Team'] in team_names:
            team_name = match['Home Team']
            simple_matches.append(add_record(team_name, 'Home', match['Score Home'], match['Score Away']))
        if match['Away Team'] in team_names:
            team_name = match['Away Team']
            simple_matches.append(add_record(team_name, 'Away', match['Score Away'], match['Score Home']))

# 数据可视化
    data = pd.DataFrame(simple_matches)
    plot = sns.barplot(x='goal_scored', y='name', hue='side' ,data=data, ci=0)
    plt.show()