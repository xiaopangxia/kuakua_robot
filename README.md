# kuakua_robot
# 用多种方式实现的夸夸机器人
### 语料来自豆瓣表扬小组，详见https://github.com/xiaopangxia/kuakua_corpus

### 1. 基于话题相似度的夸夸机器人
相似度采用TF-IDF、LSI、LDA等，搜索top4相似话题的回复，从中随机返回表扬语句，效果还不错。
![](https://raw.githubusercontent.com/xiaopangxia/kuakua_robot/master/image/kukua_2.PNG)



### 2. 借助chatterbot实现的夸夸闲聊机器人
效果很不好，chatterbot本身适用于闲聊，任务性差，对语料的方法性好像也不太敏感
![](https://raw.githubusercontent.com/xiaopangxia/kuakua_robot/master/image/kuakua_1.PNG)


### 3. 待更新
