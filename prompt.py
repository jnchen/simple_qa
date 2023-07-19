#!/usr/bin/env python
# coding: utf-8

# 主要生成提示词

chatglm_template = '已知信息:\n {}\n 根据已知信息回答问题:\n {}'

class Prompt:
    def __init__(self, llm):
        self.llm = llm

    def build(self, content, query):
        if isinstance(content, list):
            content = '\n'.join(content)
        if self.llm == 'chatglm2-6b':
            return chatglm_template.format(content, query)