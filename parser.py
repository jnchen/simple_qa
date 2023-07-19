#!/usr/bin/env python
# coding: utf-8

import fitz
import requests
from bs4 import BeautifulSoup
import re
# 主要实现文本的解析读取

splitters = ['.', '。', '?', '？', '!', '！']

'''
通过多个分隔符切分文本
'''
def multi_split(str):
    return re.split('|'.join(map(re.escape, splitters)), str)

'''
解析pdf文件
'''
def parse_pdf(path):
    sentences = []
    doc = fitz.open(path)
    for page in doc:
        cur_content = page.get_text()
        cur_content = cur_content.replace('\r\n', '')
        cur_content = cur_content.replace('\n', '')
        cur_contents = multi_split(cur_content)
        result_content = list(filter(lambda x: len(x) > 1, cur_contents))
        sentences.extend(result_content)
    return sentences

'''
解析网页内容
'''
def parse_web(url):
    sentences = []
    resp = requests.get(url)
    bs = BeautifulSoup(resp.content)
    contents = bs.text
    contents = contents.replace('\r\n', '')
    contents = contents.replace('\n', '')
    contents = multi_split(contents)
    result_contents = list(filter(lambda x: len(x) > 1, contents))
    sentences.extend(result_contents)
    return sentences

class Parser:
    def __init__(self, type, path):
        print(f'Receive the Resource {path} of {type}.')
        if type == 'pdf':
            self.data = parse_pdf(path)
        elif type == 'web':
            self.data = parse_web(path)
        else:
            print(f'The type {type} was not supported.')
            exit(0)

    def get_contents(self):
        return self.data

if __name__ == '__main__':
    path = 'C:/Users/caoji/Downloads/Documents/tlcl-cn.pdf'
    parser = Parser('pdf', path)
    contents = parser.get_contents()
    print(contents)
    url = 'http://c.biancheng.net/python_spider/bs4.html'
    parser = Parser('web', url)
    contents = parser.get_contents()
    print(contents)