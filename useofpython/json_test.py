# 学习json的使用
import json

# 将Python对象转换为JSON字符串
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)

# 将JSON字符串转换为Python对象
parsed_data = json.loads(json_string)
print(parsed_data)

# 将Python对象写入JSON文件
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# 从JSON文件读取Python对象
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
print(loaded_data)


# import os 
# # 删除刚才创建的JSON文件
# os.remove('data.json')
