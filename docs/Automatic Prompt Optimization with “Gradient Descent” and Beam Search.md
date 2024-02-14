[toc]

## 概述

- 背景：大语言模型的能力很大程度上依赖于prompts, 但合适的prompts需要多次手动编写、调整。本文对这个问题提出了一个简单、非参数的解决方案-文本梯度prompt优化算法(ProTeGi).
- 前提：有训练数据和LLM API
- 作用：这个算法自动改进prompt，优化过程可解释
- 方法：这个算法使用小批量数据形成“梯度”，对当前prompt评判；然后按梯度相反的语义方向编辑prompt；梯度消除的过程由beam search和bandit selection procedure引导，大大提高了算法效率。
- 评估：在三个NLP和LLM jailbreak上表明，通过使用数据将模糊的任务描述改写为更精确的注释指令，APO可以超越之前的prompt编辑技术，并将初始prompt的性能提高31%.

## 名词解释
梯度: 使用训练数据的小批量生成，对当前prompt缺陷的描述
Ethos: 英语仇恨言论检测数据集，包含997条网络评论和仇恨言论标签；
Liar：英文假新闻检测数据集，包含4000条语句、上下文和谎言标签
Sarcasm：是一个阿拉伯语讽刺检测数据集，包含10000条在线评论和讽刺标签

## 分段内容
2. 利用非参数梯度下降，离散提示优化
算法假定可以访问初始的prompt p0和独立同分布的训练数据，训练数据由成对的输入和输出组成
LLM API 返回一个文本y，y是prompt的延续文本，y? 由候选的 prompts 和 x 组成
这个算法会迭代的细化p0，产生p^，一个最佳提示的近似值，对于某些指标函数和域内测试或开发数据
- 这个算法怎么执行文本梯度下降，以定向方式改进提示  2.1 
包括这些过程：1. 在一批数据上评估prompt 2. 创建一个本地的loss signal即梯度，包含如何提升当前prompt 3. 在下次迭代之前，沿相反语义方向编辑prompt
  - 
- 然后这个算法利用这些梯度下降步骤在连贯语言空间L中进行 beam search，在beam expansion过程中以梯度为导向，在beam selection过程中有效识别最佳 arm  2.2  
## 翻译
Note that all prompts p are drawn from the space of coherent natural language L
请注意，所有提示 p 都是从连贯自然语言 L 的空间中提取的

returns a likely text continuation y of the prompt formed by concatenating p and x
返回通过连接 p 和 x 形成的提示的可能文本延续 y

for example, few-shot prompt and input example, or chatbot persona and conversational history
例如，小样本提示和输入示例，或聊天机器人角色和对话历史记录

## 参考
- [原文](https://arxiv.org/pdf/2305.03495)