import json

mydic = {}
with open('champion.json', encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    a = json_data["data"]
    b = a.values()
    # print(len(b))
    for i in b:
        # print(i)
        mydic[i["key"]] = i["id"]

with open('nsm.json', 'w', encoding="utf-8") as make_file:
    json.dump(mydic, make_file, ensure_ascii=False, indent="\t")

print(mydic)