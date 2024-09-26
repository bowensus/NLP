# 注意:

1. 在配置文件.env中更换你的openai api密钥，openai api密钥不是免费，需要设定支付方式，需要添加一张国外银行卡，并充值最低5美元。

2. langchain中的很多旧版本的方法已被弃用，例如LLMChat，更换为了链式调用 '|'，包括chain.__call__方法的调用，更换为了invoke()，更多细节请查阅langchain官方教程文档

3. main.py为langchain的基本原理，如何通过链的思想完成整个工作流。  
   chat_history.py为langchain如何进行记忆储存和管理，并如何模板将字符串信息转换分解为human message和AI message。session_id为记录索引，这里默认未使用。  
   textloader.py展示了langchain的embedding和chunk过程。  
   chroma.py和prompt.py演示了如何找出于问题相似度最高的文本片段。  


# NOTE:

1. In the `.env` configuration file, replace your OpenAI API key. The OpenAI API key is not free, and you need to set up a payment method by adding a foreign bank card and topping up a minimum of $5.

2. Many older methods in Langchain have been deprecated, such as `LLMChat`, which has been replaced by chain calling using '|'. This includes the `chain.__call__` method, which has been replaced by `invoke()`. For more details, please refer to the official Langchain documentation.

3. The `main.py` file demonstrates the basic principles of Langchain, showing how the concept of chaining can complete entire workflows. 
   `chat_history` shows how Langchain manages memory storage and how a template splits string information into human messages and AI messages. `session_id` records the index, but it's not used by default in this example.
