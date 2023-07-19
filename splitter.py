#!/usr/bin/env python
# coding: utf-8

# 主要实现文本的分片

class Splitter:
    def __init__(self, inputs, **options):
        self.chunks = []
        n = len(inputs)
        cur_len = 0
        cur_cache = []
        max_len = options.max_length if hasattr(options, 'max_length') else 4096
        for i in range(n):
            item = inputs[i]
            item_len = len(item)
            if max_len - cur_len > item_len:
                cur_len += item_len
                cur_cache.append(item)
            else:
                cur_len = item_len
                self.chunks.append(''.join(cur_cache))
                cur_cache.clear()

    def get_chunks(self):
        return self.chunks

if __name__ == '__main__':
    input = ['aaa','bbb','ccc','dd','ee']
    spliter = Splitter(input, {'max_length':10})
    content = splitter.get_chunks()
    print(content)