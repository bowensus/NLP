# 注意:

* 在配置文件.env中更换你的openai api密钥，openai api密钥不是免费，需要设定支付方式，需要添加一张国外银行卡，并充值最低5美元。
* langchain中的很多旧版本的方法已被弃用，例如LLMChat，更换为了链式调用 '|'，包括chain.__call__方法的调用，更换为了invoke()，更多细节请查阅langchain官方教程文档
* langchain-1为langchain的部分基本方法使用，完成相应的基本任务。
* agent为构建一个完整的智能体
