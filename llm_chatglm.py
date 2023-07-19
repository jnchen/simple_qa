#!/usr/bin/env python
# coding: utf-8

from transformers import AutoModel, AutoTokenizer


class ChatBot:
    def __init__(self, model_name='THUDM/chatglm2-6b'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(model_name, trust_remote_code=True).half().cuda()

    def chat(self, message):
        resp, history = self.model.chat(self.tokenizer, message, history=[])
        return resp



if __name__ == '__main__':
    model_name = '../chatglm2-6b'
    chat = ChatBot(model_name)
    print(chat.chat('你好，你叫什么名字'))
