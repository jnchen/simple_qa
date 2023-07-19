#!/usr/bin/env python
# coding: utf-8

from sentence_transformers import SentenceTransformer

class Embedding:
    # uer/sbert-base-chinese-nli 和 shibing624/text2vec-base-chinese
    def __init__(self, model_name='uer/sbert-base-chinese-nli'):
        self.model = SentenceTransformer(model_name)

    def encode(self, inputs):
        return self.model.encode(inputs)

if __name__ == '__main__':
    embedding = Embedding()
    vectors = embedding.encode(['我的家在东北','我家大门常打开','我家就在，山上住'])

    print(vectors.shape)