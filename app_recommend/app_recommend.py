import json
import urllib.request
import csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def run_new_json():

    url = 'https://docs.google.com/spreadsheets/d/1IfDb9SmmOMtcOaGvBZDLDzKLMLUOpEUXdmuR4-GUCng/export?format=csv'
    webpage = urllib.request.urlopen(url)
    data = csv.DictReader(webpage.read().decode('utf-8-sig').splitlines())

    data_temp = []
    for item in data:
        temp = {}
        for key, value in item.items():
            temp[key] = value
        data_temp.append(temp)
    data = data_temp
    # print(data)
    result = {}  # 創建一個新的dict
    # print(result)
    for i in data:  # 把原本的data這個list一個一個丟進去這個dict中
        # 把在data中ID這個key的value作為這次reuslt這個dict中的key
        result[i['請填入記帳幫手提供您的ID！']] = i
        del i['請填入記帳幫手提供您的ID！']
    # print(result[id])  #利用stu_id去尋找以上整理出來的dict中符合ID的dict
    with open('questionnaire_data.json', 'w', encoding='utf-8') as object:
        json.dump(result, object, ensure_ascii=False, indent=4)
    return True


user_recommend = {}


def judgement(id):
    dic1 = {"Ahorro": 0,
            "記帳城市(免費版)": 0,
            "記帳城市(付費版)": 0,
            "MOZE3.0(免費版)": 0,
            "MOZE3.0(付費版)": 0,
            "CW money(免費版)": 0,
            "CW money(付費版)": 0,
            "天天記帳": 0,
            "碎碎念記帳": 0,
            "Spendee Budget & Money Tracker": 0,
            "簡單記帳": 0,
            "記帳雞": 0,
            "卡娜赫拉家計簿": 0,
            "理財幫手 AndroMoney": 0
            }

    with open('questionnaire_data.json', 'r', encoding='utf-8') as object:
        q_d = json.load(object)
    if q_d[id]['你的手機系統?'] == "Android":  # 第一題
        if q_d[id]["是否會介意付費的記帳程式"] == "YES":  # 第二題
            functionality(q_d[id]["功能性"], dic1)
            conv(q_d[id]["易上手性"], dic1)
            immediacy(q_d[id]["即時性"], dic1)
            beauty(q_d[id]["美觀"], dic1)
            fun(q_d[id]["趣味性"], dic1)
            stop(q_d[id]["停止記帳的原因"], dic1)
            habit(q_d[id]["金錢的使用習慣"], dic1)

            del dic1['記帳城市(付費版)']  # 因第二題刪
            del dic1['CW money(付費版)']  # 因第二題刪
            del dic1["MOZE3.0(免費版)"]  # 因第一題刪
            del dic1["MOZE3.0(付費版)"]  # 因第一題刪

        elif q_d[id]["是否會介意付費的記帳程式"] == "NO":
            functionality(q_d[id]["功能性"], dic1)
            conv(q_d[id]["易上手性"], dic1)
            immediacy(q_d[id]["即時性"], dic1)
            beauty(q_d[id]["美觀"], dic1)
            fun(q_d[id]["趣味性"], dic1)
            stop(q_d[id]["停止記帳的原因"], dic1)
            habit(q_d[id]["金錢的使用習慣"], dic1)

    elif q_d[id]['你的手機系統?'] == "IOS":
        if q_d[id]["是否會介意付費的記帳程式"] == "YES":
            functionality(q_d[id]["功能性"], dic1)
            conv(q_d[id]["易上手性"], dic1)
            immediacy(q_d[id]["即時性"], dic1)
            beauty(q_d[id]["美觀"], dic1)
            fun(q_d[id]["趣味性"], dic1)
            stop(q_d[id]["停止記帳的原因"], dic1)
            habit(q_d[id]["金錢的使用習慣"], dic1)

            del dic1['記帳城市(付費版)']  # 因第二題刪
            del dic1['MOZE3.0(付費版)']  # 因第二題刪
            del dic1['CW money(付費版)']  # 因第二題刪
            del dic1['理財幫手 AndroMoney']  # 因第二題刪

        elif q_d[id]["是否會介意付費的記帳程式"] == "NO":
            functionality(q_d[id]["功能性"], dic1)
            conv(q_d[id]["易上手性"], dic1)
            immediacy(q_d[id]["即時性"], dic1)
            beauty(q_d[id]["美觀"], dic1)
            fun(q_d[id]["趣味性"], dic1)
            stop(q_d[id]["停止記帳的原因"], dic1)
            habit(q_d[id]["金錢的使用習慣"], dic1)

    user_recommend[id] = dic1
    with open('user_recommend_data.json', 'w', encoding='utf-8') as object:
        json.dump(user_recommend, object, ensure_ascii=False, indent=4)
    return total(dic1)


def functionality(number, dic1):  # 功能性
    if number == "5":
        dic1["CW money(付費版)"] += 7
        dic1["CW money(免費版)"] += 1 + 6 * 10 / 7
        dic1["MOZE3.0(付費版)"] += 1 + 6 * 10 / 7
        dic1["MOZE3.0(免費版)"] += 1 + 5 * 10 / 7
        dic1["記帳城市(付費版)"] += 1 + 4 * 10 / 7
        dic1["理財幫手 AndroMoney"] += 1 + 4 * 10 / 7
        dic1["天天記帳"] += 1 + 4 * 10 / 7
        dic1["記帳城市(免費版)"] += 1 + 3 * 10 / 7
        dic1["Ahorro"] += 1 + 3 * 10 / 7
        dic1["簡單記帳"] += 1 + 2 * 10 / 7
        dic1["記帳雞"] += 1 + 2 * 10 / 7
        dic1["卡娜赫拉家計簿"] += 1 + 1 * 10 / 7
        dic1["碎碎念記帳"] += 1 + 1 * 10 / 7
        dic1["Spendee Budget & Money Tracker"] += 1
    elif number == "4":
        dic1["CW money(付費版)"] += 9
        dic1["CW money(免費版)"] += 1 + 6 * 8 / 7
        dic1["MOZE3.0(付費版)"] += 1 + 6 * 8 / 7
        dic1["MOZE3.0(免費版)"] += 1 + 5 * 8 / 7
        dic1["記帳城市(付費版)"] += 1 + 4 * 8 / 7
        dic1["理財幫手 AndroMoney"] += 1 + 4 * 8 / 7
        dic1["天天記帳"] += 1 + 4 * 8 / 7
        dic1["記帳城市(免費版)"] += 1 + 3 * 8 / 7
        dic1["Ahorro"] += 1 + 3 * 8 / 7
        dic1["簡單記帳"] += 1 + 2 * 8 / 7
        dic1["記帳雞"] += 1 + 2 * 8 / 7
        dic1["卡娜赫拉家計簿"] += 1 + 1 * 8 / 7
        dic1["碎碎念記帳"] += 1 + 1 * 8 / 7
        dic1["Spendee Budget & Money Tracker"] += 1
    elif number == "3":
        dic1["CW money(付費版)"] += 7
        dic1["CW money(免費版)"] += 1 + 6 * 6 / 7
        dic1["MOZE3.0(付費版)"] += 1 + 6 * 6 / 7
        dic1["MOZE3.0(免費版)"] += 1 + 5 * 6 / 7
        dic1["記帳城市(付費版)"] += 1 + 4 * 6 / 7
        dic1["理財幫手 AndroMoney"] += 1 + 4 * 6 / 7
        dic1["天天記帳"] += 1 + 4 * 6 / 7
        dic1["記帳城市(免費版)"] += 1 + 3 * 6 / 7
        dic1["Ahorro"] += 1 + 3 * 6 / 7
        dic1["簡單記帳"] += 1 + 2 * 6 / 7
        dic1["記帳雞"] += 1 + 2 * 6 / 7
        dic1["卡娜赫拉家計簿"] += 1 + 1 * 6 / 7
        dic1["碎碎念記帳"] += 1 + 1 * 6 / 7
        dic1["Spendee Budget & Money Tracker"] += 1
    elif number == "2":
        dic1["CW money(付費版)"] += 5
        dic1["CW money(免費版)"] += 1 + 6 * 4 / 7
        dic1["MOZE3.0(付費版)"] += 1 + 6 * 4 / 7
        dic1["MOZE3.0(免費版)"] += 1 + 5 * 4 / 7
        dic1["記帳城市(付費版)"] += 1 + 4 * 4 / 7
        dic1["理財幫手 AndroMoney"] += 1 + 4 * 4 / 7
        dic1["天天記帳"] += 1 + 4 * 4 / 7
        dic1["記帳城市(免費版)"] += 1 + 3 * 4 / 7
        dic1["Ahorro"] += 1 + 3 * 4 / 7
        dic1["簡單記帳"] += 1 + 2 * 4 / 7
        dic1["記帳雞"] += 1 + 2 * 4 / 7
        dic1["卡娜赫拉家計簿"] += 1 + 1 * 4 / 7
        dic1["碎碎念記帳"] += 1 + 1 * 4 / 7
        dic1["Spendee Budget & Money Tracker"] += 1
    elif number == "1":
        dic1["CW money(付費版)"] += 3
        dic1["CW money(免費版)"] += 1 + 6 * 2 / 7
        dic1["MOZE3.0(付費版)"] += 1 + 6 * 2 / 7
        dic1["MOZE3.0(免費版)"] += 1 + 5 * 2 / 7
        dic1["記帳城市(付費版)"] += 1 + 4 * 2 / 7
        dic1["理財幫手 AndroMoney"] += 1 + 4 * 2 / 7
        dic1["天天記帳"] += 1 + 4 * 2 / 7
        dic1["記帳城市(免費版)"] += 1 + 3 * 2 / 7
        dic1["Ahorro"] += 1 + 3 * 2 / 7
        dic1["簡單記帳"] += 1 + 2 * 2 / 7
        dic1["記帳雞"] += 1 + 2 * 2 / 7
        dic1["卡娜赫拉家計簿"] += 1 + 1 * 2 / 7
        dic1["碎碎念記帳"] += 1 + 1 * 2 / 7
        dic1["Spendee Budget & Money Tracker"] += 1


def conv(number, dic1):  # 易上手性
    if number == "5":
        dic1["簡單記帳"] += 11
        dic1["MOZE3.0(免費版)"] += 10
        dic1["MOZE3.0(付費版)"] += 10
        dic1["Ahorro"] += 9
        dic1["理財幫手 AndroMoney"] += 8
        dic1["天天記帳"] += 7
        dic1["記帳雞"] += 6
        dic1["Spendee Budget & Money Tracker"] += 5
        dic1["CW money(免費版)"] += 4
        dic1["CW money(付費版)"] += 4
        dic1["卡娜赫拉家計簿"] += 3
        dic1["記帳城市(免費版)"] += 2
        dic1["記帳城市(付費版)"] += 2
        dic1["碎碎念記帳"] += 1
    elif number == "4":
        dic1["簡單記帳"] += 9
        dic1["MOZE3.0(免費版)"] += 8.2
        dic1["MOZE3.0(付費版)"] += 8.2
        dic1["Ahorro"] += 7.4
        dic1["理財幫手 AndroMoney"] += 6.6
        dic1["天天記帳"] += 5.8
        dic1["記帳雞"] += 5
        dic1["Spendee Budget & Money Tracker"] += 4.2
        dic1["CW money(免費版)"] += 3.4
        dic1["CW money(付費版)"] += 3.4
        dic1["卡娜赫拉家計簿"] += 2.6
        dic1["記帳城市(免費版)"] += 1.8
        dic1["記帳城市(付費版)"] += 1.8
        dic1["碎碎念記帳"] += 1
    elif number == "3":
        dic1["簡單記帳"] += 7
        dic1["MOZE3.0(免費版)"] += 6.4
        dic1["MOZE3.0(付費版)"] += 6.4
        dic1["Ahorro"] += 5.8
        dic1["理財幫手 AndroMoney"] += 5.2
        dic1["天天記帳"] += 4.6
        dic1["記帳雞"] += 4
        dic1["Spendee Budget & Money Tracker"] += 3.4
        dic1["CW money(免費版)"] += 2.8
        dic1["CW money(付費版)"] += 2.8
        dic1["卡娜赫拉家計簿"] += 2.2
        dic1["記帳城市(免費版)"] += 1.6
        dic1["記帳城市(付費版)"] += 1.6
        dic1["碎碎念記帳"] += 1
    elif number == "2":
        dic1["簡單記帳"] += 5
        dic1["MOZE3.0(免費版)"] += 4.6
        dic1["MOZE3.0(付費版)"] += 4.6
        dic1["Ahorro"] += 4.2
        dic1["理財幫手 AndroMoney"] += 3.8
        dic1["天天記帳"] += 3.4
        dic1["記帳雞"] += 3
        dic1["Spendee Budget & Money Tracker"] += 2.6
        dic1["CW money(免費版)"] += 2.2
        dic1["CW money(付費版)"] += 2.2
        dic1["卡娜赫拉家計簿"] += 1.8
        dic1["記帳城市(免費版)"] += 1.4
        dic1["記帳城市(付費版)"] += 1.4
        dic1["碎碎念記帳"] += 1
    elif number == "1":
        dic1["簡單記帳"] += 3
        dic1["MOZE3.0(免費版)"] += 2.8
        dic1["MOZE3.0(付費版)"] += 2.8
        dic1["Ahorro"] += 2.6
        dic1["理財幫手 AndroMoney"] += 2.4
        dic1["天天記帳"] += 2.2
        dic1["記帳雞"] += 2
        dic1["Spendee Budget & Money Tracker"] += 1.8
        dic1["CW money(免費版)"] += 1.6
        dic1["CW money(付費版)"] += 1.6
        dic1["卡娜赫拉家計簿"] += 1.4
        dic1["記帳城市(免費版)"] += 1.2
        dic1["記帳城市(付費版)"] += 1.2
        dic1["碎碎念記帳"] += 1


def immediacy(number, dic1):  # 即時性
    if number == "5":
        dic1["CW money(免費版)"] += 11
        dic1["CW money(付費版)"] += 11
        dic1["MOZE3.0(付費版)"] += 11
    if number == "4":
        dic1["CW money(免費版)"] += 9
        dic1["CW money(付費版)"] += 9
        dic1["MOZE3.0(付費版)"] += 9
    if number == "3":
        dic1["CW money(免費版)"] += 7
        dic1["CW money(付費版)"] += 7
        dic1["MOZE3.0(付費版)"] += 7
    if number == "2":
        dic1["CW money(免費版)"] += 5
        dic1["CW money(付費版)"] += 5
        dic1["MOZE3.0(付費版)"] += 5
    if number == "1":
        dic1["CW money(免費版)"] += 3
        dic1["CW money(付費版)"] += 3
        dic1["MOZE3.0(付費版)"] += 3


def beauty(number, dic1):  # 美觀
    if number == "5":
        dic1["記帳城市(免費版)"] += 11
        dic1["記帳城市(付費版)"] += 11
        dic1["卡娜赫拉家計簿"] += 10
        dic1["簡單記帳"] += 9
        dic1["MOZE3.0(免費版)"] += 8
        dic1["MOZE3.0(付費版)"] += 8
        dic1["記帳雞"] += 7
        dic1["Ahorro"] += 6
        dic1["Spendee Budget & Money Tracker"] += 5
        dic1["理財幫手 AndroMoney"] += 4
        dic1["天天記帳"] += 3
        dic1["碎碎念記帳"] += 2
        dic1["CW money(免費版)"] += 1
        dic1["CW money(付費版)"] += 1
    elif number == "4":
        dic1["記帳城市(免費版)"] += 9
        dic1["記帳城市(付費版)"] += 9
        dic1["卡娜赫拉家計簿"] += 8.2
        dic1["簡單記帳"] += 7.4
        dic1["MOZE3.0(免費版)"] += 6.6
        dic1["MOZE3.0(付費版)"] += 6.6
        dic1["記帳雞"] += 5.8
        dic1["Ahorro"] += 5
        dic1["Spendee Budget & Money Tracker"] += 4.2
        dic1["理財幫手 AndroMoney"] += 3.4
        dic1["天天記帳"] += 2.6
        dic1["碎碎念記帳"] += 1.8
        dic1["CW money(免費版)"] += 1
        dic1["CW money(付費版)"] += 1
    elif number == "3":
        dic1["記帳城市(免費版)"] += 7
        dic1["記帳城市(付費版)"] += 7
        dic1["卡娜赫拉家計簿"] += 6.4
        dic1["簡單記帳"] += 5.8
        dic1["MOZE3.0(免費版)"] += 5.2
        dic1["MOZE3.0(付費版)"] += 5.2
        dic1["記帳雞"] += 4.6
        dic1["Ahorro"] += 4
        dic1["Spendee Budget & Money Tracker"] += 3.4
        dic1["理財幫手 AndroMoney"] += 2.8
        dic1["天天記帳"] += 2.2
        dic1["碎碎念記帳"] += 1.6
        dic1["CW money(免費版)"] += 1
        dic1["CW money(付費版)"] += 1
    elif number == "2":
        dic1["記帳城市(免費版)"] += 5
        dic1["記帳城市(付費版)"] += 5
        dic1["卡娜赫拉家計簿"] += 4.2
        dic1["簡單記帳"] += 4.2
        dic1["MOZE3.0(免費版)"] += 3.8
        dic1["MOZE3.0(付費版)"] += 3.8
        dic1["記帳雞"] += 3.4
        dic1["Ahorro"] += 3
        dic1["Spendee Budget & Money Tracker"] += 2.6
        dic1["理財幫手 AndroMoney"] += 2.2
        dic1["天天記帳"] += 1.8
        dic1["碎碎念記帳"] += 1.4
        dic1["CW money(免費版)"] += 1
        dic1["CW money(付費版)"] += 1
    elif number == "1":
        dic1["記帳城市(免費版)"] += 3
        dic1["記帳城市(付費版)"] += 3
        dic1["卡娜赫拉家計簿"] += 2.8
        dic1["簡單記帳"] += 2.6
        dic1["MOZE3.0(免費版)"] += 2.4
        dic1["MOZE3.0(付費版)"] += 2.4
        dic1["記帳雞"] += 2.2
        dic1["Ahorro"] += 2
        dic1["Spendee Budget & Money Tracker"] += 1.8
        dic1["理財幫手 AndroMoney"] += 1.6
        dic1["天天記帳"] += 1.4
        dic1["碎碎念記帳"] += 1.2
        dic1["CW money(免費版)"] += 1
        dic1["CW money(付費版)"] += 1


def fun(number, dic1):  # 趣味性
    if number == "5":
        dic1["記帳城市(免費版)"] += 11
        dic1["記帳城市(付費版)"] += 11
        dic1["卡娜赫拉家計簿"] += 6
        dic1["記帳雞"] += 6
        dic1["碎碎念記帳"] += 6
    elif number == "4":
        dic1["記帳城市(免費版)"] += 9
        dic1["記帳城市(付費版)"] += 9
        dic1["卡娜赫拉家計簿"] += 5
        dic1["記帳雞"] += 5
        dic1["碎碎念記帳"] += 5
    elif number == "3":
        dic1["記帳城市(免費版)"] += 7
        dic1["記帳城市(付費版)"] += 7
        dic1["卡娜赫拉家計簿"] += 4
        dic1["記帳雞"] += 4
        dic1["碎碎念記帳"] += 4
    elif number == "2":
        dic1["記帳城市(免費版)"] += 5
        dic1["記帳城市(付費版)"] += 5
        dic1["卡娜赫拉家計簿"] += 3
        dic1["記帳雞"] += 3
        dic1["碎碎念記帳"] += 3
    elif number == "1":
        dic1["記帳城市(免費版)"] += 3
        dic1["記帳城市(付費版)"] += 3
        dic1["卡娜赫拉家計簿"] += 2
        dic1["記帳雞"] += 2
        dic1["碎碎念記帳"] += 2


def stop(reason, dic1):
    reasons = reason.replace(' ', '')
    reasons_list = reasons.split(",")
    for res in reasons_list:
        if res == "忘記花費":  # 用定位、錄音、拍照去回想（依功能多寡去做加分）
            dic1["碎碎念記帳"] += 1  # 可拍照
            dic1["CW money(免費版)"] += 2  # 可錄音、拍照
            dic1["CW money(付費版)"] += 2
            dic1["Spendee Budget & Money Tracker"] += 1  # 可定位
            dic1["記帳雞"] += 2  # 可錄音、拍照
        elif res == "忘記記帳":  # 用定時提醒去解決，所以有「定時提醒」功能者都會再多加一分
            dic1["CW money(免費版)"] += 1
            dic1["CW money(付費版)"] += 1
            dic1["天天記帳"] += 1
            dic1["碎碎念記帳"] += 1
            dic1["簡單記帳"] += 1
            dic1["記帳城市(免費版)"] += 1
            dic1["記帳城市(付費版)"] += 1
            dic1["MOZE3.0(免費版)"] += 1
            dic1["MOZE3.0(付費版)"] += 1
            dic1["理財幫手 AndroMoney"] += 1
        elif res == "忙碌":  # 減少記帳時間：利用widget記帳、掃電子發票、常用分類快速選取解決
            dic1["CW money(免費版)"] += 3  # 三功能皆有
            dic1["CW money(付費版)"] += 3  # 三功能皆有
            dic1["碎碎念記帳"] += 1  # 可掃電子發票
            dic1["MOZE3.0(免費版)"] += 1  # 常用分類快速選取
            dic1["MOZE3.0(付費版)"] += 3  # 三功能皆有
            dic1["Ahorro"] += 1  # 可掃電子發票
            dic1["理財幫手 AndroMoney"] += 1  # 可掃電子發票
            dic1["簡單記帳"] += 1  # 常用分類快速選取
            dic1["記帳城市(免費版)"] += 1  # 常用分類快速選取
            dic1["記帳城市(付費版)"] += 1  # 常用分類快速選取
        elif res == "懶惰":
            dic1["CW money(免費版)"] += 3  # 三功能皆有
            dic1["CW money(付費版)"] += 3  # 三功能皆有
            dic1["碎碎念記帳"] += 1  # 可掃電子發票
            dic1["MOZE3.0(免費版)"] += 1  # 常用分類快速選取
            dic1["MOZE3.0(付費版)"] += 3  # 三功能皆有
            dic1["Ahorro"] += 1  # 可掃電子發票
            dic1["理財幫手 AndroMoney"] += 1  # 可掃電子發票
            dic1["簡單記帳"] += 1  # 常用分類快速選取
            dic1["記帳城市(免費版)"] += 1  # 常用分類快速選取
            dic1["記帳城市(付費版)"] += 1  # 常用分類快速選取
        elif res == "記帳麻煩":
            dic1["CW money(免費版)"] += 3  # 三功能皆有
            dic1["CW money(付費版)"] += 3  # 三功能皆有
            dic1["碎碎念記帳"] += 1  # 可掃電子發票
            dic1["MOZE3.0(免費版)"] += 1  # 常用分類快速選取
            dic1["MOZE3.0(付費版)"] += 3  # 三功能皆有
            dic1["Ahorro"] += 1  # 可掃電子發票
            dic1["理財幫手 AndroMoney"] += 1  # 可掃電子發票
            dic1["簡單記帳"] += 1  # 常用分類快速選取
            dic1["記帳城市(免費版)"] += 1  # 常用分類快速選取
            dic1["記帳城市(付費版)"] += 1  # 常用分類快速選取


def habit(reason, dic1):
    reasons = reason.replace(' ', '')
    reasons_list = reasons.split(",")
    for res in reasons_list:
        if res == "時常會借還錢":  # 有提醒借還錢功能者加一分 （歸類在功能性的定時提醒？）
            dic1["MOZE3.0(付費版)"] += 1
            dic1["理財幫手 AndroMoney"] += 1
        if res == "需要信用卡 or 帳單繳費提醒":  # 有此功能者加一分 （歸類在功能性的定時提醒？）
            dic1["MOZE3.0(付費版)"] += 1
        if res == "需要紀錄固定開銷":  # 有「設定固定開銷」功能者加一分 （已經統計到功能性中）
            dic1["天天記帳"] += 1
            dic1["Ahorro"] += 1
            dic1["簡單記帳"] += 1
            dic1["MOZE3.0(免費版)"] += 1
            dic1["MOZE3.0(付費版)"] += 1
            dic1["CW money(免費版)"] += 1
            dic1["CW money(付費版)"] += 1
        if res == "多帳戶管理（錢包、銀行、信用卡等分別紀錄）":  # 有多帳本功能者加一分 （已經統計到功能性中）
            dic1["CW money(免費版)"] += 1
            dic1["CW money(付費版)"] += 1
            dic1["MOZE3.0(免費版)"] += 1
            dic1["MOZE3.0(付費版)"] += 1
            dic1["Ahorro"] += 1
            dic1["理財幫手 AndroMoney"] += 1
            dic1["記帳城市(免費版)"] += 1
            dic1["記帳城市(付費版)"] += 1
            dic1["天天記帳"] += 1
            dic1["Spendee Budget & Money Tracker"] += 1
            dic1["碎碎念記帳"] += 1
        if res == "紀錄專案：紀錄特定事件所花的帳目（ex.旅行、週年慶）或 預算編製":
            # 有專案功能 or 編制預算功能者加一分 （已經統計到功能性中）
            dic1["MOZE3.0(免費版)"] += 1
            dic1["MOZE3.0(付費版)"] += 1
            dic1["天天記帳"] += 1
            dic1["碎碎念記帳"] += 1
            dic1["Ahorro"] += 1
            dic1["記帳城市(付費版)"] += 1
            dic1["CW money(免費版)"] += 1
            dic1["CW money(付費版)"] += 1
        if res == "需要紀錄不同貨幣":  # 有可用不同貨幣記帳or匯率轉換功能者加一分  （已經統計到功能性中）
            dic1["理財幫手 AndroMoney"] += 1
            dic1["記帳城市(免費版)"] += 1
            dic1["記帳城市(付費版)"] += 1
            dic1["CW money(免費版)"] += 1
            dic1["CW money(付費版)"] += 1
            dic1["天天記帳"] += 1


def total(dic1):
    max(dic1.values())
    for key, value in dic1.items():
        if value == max(dic1.values()):
            return key


if __name__ == '__main__':
    print(run_new_json())
    print(judgement(id='U4068c37804d834081ea24fe8d4521ab9'))
    print(judgement(id='F54091196'))
