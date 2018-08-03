import pymongo

client = pymongo.MongoClient('localhost', 27017)  # 连接Mongo客户端

walden = client['walden']  # 创建名为walden的数据库

sheet_tab = walden['sheet_tab']  # 在walden数据库中创建名为sheet_tab的表

path = 'C:\\Users\hs\Desktop\walden.txt'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        data = {
            'index': index,
            'line': line,
            'words': len(line.split())
        }
        sheet_tab.insert_one(data)


# lt/$lte/$gt/$gte/$ne,依次等价于</<=/>/>=/!=,(l:less t:than g:greater e:equal n:not)

# for item in sheet_tab.find():
#     print(item['line'])
