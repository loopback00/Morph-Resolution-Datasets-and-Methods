from flask import Flask,request
from flask_cors import CORS
import pandas as pd
import  json
from src.readXlsx import get_index_test,get_test_data_information,get_index_final,get_final_data_information
from src.writeXlsx import append_to_jsonl_os,change_index_test,change_index_final
import  os
import  time

from src.readXlsx import authorize
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route("/authorize")
def user_authorize():
    if request.method =='GET':
        user_format = request.args.get('s1')
        user_format = json.loads(user_format)
        judge=authorize(user_format)
        auth_infp=[str(judge),user_format["username"]]
    else:
        auth_infp=[str(False),"none"]
    return auth_infp

@app.route("/getfinalindex")
def get_final_index():
    if request.method =='GET':
        user_name = request.args.get('s1')
        index = int(get_index_final())
        video_path, asr_result, label,morph_extra = get_final_data_information(index)
        data = [video_path,asr_result,label,index,morph_extra]
    return data


@app.route("/gettestindex")
def get_test_index():
    if request.method =='GET':
        user_name = request.args.get('s1')
        index = int(get_index_test(user_name))
        video_path, asr_result, label,morph_extra = get_test_data_information(index)
        data = [video_path,asr_result,label,index,morph_extra]
    return data

@app.route("/writedata")

def writejson():
    if request.method == 'GET':
        json_str = request.args.get('data')
        data = json.loads(json_str)
    
        if data["username"]=="admin1":
            append_to_jsonl_os("test1",data)
        elif data["username"]=="admin2":
            append_to_jsonl_os("test2",data)
        elif data["username"]=="admin3":
            append_to_jsonl_os("test3",data)
        else:
            append_to_jsonl_os("test4", data)
        # video_info=[]
        change_index_test(data["username"],data["index"],"test")
        index = get_index_test(data["username"])
        video_path, asr_result, label,morph_extra = get_test_data_information(index)
        data = [video_path, asr_result, label, index,morph_extra]

    return data

@app.route("/writedatafinal")

def writejson_final():
    if request.method == 'GET':
        json_str = request.args.get('data')
        data = json.loads(json_str)
        append_to_jsonl_os("final",data)

        # video_info=[]
        change_index_final(data["username"],data["index"])
        index = get_index_final()
        video_path, asr_result, label,morph_extra = get_final_data_information(index)
        data = [video_path, asr_result, label, index,morph_extra]

    return data


if __name__ == '__main__':


    app.run(debug=True)
