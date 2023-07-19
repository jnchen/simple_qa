#!/usr/bin/env python
# coding:utf-8

import gradio as gr
import random
import time
from application import QA
import argparse
from config import Config

qa = None

def respond(message, chat_history):
    bot_message = qa.ask(message)
    chat_history.append((message, bot_message))
    time.sleep(1)
    return "", chat_history

with gr.Blocks() as shell:
    chatbot = gr.Chatbot(label="问&答")
    msg = gr.Textbox(label='请输入你的问题')
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    with gr.Row():
        clear = gr.ClearButton([chatbot, msg], scale=3)
        submit = gr.Button('确定', scale=1)
        submit.click(respond, [msg, chatbot], [msg, chatbot])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='qa.conf', help='path to config file')

    args = parser.parse_args()

    qa = QA(args.config)

    conf = Config(args.config)
    
    shell.launch(server_port=conf.get_web_port())
