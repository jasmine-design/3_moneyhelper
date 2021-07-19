import json
import time
import re
from threading import Timer
from apscheduler.schedulers.blocking import BlockingScheduler

# 程式撰寫者：林玟其

def setting_debt_message(): # linebot回傳flex_message訊息
    flex_message = json.load(
        open('./flex_message/debt.json', 'r', encoding='utf-8'))
    return flex_message

def debt_data(user_id): # 在debt_data.json中建立使用者的資料
    with open("./debt_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    if user_id not in data:
        data[user_id] = {}
    with open('./debt_data.json', "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False,indent=4)

def enter_debt_count(user_id): # 在debt_data.json中建立使用者的資料
    with open("./debt_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    num = len(data[user_id].keys())
    data[user_id][str(num + 1)] = {}
    data[user_id][str(num + 1)]["content"] = "default"
    data[user_id][str(num + 1)]["debt_time"] = "default"
    with open('./debt_data.json', "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def enter_debt_data_plus(text, time, user_id):# 在debt_data.json中加入使用者的回傳的資料
    with open("./debt_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    num = len(data[user_id].keys())
    # print(data[user_id][str(num)])
    if text != '0':
        data[user_id][str(num)]["content"] = text[5:]
        with open('./debt_data.json', "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    elif time != '0':
        data[user_id][str(num)]["debt_time"] = time
        with open('./debt_data.json', "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

def cancel_debt_data(user_id, num):# 刪除debt_data.json中該筆使用者的資料（取消欠債提醒）
    with open("./debt_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    data[user_id][num]["content"] = 'finish'
    data[user_id][num]["debt_time"] = 'finish'
    with open('./debt_data.json', "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def debt_alerting_time(): # linebot回傳flex message訊息詢問欠債提醒時間
    flex_message = json.load(
        open('./flex_message/debt_alerting_time.json', 'r', encoding='utf-8'))
    reply = flex_message
    return reply

def finish_debt_alert(user_id): # linebot回傳text message訊息，通知使用者設定成功
    with open("./debt_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    a = list(data[user_id])[-1]
    reply = "設定成功！將於" + data[user_id][a]['debt_time'] + "提醒你：\n" + data[user_id][a]['content']
    return reply

def get_debt_alert_time_user(): # 於指定時間，linebot推送欠債提醒
    with open("./debt_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    now = time.ctime().split(" ")[3][:5]
    user = []
    content = []
    for i in data:
        for n in data[i]:
            if data[i][n]['debt_time'] == now:
                user.append(i)
                content.append(data[i][n]['content'])
    return user, content



# 程式撰寫者：其他組員

def register_to_group_data(group_id, user_id, user_name):
    with open("./webpage/group_data.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    if group_id not in data:
        data[group_id] = {
            "user_list": {
            },
            "history": {
            }
        }

    if user_id not in data[group_id]["user_list"]:
        data[group_id]["user_list"][user_id] = {
            'user_name': user_name,
            "debts": {}
        }
        reply = user_name + "成功註冊"
    else:
        reply = user_name + "已註冊過"

    with open("./webpage/group_data.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return reply

def setting_flex_message():
    # create flex_message json file from https://developers.line.biz/flex-simulator/
    flex_message = json.load(
        open('./flex_message/group_feature.json', 'r', encoding='utf-8'))
    return flex_message

def setting_alert_message():
    flex_message = json.load(
        open('./flex_message/alert.json', 'r', encoding='utf-8'))
    return flex_message

def setting_check_message():
    flex_message = json.load(
        open('./flex_message/alert_check.json', 'r', encoding='utf-8'))
    return flex_message

def setting_recommend_message():
    recommend_message = json.load(
        open('./flex_message/recommend.json', 'r', encoding='utf-8'))
    return recommend_message

def alert_data(user_id):
    with open("./alert_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    if user_id not in data:
        data[user_id] = {
            "time": "tm",
            "audio": "0"
        }
    with open('./alert_data.json', "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def enter_alert_time_data(tm, user_id):
    with open("./alert_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    data[user_id]["time"] = tm
    with open('./alert_data.json', "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def enter_alert_audio_data(user_id, aud):
    with open("./alert_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    data[user_id]["audio"] = aud
    with open('./alert_data.json', "w", encoding='utf-8') as f:

        json.dump(data, f, ensure_ascii=False, indent=4)

def return_alert_data():
    with open("./alert_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    return data

def get_alert_time_user():
    with open("./alert_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    now = time.ctime().split(" ")[3][:5]
    user = []
    user2 = []
    for i in data:
        if data[i]["time"] == now:
            user.append(i)
            if data[i]["audio"]!="0":
               user2.append(i)
    with open("./debt_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data2 = json.load(f, strict=False)
    debt_user = []
    content = []
    num = []
    for i in data2:
        for n in data2[i]:
            if data2[i][n]['debt_time'] == now:
                print(data2[i][n]['debt_time'])
                debt_user.append(i)
                content.append(data2[i][n]['content'])
                num.append(n)
    return user,user2,debt_user,content, num

def get_audio_user():
    with open("./alert_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data = json.load(f, strict=False)
    user = []
    for i in data:
        if data[i]["audio"] != "0":
            user.append(i)

    return user

def cancel_alert(user_id):
    with open("./alert_data.json", "r", encoding='utf-8-sig', errors='ignore') as f:
        data= json.load(f, strict=False)
    for i in data:
        if i==user_id:
            data[i]["time"]="tm"
        with open('./alert_data.json', "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print(get_audio_user())
