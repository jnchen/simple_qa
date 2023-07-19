import configparser

class Config:
    def __init__(self, config='qa.conf'):
        self.config = configparser.ConfigParser()
        self.config.read(config)

    def get_max_length(self):
        return int(self.config['embedding']['max_length'])
    
    def get_embedding_type(self):
        return self.config['embedding']['type']
    
    def get_embedding_model(self):
        return self.config['embedding']['model']
    
    def get_llm_model(self):
        return self.config['llm']['model']
    
    def get_vector_store(self):
        return self.config['store']['vector_db']
    
    def get_content_store(self):
        return self.config['store']['content_db']
    
    def get_open_api_key(self):
        return self.config['openai']['api_key']

    def get_glm_local_cache(self):
        return self.config['glm']['local_cache']
