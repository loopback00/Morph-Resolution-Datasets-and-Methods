
import  pandas as pd

data=pd.read_json("xls/video_asr_filter_detail_morph_extra.json")
print(data)
# new_data = {"name": "张三", "age": 25, "city": "北京"}
# append_to_jsonl(r'D:\MorphDataset\wordLabel\xls\test_result_user1.jsonl', new_data)
#
# multiple_data = [
#     {"name": "李四", "age": 30, "city": "上海"},
#     {"name": "王五", "age": 28, "city": "广州", "country": "中国"}
# ]
# append_to_jsonl(r'D:\MorphDataset\wordLabel\xls\test_result_user1.jsonl', multiple_data)

# with open(r'D:\MorphDataset\wordLabel\xls\test_result_user1.jsonl', 'r', encoding='utf-8') as f:
#     for line in f:
#         data = json.loads(line.strip())
#         print(data["name"])