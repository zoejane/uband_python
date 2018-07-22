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

def ranking(result_details):
        # 1. 按照 map 当中的 recommendation_score 字段排序(降序)
        ranking_list = sorted(result_details.items(), key=lambda item:item[1]['recommendation_score'], reverse=True)
        index = 0
        for item in ranking_list:
            index = index + 1
            format_print(item, index)


def ranking_by_type(result_details, ty):

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
    index = 0
    for item in ranking_list:
        index = index + 1
        format_print(item, index)

def main():
    result_details = md.moding()
    ranking(result_details)

if __name__ == '__main__':
    main()