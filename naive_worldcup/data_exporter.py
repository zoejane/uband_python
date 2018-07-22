#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import model as md

def format_print(rank_item, rank):
    real_item = rank_item[1]
    recommendation_index = int((real_item['recommendation_score'] / 0.5) * 100)
    uncertainty_index = int((real_item['uncertainty_score'] / 0.4) * 100)
    goal_index = int((real_item['goal_score'] / 0.4) * 100)
    fame_index = int((real_item['fame_score'] / 0.8) * 100)

    # print(real_item)
    print('---比赛场次推荐---')
    print('推荐排名: %d' % (rank))
    print('%s VS %s' % (real_item['team_a'], real_item['team_b']))
    print('综合推荐指数: %d' % (recommendation_index))
    print('分类推荐指数')
    print('悬念指数: %d' % (uncertainty_index))
    print('比分指数: %d' % (goal_index))
    print('球星指数: %d' % (fame_index))
    print('\n')

def print_list(ranking_list):
    index = 0
    for item in ranking_list:
        index = index + 1
        format_print(item, index)

def ranking_by_type(result_details, ty='recommendation', need_print_list=True):

    key_dict = {
        'fame': 'fame_score',
        'goal': 'goal_score',
        'uncertainty': 'uncertainty_score',
        'recommendation': 'recommendation_score'
    }

    if(ty not in key_dict.keys()):
        print('没有找到合适的类型哦!')
        return 0
    ty_value = key_dict[ty]

    # 1. 按照 map 中的字段排序(降序)
    ranking_list = sorted(result_details.items(), key=lambda item: item[1][ty_value], reverse=True)

    if need_print_list:
        print_list(ranking_list)

    return ranking_list

def get_certain_ranking(result_details, ty, num):
    ranklist = ranking_by_type(result_details, ty, need_print_list=False)

    # 1. 找到排名为 num 的位置
    rank_num = num - 1
    # 2. 打印
    format_print(ranklist[rank_num], num)
    # 3. 返回
    return ranklist[rank_num]

def get_certain_date(result_details, dt_str):
    # 1. 获取当天所有的场次
    new_results = dict()
    for index, item in enumerate(result_details.values()):
        time = item['match_date']
        time_str = time.strftime("%Y-%m-%d")

        if(dt_str == time_str):
            new_results[str(index)] = item

    if(len(new_results.values()) == 0):
        print('当天没有任何比赛')
        return 0

    # 2. 排序
    # 3. 打印和输出
    ranking_by_type(new_results)

def main():
    result_details = md.moding()
    ranking(result_details)

if __name__ == '__main__':
    main()