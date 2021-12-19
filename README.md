# 夸夸！！！

## 基于话题相似度的夸夸机器人

原作者[@Hualong_Zhang](https://github.com/xiaopangxia)

我修复了模块的若干问题，优化目录结构，去除了基于chatterbot的部分，提供了一个flask后端。

语料来自豆瓣表扬小组，详见https://github.com/xiaopangxia/kuakua_corpus

相似度采用TF-IDF、LSI、LDA等，搜索top4相似话题的回复，从中随机返回表扬语句，效果还不错。

![](https://raw.githubusercontent.com/xiaopangxia/kuakua_robot/master/image/kukua_2.PNG)

## 食用方法

将sim_kuakua移动到项目文件夹，在你的项目内使用

```Python
from sim_kuakua import kuakuaChat
```

### 直接在项目中调用

```Python
input="" #输入语句
bot=kuakuaChat()
answerList=bot.answer_question(input)
```

会返回一个回答的List

### 启动服务器

```Python
bot=kuakuaChat()
bot.start_server()
```

这样会在5000端口启动一个服务器。

请求 /getKuakua ,附加payload sentence={输入}

样例：
