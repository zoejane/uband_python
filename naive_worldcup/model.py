#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import data_parser as dp
import math
from datetime import datetime

def get_team_info(teams, team_name):
    for team in teams:
        if team["Name"] == team_name:
            return int(team["Rank"]), team["Code"]

def get_match_uncertainty(match, rank_a, rank_b):
    # 计算排名差值
    rank_diff = abs(rank_a - rank_b)

    # 计算赔率因素
    odds_win, odds_draw, odds_lose = float(match["Odds Win"]), float(match["Odds Draw"]), float(match["Odds Lose"])
    avg_odds = (odds_win + odds_draw + odds_lose) / 3
    std_odds = math.sqrt(((odds_win - avg_odds) ** 2 + (odds_draw - avg_odds) ** 2 + (odds_lose - avg_odds) ** 2) / 3)

    uncertainy = 0.5 * 1 / rank_diff + 0.5 * 1 / (1 + std_odds)
    return uncertainy

def get_match_goals(history_matches, team_a, team_b):
    matches_a, matches_b = 0, 0
    scores_a, scores_b = 0, 0
    for match in history_matches:
        if match["Home Team"] == team_a or match["Away Team"] == team_a:
            matches_a += 1
            scores_a += int(match["Score Home"]) + int(match["Score Away"])
        if match["Home Team"] == team_b or match["Away Team"] == team_b:
            matches_b += 1
            scores_b += int(match["Score Home"]) + int(match["Score Away"])
    goals_exp = 0.5 * scores_a / (matches_a * 90) + 0.5 * scores_b / (matches_b * 90)
    return goals_exp * 10

def get_player_fame_bonus(posts_count):
    posts_count = int(posts_count)
    if posts_count < 100:
        return 1
    elif posts_count < 500:
        return 1.1
    elif posts_count < 1000:
        return 1.2
    else:
        return 1.3

def get_player_fame_lv(fans_count):
    fans_count = int(fans_count)
    if fans_count < 1e4:
        return 1
    elif fans_count < 1e5:
        return 2
    elif fans_count < 1e6:
        return 5
    elif fans_count < 1e7:
        return 10
    elif fans_count < 5 * 1e7:
        return 20
    else:
        return 50

def get_match_fame(squads, code_a, code_b):
    fame_a, fame_b = 0,0
    for player in squads:
        player_posts_count = player["Instagram Posts"]
        player_fans_count = player["Instagram Fans"]
        if player["Nation"] == code_a:
            fame_a += get_player_fame_bonus(player_posts_count) * get_player_fame_lv(player_fans_count)
        if player["Nation"] == code_b:
            fame_b += get_player_fame_bonus(player_posts_count) * get_player_fame_lv(player_fans_count)
    match_fame = 0.5 * fame_a + 0.5 * fame_b
    return match_fame / 100

def format_date(dt, tim):
    month = int(dt.split('.')[0])
    day = int(dt.split('.')[1])
    hour = int(tim.split(':')[0])
    minute = int(tim.split(':')[1])

    return datetime(year=2018, month=month, day=day, hour=hour, minute=minute)

def moding():
    # 1. 读取数据
    matches = dp.parser_data('sc_data/wc_group_matches.csv')
    teams = dp.parser_data('sc_data/team_info.csv')
    history_matches = dp.parser_data('sc_data/history_matches.csv')
    squads = dp.parser_data('sc_data/squads.csv')

    # 2. 初始化结果表示结构
    match_details = dict()

    # 3. 计算每场比赛的推荐度
    for match in matches:
        # 3.1 获取比赛基本信息
        result_map = dict()
        match_id = match["No."]
        match_date = format_date(match['Date'], match['Time'])
        team_a, team_b = match["TeamA"], match["TeamB"]
        rank_a, code_a = get_team_info(teams, team_a)
        rank_b, code_b = get_team_info(teams, team_b)

        # 3.2 计算悬念大小
        uncertainty_score = get_match_uncertainty(match, rank_a, rank_b)

        # 3.3 计算进球期望
        goal_score = get_match_goals(history_matches, team_a, team_b)

        # 3.4 计算球员知名度
        fame_score = get_match_fame(squads, code_a, code_b)

        # 3.5 计算综合推荐分数

        recommendation_score = (uncertainty_score + goal_score + fame_score) / 3

        # print(match_id + " " + team_a + " vs. " + team_b + ":")
        # print("uncertainty_score: %.2f goal_score: %.2f fame_score: %.2f" % (uncertainty_score, goal_score, fame_score))
        # print("recommendation socre: %.2f" % recommendation_score)

        # 3.6 生成比赛推荐结果
        result_map['match_id'] = match_id
        result_map['team_a'] = team_a
        result_map['team_b'] = team_b
        result_map['uncertainty_score'] = uncertainty_score
        result_map['goal_score'] = goal_score
        result_map['fame_score'] = fame_score
        result_map['recommendation_score'] = recommendation_score
        result_map['match_date'] = match_date

        match_details[match_id] = result_map

    # print(match_details)
    return match_details

if __name__ == '__main__':
    moding()