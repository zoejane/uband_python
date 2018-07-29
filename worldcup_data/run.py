# 1. 把每一行数据读入

file = open('data/teams.txt', 'r+')
lines = file.readlines()

countries = []

for line in lines:
    # 2. 对每一行数据进行处理, 得到一个完整的国家名字
    new_line = line[1:]

    find_sharp = new_line.find('#')
    if find_sharp != -1:
        new_line = new_line[:find_sharp]
    # print(new_line)

    country = new_line.replace('\n', '').strip()
    print(country)

    # split_lines = new_line.split(' ')
    # country = split_lines[0]
    # country = country.replace('\n', '')
    
    # 3.放在一个列表里面等待使用
    countries.append(country)

print(countries)
