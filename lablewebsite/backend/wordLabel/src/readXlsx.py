import pandas as pd
import  os

def get_test_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(BASE_DIR, 'xls', 'video_asr_sample_detail_morph_extra.json')
    df=pd.read_json(json_path)
    row_data = []
    for index, row in df.iterrows():
        row_data.append(row)
    return row_data
def get_final_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(BASE_DIR, 'xls', 'video_asr_filter_detail_morph_extra.json')
    df=pd.read_json(json_path)
    row_data = []
    for index, row in df.iterrows():
        row_data.append(row)
    return row_data
def get_index_test(user_name):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(BASE_DIR, 'xls', 'log.json')
    index=0
    temp_data = pd.read_json(json_path)
    if user_name=="admin1":
        for i in range(temp_data.shape[0]):
            if temp_data.iloc[i]["username"]==user_name:
                index= temp_data.iloc[i]["last_label_index_test"]+1
    elif user_name=="admin2":
        for i in range(temp_data.shape[0]):
            if temp_data.iloc[i]["username"]==user_name:
                index= temp_data.iloc[i]["last_label_index_test"]+1
    elif user_name=="admin3":
        for i in range(temp_data.shape[0]):
            if temp_data.iloc[i]["username"]==user_name:
                index= temp_data.iloc[i]["last_label_index_test"]+1
    else:
        for i in range(temp_data.shape[0]):
            if temp_data.iloc[i]["username"]==user_name:
                index= temp_data.iloc[i]["last_label_index_test"]+1
    return   int(index)

def get_index_final():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(BASE_DIR, 'xls', 'final_log.json')
    temp_data = pd.read_json(json_path)
    index = temp_data.iloc[0]["final_index"] + 1
    return  int( index)




def get_test_data_information(index):
    video_info_test=get_test_data()
    temp=video_info_test[index]
    video_plat=temp["plat_name"]
    video_name = temp["chanel_name"]
    video_chanel =temp["file_name"]
    video_path=os.path.join("video","downloads",video_plat,video_name,video_chanel)
    morph_details=temp["asr_result_para_detail"]
    return  video_path,temp["asr_result_para"]," ",morph_details
def get_final_data_information(index):
    video_info_test=get_final_data()
    temp=video_info_test[index]
    video_plat=temp["plat_name"]
    video_name = temp["chanel_name"]
    video_chanel =temp["file_name"]
    video_path=os.path.join("video","downloads",video_plat,video_name,video_chanel)
    morph_details = temp["asr_result_para_detail"]
    return  video_path,temp["asr_result_para"]," ",morph_details



def authorize(user_format):
    password_list = [{"username": "admin1", "password": "yzunlp1"},
                     {"username": "admin2", "password": "yzunlp2"},
                     {"username": "admin3", "password": "3admin"},
                     {"username": "admin4", "password": "4admin"}]
    for entry in password_list:
        if entry['username'] == user_format['username'] and entry['password'] == user_format['password']:
            return True
    return False



