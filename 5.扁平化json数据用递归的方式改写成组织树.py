import json

json_str = """[
    {
      "id": "1",
      "name": "中国",
      "code": "110",
      "parent": ""
    },
    {
      "id": "2",
      "name": "北京市",
      "code": "110000",
      "parent": "110"
    },
    {
      "id": "3",
      "name": "河北省",
      "code": "130000",
      "parent": "110"
    },
    {
      "id": "4",
      "name": "四川省",
      "code": "510000",
      "parent": "110"
    },
    {
      "id": "5",
      "name": "石家庄市",
      "code": "130001",
      "parent": "130000"
    },
    {
      "id": "6",
      "name": "唐山市",
      "code": "130002",
      "parent": "130000"
    },
    {
      "id": "7",
      "name": "邢台市",
      "code": "130003",
      "parent": "130000"
    },
    {
      "id": "8",
      "name": "成都市",
      "code": "510001",
      "parent": "510000"
    },
    {
      "id": "9",
      "name": "简阳市",
      "code": "510002",
      "parent": "510000"
    },
    {
      "id": "10",
      "name": "武侯区",
      "code": "51000101",
      "parent": "510001"
    },
    {
      "id": "11",
      "name": "金牛区",
      "code": "51000102",
      "parent": "510001"
    }
  ]"""

json_obj = json.loads(json_str)
# for d in json_obj:
#     d["children"]=[]
#     for temp in json_obj:
#         if d["code"] == temp["parent"]:
#             d["children"].append(temp)
# print([json_obj[0]])


def test(lists,index1,index2):
    if index2 == 0 and index1 < len(lists):
        lists[index1]["children"] = []
    if index1 == len(lists):
        return
    elif index2 == len(lists):
        test(lists,index1+1,0)
    else:
        if lists[index1]["code"] == lists[index2]["parent"]:
            lists[index1]["children"].append(lists[index2])
        test(lists,index1,index2+1)
    return lists

result = [t for t in test(json_obj,0,0) if t["parent"] == '' ]
print(result)
