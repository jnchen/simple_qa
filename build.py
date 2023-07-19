#!/usr/bin/env python
# coding:utf-8

import argparse
from application import QA


# 主要负责加入新的本地知识

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--type', type=str, help='type for the document')
    arg_parser.add_argument('--url', type=str, help='the address of the document')

    args = arg_parser.parse_args()

    app = QA(build_mode=True)
    app.add_resource(args.type, args.url)
