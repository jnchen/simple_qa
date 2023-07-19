# 本地知识问答系统
## 配置

修改qa.conf下的配置项

## 部署

```bash
pip install -r requirements.txt
```

## 添加知识

```bash
python build.py --type pdf --url xxxx #可以是远程地址和本地文件路径
python build.py --type web --url http://xxxxxx #网页
```

## 启动前端
```bash
python chatshell.py
```

## 包含模块

- parser.py 解析文档
- splitter.py 文本分片
- embedding*.py 词向量生成
- store.py 知识的本地存储
- prompt.py 提示词生成
- llm*.py 回答生成的大语言模型
- config.py 配置解析
- build.py 本地知识维护
- chatshell.py 网页版的前端
- application.py 组织问答系统的各模块