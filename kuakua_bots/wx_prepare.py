# -*- coding: utf-8 -*-
# File: douban_spider.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-04-02
import json
import requests

# 测试号
# app_id = "wx8b499bf1d941e739"
# app_secret = "7fa965e42e561778ae6503328cf2ae6e"
# access_token = "20_2cd8zA9vKfOk2SJlsIOUO0tqr8nbKZ4_oJ4qk-aiv5PyqmY0Fai_m4AEicwhI_fmlpmYetmqMEd19QUZuLpNlbZo-nYdK58E0nQi0nW82N8z7kPY7lbDkzJgM5-bw6q_JyNZeLiD5GXZsMjVHGXcABANMD"
# res = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(app_id, app_secret))


# 正式号
app_id = "wxb50bb81c609eae1c"
app_secret = "de91cb09d2daac422b794814ff783d06"



base_url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=20_2cd8zA9vKfOk2SJlsIOUO0tqr8nbKZ4_oJ4qk-aiv5PyqmY0Fai_m4AEicwhI_fmlpmYetmqMEd19QUZuLpNlbZo-nYdK58E0nQi0nW82N8z7kPY7lbDkzJgM5-bw6q_JyNZeLiD5GXZsMjVHGXcABANMD"
send_data = {
            "touser": "o6Y3A54m7Qmsglj-f9nYJZ3jLrhg",
            "msgtype": "text",
            "text": {
                "content": "测试"
            }
        }


my_session = requests.session()
my_session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
my_session.post(base_url, data=json.dumps(send_data, ensure_ascii=False).encode('utf8'))


# print(res.content)
# print(res.text)
