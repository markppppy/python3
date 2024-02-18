[toc]

## 概述

- 背景：大语言模型的能力很大程度上依赖于prompts, 但合适的prompts需要多次手动编写、调整。本文对这个问题提出了一个简单、非参数的解决方案-文本梯度prompt优化算法(ProTeGi).
- 前提：有初始prompt、有一批训练数据和LLM API，（还有三个在优化过程中使用的prompt模板
- 作用：这个算法自动改进prompt 
- 方法：这个算法使用小批量数据形成“梯度”，对当前prompt评判；然后按梯度相反的语义方向编辑prompt；梯度消除的过程由beam search和bandit selection procedure引导，大大提高了算法效率。
- 评估：在四个分类任务(判断仇恨、假新闻、讽刺、越狱)上，通过使用数据将模糊的任务描述改写为更精确的注释指令，这个算法可以超越之前的prompt编辑技术(Monte-Carlo、Reinforcement Learning、AutoGPT)，并将初始prompt的性能提高31%.
- 优点: 没有模型训练的过程，就可以提高prompt的效果；可解释性强；通用性强；
- 缺点：算法效率受LLM接口调用速度的限制，且整个过程需要多次调用，耗时长，通常在1个小时以上，大的prompt spaces或紧急任务不适用；只在分类任务上做了测试。

## 名词解释
Ethos: 英语仇恨言论检测数据集，包含997条网络评论和仇恨言论标签；
Liar：英文假新闻检测数据集，包含4000条语句、上下文和谎言标签
Sarcasm：是一个阿拉伯语讽刺检测数据集，包含10000条在线评论和讽刺标签

## 案例 
- ProTeGi概述 
![ProTeGi概述](../pics/Overview%20of%20the%20proposed%20Prompt%20Optimization%20with%20Textual%20Gradients%20(ProTeGi).jpg)

- 流程图
![the text dialogue tree](../pics/Figure%202.jpg)

- 代码解析
prompt 0: ethos.md
data: 998条文本和是否是仇恨言论的标签
把data分成训练集和测试集

循环指定次数执行如下步骤：
1. 扩展prompt  p0
   1. 从训练集随机抽取若干条数据 minibatch
   2. 对每个prompt循环: 
      1. 从 minibatch 取100条和第一个prompt组成问题让gpt返回 是或否
      2. 返回100训练数据，真实标签，预测标签
      3. 获取梯度: 从预测错误的样本中取4个，组成一个包含text、预测标签和实际标签的字符串error_str，和prompt组成问题让gpt给出若干原因，把每个原因和字符串凑一对放入列表
      4. 应用梯度：把prompt和error_str和每个原因依次发给gpt，让其返回一个新的prompt
      5. 生成同义词: 把当前prompt和新的prompts，让gpt生成若干个同义prompt
      6. 合并梯度和同义生成的prompts，总数不多于设置的值

2. 对prompts排序并取排名前n的prompt   ucb
   1. 对候选prompts采样m, 对训练数据随机抽取n
   2. 组成 m*n 个问题, 问gpt返回是和否, 对照label，计算出正确率
   3. 上述过程循环若干次计算出每个prompt的分值
   4. 按分值给prompt排序并取前若干个

3. 记录选取的prompts和其评估的分和真实的分: 
   1. 把prompt和测试数据组合，推理，并计算f1


## 翻译
Note that all prompts p are drawn from the space of coherent natural language L
请注意，所有提示 p 都是从连贯自然语言 L 的空间中提取的

returns a likely text continuation y of the prompt formed by concatenating p and x
返回通过连接 p 和 x 形成的提示的可能文本延续 y

for example, few-shot prompt and input example, or chatbot persona and conversational history
例如，小样本提示和输入示例，或聊天机器人角色和对话历史记录

## 参考
- [原文](https://arxiv.org/pdf/2305.03495)