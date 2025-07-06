[toc]
## 概述
- 工作方法
  - 收集数据
  - 产生想法
  - 把想法转换为模型
  - 在历史数据上验证  回测
  - 验证鲁棒性 稳定性

- alpha是什么 
  - 是一个表达式，计算的是第二天的买入和卖出值

- data 
  - 基本面数据表: Balance sheet , income statement, cash flow statement 
  - frequency 数据更新频率
  - data fields  字段
    - open 当天开盘价 close 当天收盘价 high 当天最高价 low 当天最低价 vwap 已成交量的加权平均价格 adv20 过去20天的平均成交量 
  - 数据类型: Matrix, Vector, Group, Universe 平台自定义的，只在Brain这个平台是这样的含义 
    - Matrix 二维数据
    - Vector 三维数据, 使用时需要用 vector operators(e.g. vec_choose) 把数据类型变为 Matrix 

- operator
## BRAIN 页面模块介绍

### BRAIN页面结果解读
- PnL profit and loss 利润和损失的图表
- IS OS 
  - IS in sample 样本内
  - OS out sample 样本外 
- IS Summary 汇总了关键指标
  - Sharpe 
    - 风险调整后的收益 越高越好 表示 赚钱稳不稳定
    - = Avg. Annualized Returns / Annualized Std. Dev. of Returns  (平均年化回报 / 标准年化回报)
  - Turnover  周转率
    - alpha 每天交易的资本的百分比 
    - = Value Traded / Value Held (交易价值 / 持有价值)
  - Fitness 
    - 一个综合了 returns, turnover and Sharpe 的函数 越高越好 
    - = Sharpe * Sqrt(Abs(Returns)) / Max(Turnover,0.125) 
  - Returns 
    - 利润
    - 因为假设的是一个多空投资组合，所以总投资金额为账面金额的一半 
  - Drawdown 
    - 表示回溯测试中任意一年发生的最大损失百分比 
    - return-to-drawdown ratio (回报回撤比率) 最好大于1，越高越证明 alpha 越好 
  - Margin 
    - 表示相对于交易金额获得的盈亏 ， 单位是 万分之一(基点)  
    - 总盈亏除以交易金额

### 输入表达式(即 alpha)后，平台做了什么
1. Expression Calculation 把每个股票代入表达式计算  股票范围和时间范围可以设置吗？
2. Market Neutralization 市场中性化
   - 消除特定因素对alpha的影响，只持有一些股票的多头头寸有很高的风险，所以在BRAIN假设建立的是一个多空投资组合，一半多头头寸，一半空头头寸
   - 做法  1，2 数据中心化  3，4 权重标准化 5，6 分配资本
     1. 计算每个股票在某一天alpha的值，得到一组数组L1，然后计算平均值M；
     2. 每个股票的alpha值减去平均值，得到一组数字L2；
     3. 将L2中每个值的绝对值求和得到S；
     4. 用L2中的每个值除以S，得到一组数字L3；
     5. 假设资本是20Mn=两千万，L3中每个数字乘以资本得到L4;  会有两千万的买入和卖出
     6. 获取第二天每个股票的回报百分比，得到一组数字R，R*L4 得到每个股票的盈亏（PnL）

### Simulate settings 含义
- Neutralization

- Decay 衰变 
  - 大概明白是 设置权重时要参考历史多天的权重值，然后按 Decay_linear(x,n)=(x[date]∗n+x[date−1]∗(n−1)+…+x[date−n−1]*1)/(n+(n−1)+…+1) 计算最终权重
  - Decay会削减信号强度，因为会让当前 alpha 影响变小；通常 Decay的值小于10 

## 如何让整体的alpha质量更高以及不该做的事情
- 如何让整体的alpha质量更高
  - 高质量的alpha: 在样本内和样本外增长速度几乎一致  consistency 
  - 如何让整体的alpha质量更高: 多尝试不同的思路，找到高质量alpha, 尽可能多的提交高质量alpha 
- 不该做的事情 
  - 不要在alpha限制特殊年份
  - 自相关性高于0.7的 alpha 
  - 不要花太多的时间调整alpha中的参数/设置，使alpha可以提交 
  - 不要基于已提交的alpha,增加一些噪音降低相关性使alpha可以提交 

## 管理回测过的Alpha


## 相关名词解释 
- Position 头寸 （资金，所有可以运用的资金总和） ，包括 long positions 多头头寸 和 short positions 空头头寸 


## 待办
- 把day1的代码单独拿出来并跑一下
- 字段 anl4_cff_flag 更新频率  

## 学习资料

《零基础学量化》录播课，解锁密码 BRAIN2024
[第一课](https://v.youku.com/v_show/id_XNjQ0NTQwMzU3Mg==.html?spm=a2hcb.playlist.page.9&playMode=pugv)
[第二课](https://v.youku.com/v_show/id_XNjQ1Mjg5Mzk4NA==.html?spm=a2hcb.playlist.page.9&playMode=pugv)
[第三课](https://v.youku.com/v_show/id_XNjQ1MjkwMDEwMA==.html?spm=a2hcb.playlist.page.9&playMode=pugv)
[第四课](https://v.youku.com/v_show/id_XNjQ0NTQwMjA5Ng==.html)

录播课例子中CHN市场目前已经不对用户阶段开放。
学习完录播课并完成顾问申请流程后，可正常参与后续线下顾问课程。
学习过程中BRAIN相关问题可以私信“BRAIN智能助手” 公众号快速得到解答。
整个过程中请及时关注邮箱查收通知和资料，有疑问请邮件至中国区官邮mainlandchina@worldquantbrain.com
询问，回复通常需要一两天时间。
