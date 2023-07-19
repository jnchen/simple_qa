#!/usr/bin/env python
# coding: utf-8

# 主要负责生成句子嵌入

# 对比 bert-base-chinese 

from transformers import AutoModel, AutoTokenizer

import torch
import numpy as np

class MyDataset(torch.utils.data.Dataset):
    def __init__(self,datas):
        self.data = datas
    def __getitem__(self, idx):
        return self.data[idx]
    def __len__(self):
        return len(self.data)


class Embedding:
    # uer/sbert-base-chinese-nli 和 shibing624/text2vec-base-chinese
    def __init__(self, device, model_name = 'bert-base-chinese'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.device = device if device else torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)

    def encode(self, inputs):
        self.model.eval()
        dataset = MyDataset(inputs)
        data_loader = torch.utils.data.DataLoader(dataset, 30)
        vectors = np.ndarray((0, 768), dtype='float32')
        for batch in data_loader:
            inputs = self.tokenizer.batch_encode_plus(batch, truncation=True, return_tensors='pt', padding=True)
            inputs = inputs.to(self.device)
            with torch.no_grad():
                rfet = self.model(**inputs)
                vectors = np.concatenate([vectors, rfet[1].cpu().detach().numpy()], axis = 0)
        return vectors

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    embedding = Embedding(device=device)
    vectors = embedding.encode(['我的家在东北','我家大门常打开','我家就在，山上住'])

    print(vectors.shape)


