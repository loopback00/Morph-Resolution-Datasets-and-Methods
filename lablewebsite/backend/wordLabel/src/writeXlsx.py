import pandas as pd
import  os
import json

def append_to_jsonl(filename, data):
    with open(filename, 'a', encoding='utf-8') as f:
        if isinstance(data, list):
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        else:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
def append_to_jsonl_os(type,data):
    if type=="test1":
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(BASE_DIR, 'xls', 'test_result_user1.jsonl')
    elif type=="test2":
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(BASE_DIR, 'xls', 'test_result_user2.jsonl')
    elif type=="test3":
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(BASE_DIR, 'xls', 'test_result_user3.jsonl')
    elif type=="test4":
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(BASE_DIR, 'xls', 'test_result_user4.jsonl')
    else:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(BASE_DIR, 'xls', 'final_result.jsonl')
    append_to_jsonl(json_path, data)


def change_index_test(user_name,index,type):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(BASE_DIR, 'xls', 'log.json')
    df = pd.read_json(json_path)
    df.loc[df['username'] == user_name, 'last_label_index_test'] = index
    df.to_json(json_path,orient='records', indent=3, force_ascii=False)
def change_index_final(user_name,index):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(BASE_DIR, 'xls', 'final_log.json')
    df = pd.read_json(json_path)
    df.loc[0,'final_index'] = index
    print(df)
    if user_name=="admin1":
        df.loc[0,'user1_label'] = int(df.loc[0,'user1_label'])+1
    elif user_name=="admin2":
        df.loc[0,'user2_label'] = int(df.loc[0,'user2_label'])+1
    elif user_name == "admin3":
        df.loc[0, 'user3_label'] = int(df.loc[0, 'user3_label']) + 1
    else:
        df.loc[0,'user4_label'] = int(df.loc[0,'user4_label'])+1
    df.to_json(json_path,orient='records', indent=3, force_ascii=False)
