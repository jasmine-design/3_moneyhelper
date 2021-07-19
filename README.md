## 3_money_helper:

* 成果說明


    此為「運算思維與問題解決」之期末成果，分組進行專題。
    我們這組的主題為探討「如何幫助人們持之以恆地記帳」，組員共有五人。 
    在了解問題、解法發想後，我們最終產出為「linebot機器人—記帳幫手」。

* 「Linebot記帳幫手」功能說明


    此Linebot記帳幫手，提供「有需求卻無法持之以恆記帳」的人們多項輔助記帳功能，
    包括「記帳程式推薦、定時記帳提醒、社群群組分帳」等，
    不僅能幫助大家找到最適合自己的記帳程式；在忙碌時支援您語音記帳；
    設置每日提醒記帳；並且提供群組分帳功能，幫助您有效快速地瞭解自身支出，
    有效消除任何中斷記帳的可能性，讓您能輕鬆、持之以恆地快樂記帳！

* 分工說明

    
    在此專案中，我負責的部分為
    
    1.  欠債提醒 – 流程設計、程式碼撰寫：
        提供使用者紀錄多筆債務資訊，系統會在指定時間推送訊息，提醒使用者處理債款的功能。
        (程式碼：Linebot_server.py, Linebot_function.py, flex_message, debt_data.json)
        
    2.  群組分帳網站 – 流程設計、視覺設計：
        幫助使用者在出遊、日常購物時快速分帳。
    

### Linebot_function.py

* 欠債提醒 | API definition

| API  | definition |
| ------------- |:-------------:|
| setting_debt_message() | linebot回傳flex_message訊息  |
| debt_data(user_id)  | 在debt_data.json中建立使用者資料 |
| enter_debt_count(user_id) | 在debt_data.json中建立使用者資料|
| enter_debt_data_plus(text, time, user_id) |在debt_data.json中加入使用者的回傳的資料|
| cancel_debt_data(user_id, num) | 刪除debt_data.json中該筆使用者的資料 |
| debt_alerting_time()  | linebot回傳flex message訊息詢問欠債提醒時間 |
| finish_debt_alert(user_id) | linebot回傳text message訊息，通知使用者設定成功 |
| get_debt_alert_time_user() | 於指定時間，linebot推送欠債提醒 |

### Linebot_server.py

    主要建置程式碼由組員撰寫，我負責的部分為欠債提醒之相關內容。
    
### flex_message
    
    資料夾中的 debt.json, debt_alerting_time.json 為linebot欠債提醒的flex message程式碼。


### debt_data.json
    
    為儲存使用者欠債提醒相關資訊的檔案。