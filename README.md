# 夸夸！！！

## 基于话题相似度的夸夸机器人

原作者[@Hualong_Zhang](https://github.com/xiaopangxia)

我修复了模块的若干问题，优化目录结构，去除了基于chatterbot的部分，提供了一个flask后端。

语料来自豆瓣表扬小组，详见https://github.com/xiaopangxia/kuakua_corpus

相似度采用TF-IDF、LSI、LDA等，搜索top4相似话题的回复，从中随机返回表扬语句，效果还不错。

![](https://raw.githubusercontent.com/xiaopangxia/kuakua_robot/master/image/kukua_2.PNG)

## 食用方法


