#!/usr/bin/env python
# coding: utf-8

import openai

model_name = 'gpt-3.5-turbo'

class ChatBot:
    def __init__(self, api_key):
        openai.api_key = api_key
    def chat(self, message):
        response = openai.ChatCompletion.create(
            model = model_name,
            messages=[
                {'role':'system', 'content':'你是一个负责文档过滤汇总的老师。'},
                {'role':'user','content': message}
            ]
        )
        return response.choices[0]['message']['content']


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str, help='openai api key')
    args = parser.parse_args()
    chat = ChatBot(args.key)
    print(chat.chat('你好，你叫什么名字'))
