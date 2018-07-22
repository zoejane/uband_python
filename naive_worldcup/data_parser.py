import csv
def parser_data(path):
    lst = []
    # 1.获取数据路径
    match_file_path = path

    # 2.读入数据
    file = open(match_file_path, 'r+', encoding='utf-8')
    lines = csv.DictReader(file)
    for line in lines:
        # 3. 整理成字典
        # 4. 加入到列表
        lst.append(dict(line))

    return lst

def main():
    match_list = parser_data('sc_data/history_matches.csv')
    team_infos = parser_data('sc_data/team_info.csv')
    squads = parser_data('sc_data/squads.csv')
    wc_matches = parser_data('sc_data/wc_group_matches.csv')

    print(match_list)
    print(team_infos)
    print(squads)
    print(wc_matches)


if __name__ == '__main__':
    main()
