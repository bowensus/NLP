# 注意:

** 在配置文件.env中更换你的openai api密钥，openai api密钥不是免费，需要设定支付方式，需要添加一张国外银行卡，并充值最低5美元。
** langchain中的很多旧版本的方法已被弃用，例如LLMChat，更换为了链式调用 '|'，包括chain.__call__方法的调用，更换为了invoke()，更多细节请查阅langchain官方教程文档
** main.py为langchain的基本原理，如何通过链的思想完成整个工作流。  
   chat_history.py为langchain如何进行记忆储存和管理，并如何模板将字符串信息转换分解为human message和AI message。session_id为记录索引，这里默认未使用。  
   textloader.py展示了langchain的embedding和chunk过程。  
   chroma.py和prompt.py演示了如何找出于问题相似度最高的文本片段。  
