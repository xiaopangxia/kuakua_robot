# -*- coding: utf-8 -*-
# File: sim_kuakua.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-04-3
import os
import sys
import random
from zhcnSegment import zhcnSeg
from sentenceSimilarity import SentenceSimilarity

class kuakuaChat():
    def __init__(self):
        """
        初始化夸夸话题回复表
        """
        self.qa_dict = {}
        self.q_list = []
        with open('./douban_kuakua_topic.txt', 'r', encoding='utf8') as in_file:
            for line in in_file.readlines():
                que = line.split('<######>')[0].strip()
                ans_list = []
                for ans in line.split('<######>')[-1].split('<$$$$$$>'):
                    if len(ans) > 2:
                        ans_list.append(ans)

                if len(que)>5:
                    self.q_list.append(que)
                    self.qa_dict[que] = ans_list

        zhcn_seg = zhcnSeg()
        self.sent_sim = SentenceSimilarity(zhcn_seg)
        self.sent_sim.set_sentences(self.q_list)
        # 默认用tfidf
        self.sent_sim.TfidfModel()


    def answer_question(self, question_str):
        """
        返回与输入问句最相似的问句的固定回答
        :param question_str:
        :return:
        """
        most_sim_questions = self.sent_sim.similarity_top_k(question_str, 4)
        answer_list = []
        for item in most_sim_questions:
            answer = self.qa_dict[item[0]]
            answer_list += answer
        return answer_list



if __name__ == '__main__':
    test_bot = kuakuaChat()
    while True:
        try:
            user_input = input('USER:')
            answer_list = test_bot.answer_question(user_input)
            response = random.choice(answer_list)
            print('BOT:', response)
        # 直到按ctrl-c 或者 ctrl-d 才会退出
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


