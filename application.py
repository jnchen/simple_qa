#!/usr/bin/env python
# coding: utf-8

# 编写一个类合并所有的逻辑
from config import Config
from parser import Parser
from splitter import Splitter
from store import Store


class QA:
    def __init__(self, config='qa.conf', build_mode=False):
        conf = Config(config)

        self.max_embedding_length = conf.get_max_length()
        
        if not conf.get_embedding_type() or conf.get_embedding_type() == 'sentence_transformers':
            from embedding_sentence import Embedding
            self.embedding = Embedding('shibing624/text2vec-base-chinese' if not conf.get_embedding_model() else conf.get_embedding_model())
        elif conf.get_embedding_type() == 'transformers':
            from embedding_transformers import Embedding
            self.embedding = Embedding()

        self.vector_store_path = conf.get_vector_store() if conf.get_vector_store() else './db'
        print(f'Prepare Load the vector from {self.vector_store_path}.')
        
        self.content_store_path = conf.get_content_store() if conf.get_content_store() else './db'
        print(f'Prepare Load the content from {self.content_store_path}.')

        if build_mode:
            return

            
        self.llm_model = conf.get_llm_model() if conf.get_llm_model() else 'chatglm2-6b'

        if self.llm_model == 'chatglm2-6b':
            from llm_chatglm import ChatBot
            cache = conf.get_glm_local_cache()
            if cache:
                self.llm = ChatBot(cache)
            else:
                self.llm = ChatBot()
        else:
            from llm_chatgpt import ChatBot
            self.llm = ChatBot(conf.get_open_api_key())

        print(f'~ QA system is ready ~')

    def add_resource(self, type, url):
        parser = Parser(type, url)
        contents = parser.get_contents()
        splitter = Splitter(contents, max_length=2500)
        chunks = splitter.get_chunks()

        store = Store(self.embedding, self.vector_store_path, self.content_store_path)
        store.store(chunks)
        
    def ask(self, question):
        from prompt import Prompt
        # query similarity prompt
        store = Store(self.embedding, self.vector_store_path, self.content_store_path)
        relative_content = store.query(question, 3)

        # tempalate fil
        promptor = Prompt(self.llm_model)
        prompt_msg = promptor.build(relative_content, question)

        # send to the llm
        return self.llm.chat(prompt_msg)

if __name__ == '__main__':
    qa = QA()
    resp = qa.ask('xxxx')
    print(resp)
