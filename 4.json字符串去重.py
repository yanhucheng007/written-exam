import json

json_str = """[{
    "name": "张三",
    "serial": "0001"
  }, {
    "name": "李四",
    "serial": "0002"
  }, {
    "name": "王五",
    "serial": "0003"
  }, {
    "name": "王五2",
    "serial": "0003"
  }, {
    "name": "赵四",
    "serial": "0004"
  }, {
    "name": "小明",
    "serial": "005"
  }, {
    "name": "小张",
    "serial": "006"
  }, {
    "name": "小李",
    "serial": "006"
  }, {
    "name": "小李2",
    "serial": "006"
  }, {
    "name": "赵四2",
    "serial": "0004"
  }]"""

json_obj = json.loads(json_str)
result = []
temp = {}
for dict_ in json_obj:
    if dict_["serial"] in temp.keys():
        continue
    else:
        temp[dict_["serial"]] = dict_
for dict_1 in temp.values():
    result.append(dict_1)

json_str_r = json.dumps(result,ensure_ascii=False)

print(json_str_r)

