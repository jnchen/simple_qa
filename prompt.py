#!/usr/bin/env python
# coding: utf-8

# 主要生成提示词

chatglm_template = '已知信息:\n {}\n 根据已知信息回答问题:\n {}'
chatgpt_template = '已知信息:\n {}\n 请根据已知信息回答问题,不要回答已经信息中没有的内容，问题是:\n {}'

class Prompt:
    def __init__(self, llm):
        self.llm = llm

    def build(self, content, query):
        if self.llm == 'chatglm2-6b':
            if isinstance(content, list):
                content = '\n'.join(content)
            return chatglm_template.format(content, query)
        elif self.llm == 'chatgpt':
            # chatgpt的token宽度只有4096,只取top1
            if isinstance(content, list):
                content = content[0]
            return chatgpt_template.format(content, query)
