#!/usr/bin/env python
# coding: utf-8

import faiss
import os
import pickle

# 向量的存储与查询

class Store:
    def __init__(self, embedding, vector_path, content_path):
        self.embedding = embedding
        
        self.vector_file_path = os.path.join(vector_path, 'vectors')
        self.content_file_path = os.path.join(content_path, 'contents')

        if not os.path.exists(vector_path):
            os.makedirs(vector_path)
        if not os.path.exists(content_path):
            os.makedirs(content_path)

        if os.path.exists(self.vector_file_path):
            self.vectors = faiss.read_index(self.vector_file_path)
            print(f'Loaded {self.vectors.ntotal} vectors.')
        else:
            # 设置量化器建立检索空间
            self.vectors = faiss.IndexFlatL2(768)
            print(f'Does not detected the old vectors, create a new one.')

        if os.path.exists(self.content_file_path):
            with open(self.content_file_path, 'rb') as f:
                self.contents = pickle.load(f)
            print(f'Loaded {len(self.contents)} contents.')
        else:
            self.contents = []
            print(f'Dose not detected the old contents, create a new one.')

    def store(self, inputs):
        # acquire a word embedding
        input_word_embeddings = self.embedding.encode(inputs)
        
        # add vectors to vector database
        if not self.vectors.is_trained:
            self.vectors.train(input_word_embeddings)
        self.vectors.add(input_word_embeddings)

        # add content to content list
        self.contents.extend(inputs)

        # if vector size greater than 100, translate to a IVFFlat
        # if self.vectors.ntotal > 100:
        #     self.vectors = faiss.IndexIVFFlat(self.vectors, 768, 100)

        # save faiss index to file
        faiss.write_index(self.vectors, self.vector_file_path)
        # save content list to file
        with open(self.content_file_path, 'wb+') as f:
            pickle.dump(self.contents, f)
        
        return True

    def query(self, query, topn):
        # acquire the query embedding
        query_id = self.embedding.encode([query])
        # query relative content's vector 
        _, i = self.vectors.search(query_id, topn)
        indexes = i[0]
        print('Searched the indexs', indexes)
        # fetch the content
        result = []
        for i in indexes:
            if -1 == i:
                continue
            result.append(self.contents[i])
        return result
