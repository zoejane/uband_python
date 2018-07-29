import json

# 读取文件
with open('response.txt', 'r', encoding='utf-8') as f:
    contents = ''
    for line in f.readlines():
        contents += line.strip()
# print(contents)

comments = json.loads(contents) # 这是一个 dictionary
# print(comments)
# print(type(comments))

# 初始化计算器
users = dict()

# 循坏遍历
for comment in comments: # for xxx in 某个dictionary:  xxx 表示的是其中的 keys 部分, 相当于 for xxx in comments.keys():
    if comment != 'totComment':
        comment_content = comments[comment] # comment 是 key 部分, comments[comment] 就是求的 value 部分, 也就是 k:v 中冒号后的 v 部分
        country = comment_content["Country"] # comment_content 还是一个列表, "Country" 是key 部分, comment_content["Country"] 求的是 value 部分

        if country in users:
            users[country] = users[country] + 1 # users[country] 代表 users 列表中 country 这个 key 对应的 value
        else:
            users[country] = 1

# 输出
for country in users:
    print(country + " - " + str(users[country]))
