# -*- coding: utf-8 -*-
# File: chatterbot_kuakua.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-04-03

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import json
# logging.basicConfig(level=logging.INFO)

class kuakuaChat():
    @classmethod
    def corpus_convert(cls):
        """
        格式转化，将夸夸语料转成chatterbot训练语料
        :return:
        """
        dialog_list = []
        with open('douban_kuakua_qa.txt', 'r', encoding='utf8') as in_file:
            que = None
            ans = None
            for line in in_file.readlines():
                if 'Q:\t' in line:
                    que = line.strip().split('\t')[-1]
                elif 'A:\t' in line:
                    ans = line.strip().split('\t')[-1]
                    if len(que) > 5 and ans is not None and len(ans) > 2:
                        dialog_list.append([que, ans])

                    que = None
                    ans = None

        chatterbot_corpus = {"conversations": dialog_list}
        out_file = open('kuakua_corpus.json', 'a', encoding='utf8')
        json.dump(chatterbot_corpus, out_file, ensure_ascii=False)




    @classmethod
    def create_chatterbot(cls):
        """
        用语料训练一个chatbot
        :return:
        """
        cn_chatter = ChatBot("National Lib Chatter",
                             storage_adapter='chatterbot.storage.SQLStorageAdapter',
                             input_adapter='chatterbot.input.TerminalAdapter',
                             output_adapter='chatterbot.output.TerminalAdapter',
                             logic_adapters=[
                                 'chatterbot.logic.BestMatch',
                                 'chatterbot.logic.MathematicalEvaluation',
                             ],
                             database='./db.sqlite3'
        )
        trainer = ChatterBotCorpusTrainer(cn_chatter)
        trainer.train('./kuakua_corpus.json')

        # trainer.export_for_training('./my_export.json')

        return cn_chatter
    @classmethod
    def load_chatterbot(cls):
        """
        加载训练好的bot
        :return:
        """
        cn_chatterbot = ChatBot('National Lib Chatter',
                                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                                input_adapter = 'chatterbot.input.TerminalAdapter',
                                output_adapter = 'chatterbot.output.TerminalAdapter',
                                logic_adapters = [
                                                'chatterbot.logic.BestMatch',
                                                'chatterbot.logic.MathematicalEvaluation',
                                ],
                                database = './db.sqlite3'
        )
        return cn_chatterbot



if __name__ == '__main__':
    # kuakuaChat.corpus_convert()
    # test_chatter = kuakuaChat.create_chatterbot()
    test_chatter = kuakuaChat.load_chatterbot()
    while True:
        try:
            user_input = input('USER:')
            response = test_chatter.get_response(user_input)
            print('BOT:', response)
        # 直到按ctrl-c 或者 ctrl-d 才会退出
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
