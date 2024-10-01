# 文件说明:


* main.py为langchain的基本原理，如何通过链的思想完成整个工作流。  
* chat_history.py为langchain如何进行记忆储存和管理，并如何模板将字符串信息转换分解为human message和AI message。session_id为记录索引，这里默认未使用。  
* textloader.py展示了langchain的embedding和chunk过程。  
* chroma.py演示了如何找出于问题相似度最高的文本片段。  
* prompt.py为如何在检索相似度片段时去除重复添加文本的解决方案
