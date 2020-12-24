

[TOC]

# Python

## 基础知识

### 基本数据类型

数值、字符串、布尔类型（True，False）、空值（None）

#### 数值类型

​       1）整数，没有取值范围限制；pow(x,y)表示x的y次方；提供四种进制表示形式（二进制，0b或0B开头；八进制，0o或0O开头；十进制；十六进制，0x或0X开头）

​       2）浮点数，取值范围和精度基本无限制；浮点数间运算存在不确定尾数，可以用round(x,d)解决；科学记数法表示（4.3e-3表示0.0043，4.3E3表示4300.0）；

​       3）复数，a + bj（j = $\sqrt{-1}$ ），其中a是实部，b是虚部；

​       4）运算操作符，x / y 是浮点数结果，x // y是整除；x % y取余；x ** y表示x的y次幂；

​       5）增强赋值操作符，x op = y，如：x += y；

​       6）不同数值类型间运算，结果与最宽泛的数值类型一致，由窄到宽依次是：整数，浮点数，复数；

​       7）数值运算函数，abs(x) 绝对值；

​                                        divmod(x,y)商余，表示(x//y, x%y)；

​                                        pow(x, y[, z])幂余，表示：(x**y)%z；

​                                        round(x[,d])四舍五入，d表示保留小数位，默认取整；

​                                        max(x~1~,...,x~n~)；min(x~1~,...,x~n~)；

（类型转换，适应于字符串）   int(x)；float(x)；complex(x)将实数变为复数，增加虚部为0的虚数部分；

#### 字符串类型

定义：单引号，双引号，三单引号或三双引号；

>字符串的使用：

​        1）获取，通过==索引==获取<字符串>[索引]，第一个字符的索引为0；通过==切片==获取一段字符串，<字符串>[M:N];

​        2）切片的高级使用，<字符串>[M:N:K]，当K为-1时，表示将字符串逆序；

​        3）转义符 \，一是用来表示特定字符的本意；二是形成一些组合，表示一些不可打印的含义，如：\n 换行，\b 回退，\r 回车，光标移动到当前行行首；

​        4）字符串操作符，x + y 连接；n * x或x * n表示复制n次字符串x；x in s判断x是否是s的字串，返回True或False；

​        5）字符串处理函数，eval(x)，可以去掉字符串两边的引号，将其转换为数字；

​                                             str(x)将任意类型的x转换为字符串形式；

​                                             len(x)，python程序中汉字和字母长度都为1； 

​                                             hen(x)或oct(x)，将十进制整数x转换为x的十六进制或八进制小写形式的字符串；             

​                                             chr(u)，u为Unicode编码，返回其对应的字符；

​                                             ord(x)，x为字符，返回其对应的Unicode编码；

​        6）常用的字符串方法，str.lower() or .upper()；

​                                                  str.split(sep)，返回一个str被sep字符分割后的列表；

​                                                  str.count(sub)，返回子串sub在str中出现的次数；

​                                                  str.replace(old,new)，将old子串替换为new后，返回新字符串；

​                                                  str.center(width[,fillchar])，字符串str根据宽度width居中，两侧用fillchar填充；

​                                                  str.strip(chars)，去掉str两侧的chars中包含的字符；

​                                                  str.join(iter)，在iter变量中每个字符间插入str；                                             

​        7）字符串类型的格式化，用法：<模板字符串>.format(<逗号分割的参数>)，模板字符串中多个槽位{}用逗号隔开；

![TIM截图20190609135633](http://ws1.sinaimg.cn/large/83fd1fc9ly1g3uv3r8mx5j20ms080429.jpg)

整数类型b表示二进制，c表示Unicode编码，d表示十进制，o表示八进制，x表示小写的十六进制；

### 程序的控制结构

程序的分支结构，程序的循环结构

#### 程序的分支结构

单分支、二分支和多分枝结构，程序的异常处理

1）单分支结构 

​              if <条件>:

​                 <语句块>

2）二分支结构

形式一:   if <条件>:

​                  <语句块>

​               else :

​                 <语句块>

形式二：<表达式1> if <条件> else <表达式2>

3）多分支结构

​              if <条件>:

​                 <语句块>

​              elif :

​                 <语句块>

​              ...

​              else :

​                  <语句块>

4）程序的异常处理

try :

​    <语句块1>

except [<自定义异常名称>] :

​    <语句块2>

[else :]

​    <语句块3>

[finally :]

​    <语句块4>

else中的语句块在没有发生异常时执行；

finally中的语句块一定会执行；

关键字 pass；

#### 程序的循环结构

遍历循环、无限循环、循环控制保留字、循环的高级用法

1）遍历循环

for <循环变量> in <遍历结构> :

​    <语句块>

从遍历结构中逐一提取元素，放在循环变量中；

如：for str in "abc"

​            print(str, end=",")

2）无限循环

while <条件> :

​    <语句块>

3）循环控制保留字 break、continue

4）循环的高级用法

for <循环变量> in <遍历结构> :

​    <语句块>

else :

​    <语句块>

在for或while中搭配else，执行else语句块作为对循环没有被break中断的奖励；

### 函数和代码复用

函数的定义和使用、代码的复用与函数递归

#### 函数的定义和使用

1）函数的定义

def <函数名>(<0个或多个传入的==参数==，用逗号隔开>):

​    <函数体>

​    [return <返回值>]

参数：可选参数，在定义时给定默认值，可选参数要放在后面；可变参数，在定义时不确定参数的数量，用*参数名表示；

函数可以返回0个或多个结果，用逗号分割；

2）参数的传递

函数调用时，可以通过位置或名称的方式传递参数；

3）在函数中使用全局变量可以在变量前加global关键字；

4）lambda函数

定义：<函数名> = lambda <参数>: <表达式>

如：f = lambda x, y: x + y

调用：f(2, 3)

使用场景：主要用作一些特定函数或方法的参数；有一些固定的使用场景，定义函数尽量用def；

#### 代码的复用与函数递归

递归的实现：函数 + 分支语句；递归本身是一个函数；递归函数内部采用分支语句对输入进行判断，对基例和链条编写对应的代码；

#### class和def的区别

Class有点像是将多个函数进行功能性封装

#### python类方法中的self

1、self是在类的方法中必须有的，独立的函数或方法是不必带有self的



### 组合数据类型

集合、序列(字符串、元组和列表)、字典类型及操作

#### 集合

定义：多个元素的无序组合；用大括号{}或set()定义，包含{}中元素用逗号隔开，空集合定义必须用set()；

特点：无序；每个元素唯一，且为不可变元素；

集合操作符：

​        1）S | T 并集；S - T 差集，表示在S且不在T中的元素；S & T 交集；S ^ T 对称差集，表示S和T中不相同的元素；

​        2）<,=,>=,<= 表示集合间的包含关系；

​        3）增强操作符，如：S |= T 取并集，更新集合S；

集合的处理方法：S.add(x) 增加；

​                               S.discard(x) 移除集合S中的x，若x不在S中不报错；

​                               S.remove(x) 移除集合S中的x，若x不在S中报错（KeyError异常）；

​                               S.clear() 清除集合中的元素；

​                               S.pop() 随机取出集合S中的一个元素，并在S中删除该元素，若S为空，报KeyError异常；

​                               S.copy()；len(S)；x in S；x not in S；set(x)；

#### 序列

定义：序列是一组有序的元素集合，是一种基类数据类型，常用的是其衍生类型，有：字符串，元组，列表；

序列通用操作符：in, not in, +, *, s[i] 索引, s[i: j]或s[i: j: k] 切片；

序列通用函数和方法：len(s), min(s) 若包含不同类型元素会报错, max(s) 同min, s.index(x) 或 s.index(x, i, j) 返回从i到j第一次出现x的位置，s.count(x)；

1）元组

定义：使用小括号()或tuple()，元素间用逗号分割；定义时也可以省略小括号；元组创建后不能被修改；

2）列表

定义：使用方括号[]或list()创建，元素间用逗号分割；列表中的元素可以修改；

列表操作函数和方法：ls[i] = x, ls[i: j: k] = lt, del ls[i], del ls[i: j: k], ls += lt, ls *= n 复制ls中的元素n次，并更新ls；

​                                      .append(x) 将x中的一个或多个元素当作一个对象追加到list, .extend(x) 将x中的每个元素当作一个对象追加到list, .clear(), 

​                                      .copy() 复制成新列表（id()不同），但如果原列表中包含元素列表A，则新列表的元素A指向之前的对象，此时完全复制要用copy包中的.deepcopy(),

​                                      .insert(i, x), .pop(i), .remove(x) 删除第一个出现的x, .reserse() 反转列表中的元素；

#### 字典

定义：字典是键值对的集合，键值对之间无序；键可以视为索引的扩展；使用{}和dict()创建，键值用冒号:隔开，键值对用逗号隔开；

字典类型的操作函数和方法：d[key1] = value1 向字典中增加元素,

​                                                  del d[k], k in d 判断键k是否包含在字典中, 

​                                                  d.keys() 返回字典d中所有的键信息，返回的是dict_keys类型，可以遍历，不能当作列表操作, 

​                                                  d.values() 返回的是dict_keys类型, d.items(), 

​                                                  d.get(k, <default>), d.pop(k, <default>),

​                                                  d.popitem() 随机取出一个键值对，以元组形式返回, 

​                                                  d.clear() 

### 文件和数据格式化

文件的使用，一维和二维数据的格式化和处理

文件的使用

1）文件类型，文本文件（由某一特定编码组成）和二进制文件（由0，1组成，如：.png，.avi等）；任何文件都可以用二进制形式打开；

2）文件的打开和关闭

文件的打开：<变量名> = open(<文件名>, <打开模式>[ ,encoding = 'utf8'])

打开模式：'r' 只读，'w' 覆盖写，'x' 创建写，若文件已存在会报错，'a' 追加写，

​                   'b' 以二进制形式打开文件，'t' 以文本形式打开文件，'+' 与r/w/a/x一起使用，使同时具备读写能力；

文件关闭：<变量名>.close()

3）文件内容的读取

<f>.read(size=-1) 读取全部内容，若给出参数，读入前size长度内容；

<f>.readline(size=-1) 读入一行内容，若给出参数，读入该行前size长度内容；

<f>.readlines(hint=-1) 读入文件所有行，以每行为元素形成列表，若给出参数，读入前hint行内容；

\# 逐行读入逐行处理

fo = open(fname, 'r')

for line in fo:

​    print(line)

fo.close()

4）数据文件的写入

<f>.write(s) 向文件中写入一个字符串

<f>.writelines(lines) 将一个元素全为字符串的==列表==写入文件

<f>.seek(offset) 改变当前文件操作指针的位置，0表示开头，1表示当前位置，2表示文件结尾

\# seek的使用场景之一

fo = open(fname, 'w+')

ls = ["2", "厉害", "中国"]

fo.writelines(ls) 

fo.seek(0)  # 需要调整指针位置才能读出内容

for line in fo:

​    print(line)

fo.close()

#### 一维数据的格式化和处理

数据组织的维度，一维数据的表示，一维数据的存储，一维数据的处理

1）数据组织的维度，一维数据（如：字符串，列表等），二位数据（如：表格），高维数据

数据的操作周期：存储（存储格式） <-> 表示（数据类型） <-> 操作（操作方式）

2）一维数据的表示，如果数据之间有序，可以使用列表；如果无序，可以使用集合；

3）一维数据的存储

方式一：空格（或其他符号）分隔，不换行，但数据不能存在空格（或其他符号）；

4）一维数据的处理 如何以指定数据类型操作数据

#### 二维数据的格式化和处理

1）二维数据的表示 如：列表中存储列表，两层for循环

2）二维数据的存储

3）二维数据的处理

### 程序设计方法学

Python程序设计思维、第三方库的安装

#### Python程序设计思维

计算思维与程序设计（重视构造和过程）、计算生态与Python语言、用户体验与软件产品、基本的程序设计模式



#### 第三方库安装

Python第三方库网址：https://pypi.org/

安装的三种方法：

1）pip（需要联网）

pip -h 帮助；pip install <第三方库名> 安装；pip install -U <第三方库名> 更新；pip unstall <第三方库名> 卸载；pip download <第三方库名> 下载但不安装；pip show <第三方库名> 列出第三方库的详细信息；pip search <关键词> 在名称和介绍中搜索第三方库；pip list 列出已安装的第三方库；

2）集成安装

Anaconda

3）文件安装

某些第三方库只能下载，不能直接安装，因为需要先编译；

网址：http://www.Ifd.uci.edu/~gohlke/pythonlibs/

UCI页面提供了windows系统可以下载，但需要编译后在安装的所有编译后的第三方库；

在该页面下载对应版本库后，使用命令pip install <文件名> 来安装；



## Python数据分析与展示

主要学习数据的清洗、统计和展示；

主要内容：numpy、Matplotlib、Pandas库的学习，若干案例（一、图像的手绘效果，二、引力波的绘制，三、房价趋势的关联因素分析，四、股票数据的趋势分析曲线）和一个项目；

学习目标：从一组数据中提取数据特征，形成基本统计（如：排序），分布/累计统计，数据特征（相关性、周期性等），数据挖掘等；

### NumPy：科学计算工具

数据的维度：一维数据（可以用列表和集合表示）、二维数据（列表）、多维数据（列表）和高维数据（字典或数据表示格式，如：JSON,XML,YAML等）；

​        NumPy提供了一个N维数组对象ndarray，也可以叫数组；数组中一般要求所有元素数据类型相同，若元素数据类型不一样，每个元素的类型会转化为object，叫非同质对象，非同质对象无法发挥numpy优势，应避免；

使用：import numpy as np;

a = np.array([...])  .array()生成一个ndarray数组，array是ndarray在程序中的别名，输出成[]形式，元素由空格分隔；轴(axis)：保存数据的维度，序数，从0开始；秩(rank)：轴的数量；支持bool及若干数值类型(基于C++语言)；

ndarray对象的属性：.ndim 秩，即维度的数量；

​                                     .shape ndarray对象的尺度，如矩阵的n行m列；

​                                     .size 对象中元素的个数，如矩阵的n*m；

​                                     .dtype 对象元素的类型；

​                                     .itemsize 对象中每个元素的大小，以字节为单位；

​                                     .data 返回ndarray在内存中的位置，唯一；

创建ndarray数组(除了arange，大部分生成的数据类型为浮点型)：

​     1）从列表类型、元组类型、列表与元组混合类型，如：x = np.array(\[\[1,2,3],(4,7,9)][, dtype=np.float16])，但是元组和列表包含的数组个数要相同；

​     2）使用numpy中的函数创建ndarray数组，

​     有：np.arange([m, ]n[, k]) 元素从0到n-1，

​       .ones(shape) 根据shape生成一个全为1的数组，shape是==元组类型==，

​       .zeros(shape)，

​       .full(shape, val) 每个元素都为val，

​       .eye(n) n*n的单位矩阵(对角线元素为1，其他为0),

​       .ones_like(a) 根据数组a的形状生成一个全1数组，.zeros_like(a)，.full_like(a, val)，

​       .resize(array, shape) 可以在array的元素范围内生成一个shape形状的新数组，

​       .linspace(m, n, k\[, endpoint=True][, retstep=False]) 根据起止数据m,n等间距地填充k个数据，若不包含最后一个元素n，则多分一份，如np.linspace(1, 10, 4, endpoint=False) => array([1., 3.25, 5.5, 7.75]); retstep=True返回的是元组，第一个元素是生成的数组，第二个元素是步长；

​       .concatenate() 将两个或多个数组合并成一个新数组（保留原维度，纵向合成），如：np.concatenate((a, b))；

ndarray数组的变换：（维度变换、元素类型变换）

​        维度变换：.reshape(shape) 不改变数组元素，返回一个新的shape形状的数组；

​                           .resize(shape) 同reshape，但改变的是原数组；

​                           .swapaxes(ax1, ax2) 将数组n个维度中两个维度进行调换，返回新数组；==？==

​                           .flatten() 将数组降维，返回一个新的一维数组；

​        元素类型变换：.astype(new_type) 将当前数组元素类型转换为新的指定类型，返回一个新数组，如：a.astype(np.float)，可以直接写float不带位数，程序会自动识别；

ndarray转化为列表：.tolist();

ndarray数组的操作，即索引（获取数组中特定位置的元素）和切片（获取数组中元素子集），复制：

​          一维数组的索引和切片：与列表相同；

​          多维数组的索引和切片：索引：a[a, b, c]；切片：a[:, :, :] 每个维度可以再加一个冒号选取步长；

​          布尔型索引和切片：array[array > 5]将输出一个==一维数组==，表示原数组中所有>5的元素；i = np.array([False, True]), array[i]返回的是array数组的第二个轴；

​          复制：b = array.copy() 返回一个新数组；

ndarray数组的运算：

​    1）与标量或针对每个元素自身的运算；

​    2）数组之间的运算(二元)：基本运算，np.maximum(a, b)，np.minimum(a,b)，np.mod(a, b)，np.copysign(x, y) 将数组y中各元素值的符号赋给x中的对应元素；

Numpy随机函数

​    np.random.normal([loc=0,] [scale=1,] [size=1]) 生成一个正太分布的样本值, loc为μ(期望、均值), scale为σ(方差)； 

​    i = np.random.rand(d1[, d2, d3, d4,...]) 生成一个[0,1)之间的N维浮点数组，i * 100可以扩大范围，dn表示生成数据每个维度的数量；

​    np.random.randn(d1[, d2, d3, d4,...])  生成一个N维标准正太分布的样本值；

​    np.random.randint([m=0, ]n[, size=1] [, dtype='l']) 生成N维[m, n)整数数组； ==dtype?==

Numpy数据存取与函数

​    一二维数据的存储文件合适：csv

​    Numpy中==保存==数组为文件的函数：np.savetxt(frame, array, fmt='', delimiter=None)；frame：带后缀名的文件名，可以是.gz或.bz2的压缩文件；array 要存入的数组对象；fmt 写入文件的数据格式，如：%d %.2f %.18e；delimiter 指定分割字符串，默认是空格；                   

​    Numpy中==读取==文件为数组的函数：np.loadtxt(frame, dtype=np.float, delimiter=None, unpack=False)；unpack 如果为False，读入数据将写入一个数组；

多维数据的存取：存取方法1和2对应使用

​    保存：

​    1）a.tofile(frame, sep='', format='%s') frame表示文件名；sep 数据分割字符串，如果是空串，写入文件为二进制文件；format 写入数据的格式；写入文件后，维度信息丢失，也就是读取后要重新reshape；

​    2）np.save(frame, array) or np.savez(frame, array) frame 以.npy为扩展名，压缩扩展名是.npz；该方法可以保留维度和变量信息；

​    读取：

​     1）np.fromfile(frame, dtype=float, count=-1, sep='') count 表示读入元素的个数，-1表示读取整个文件；

​     2）np.load(frame) frame 以.npy为扩展名，压缩扩展名是.npz；

Numpy的统计函数



Numpy的梯度函数（常用于图像或声音数据处理发现边缘）

​    梯度：连续值之间的变化率，即斜率；

​    np.gradient(f) 计算数组f中元素的梯度，若f为多维，返回每个维度的梯度；一维计算方法为(右边元素的值 - 左边元素的值) / 2 ；若一侧没有值，则用当前元素代替；

### Pandas：数据分析核心工具包

三部分内容：Series和Dataframe介绍，时间序列，Pandas的常用操作；

#### Series和Dataframe介绍

##### Series

概述：

​    Series可以看作是带有索引的==一维数组==，索引可以自定义，支持数值和字符串类型，Series的值可以是任何数据类型；

​    .index可以查看Series的索引；.values可以查看Series的值，其值是ndarray类型；

​    Series类似于有顺序的字典；



创建：import pandas as pd

​    1）通过字典创建：dic = {'a': 1, 'b': 'word', 5: 'five', 6: 666}  s = pd.Series(dic) ; s1 = pd.Series(dic, index=['b', 5, 'a', 'q']) 也可以通过index从字典中进行选择操作，若索引在字典中没有对应的值用NaN替代 ;

​    2）通过一维数组创建：arr = np.arange(10)  s = pd.Series(arr, index=np.arange(9, 4, -1)) ;

​    3）通过标量创建：s = pd.Series(100, index=range(10)) ;

​    4）列表或其他函数；

Series的基本操作：

​    1）索引和切片都可以通过自动索引操作，切片返回的结果类型是Series；

​    2）大多操作都类似ndarray和字典；

​    3）Series类型间在运算时会自动对齐不同索引的数据，依照索引操作；



属性：name

​    Series的索引和值都有一个name属性，可通过b.name = '', b.index.name = ''赋值；

值的修改：通过索引修改；

##### DataFrame

概述：

​    共用同一列索引的多列数据组成，每列值的类型可以不同；

​    DataFrame既有行索引，也有列索引，行索引叫index，列索引叫column，都从0开始；

​    常用于表示二位数据，也可以表达多维数据；



创建：

​    1）二维ndarray对象创建：d = pd.DataFrame(np.arange(10).reshape(2, 5))

​    2）由一维ndarray、列表、字典、元组或Series构成的字典：dt = {'one': pd.Series([1, 2, 3], index = ['a', 'b', 'c']), 'two':pd.Series([5, 6, 8, 9], index = ['b', 'c', 'd'])}  d1 = pd.DataFrame(dt)  d2 = pd.DataFrame(dt, index=['b', 'c', 'd'], colums=['two', 'three'])

​    3）Series类型：

​    4）其他的DataFrame类型



Pandas数据类型操作：Series和DataFrame对象转变

​    增加或重排：重新索引

​    d.reindex(index=[...]) or d.reindex(columns=[...])

​    .reindex(...)的参数：index, columns 自定义行列的索引；fill_value 用于填充缺失位置的值；method 当前值向前向后填充；limit 最大填充量；copy 为True时，生成新对象；

​    d.index 获取行索引；d.columns 获取列索引；

​    DataFrame和Series的索引类型是index，index对象是==不可修改==的；

​    索引常用方法：.append(idx) 连接另一个index对象，产生新的index对象；

​                           .diff(idx) 计算差集，产生新的index对象；.intersection(idx) 计算交集；.union(idx) 计算并集；

​                           .delete(loc) 删除loc位置处的元素,产生新的index对象；

​                           .insert(loc, e) 在loc位置上插入一个元素e,产生新的index对象

​    删除：drop

​    ser.drop([...]), d.drop('') 删除行； d.drop('', axis=1) 删除列；

​    axis = 0  代表对横轴操作，也就是第0轴；axis = 1 代表对纵轴操作，也就是第1轴；



运算：

​    1）算术运算：根据行列索引来，补齐后运算，默认生成浮点数；补齐填充NaN；不同维运算为广播运算；运算可以使用符号+-*/，也可使用方法.add(d)  .sub(d) .mul(d) .div(d)，使用方法运算可以加参数，如fill_value, axis；

​    一维Series默认在1轴参与运算；

​    2）比较运算：只比较相同索引的元素，不进行补齐；使用< > <= >= == != 进行运算，结果为布尔值；同纬度运算，形状要一致；不同维度比较运算默认发生在1轴；



排序：



#### 时间序列

TimeSeries / DataFrame: 以DatetimeIndex为索引的Series / DataFrame.

例如：rng = pd.DatetimeIndex(['20180101', '20190202', '20190202'])
           st = pd.Series(np.random.rand(3), index = rng)

##### pd.date_range() 使用日期范围生成，生成的数据类型为

pd.date_range(start = None, end = None, period = None, freq = 'D', normalize = Flase, closed = None)

常用生成方法：1）start, end; 2)start / end, periods

参数解释：period 生成元素的个数；freq生成频率，下面详述；normalize如果为True，会舍去时间部分；closed可以为‘left’, 'right'或None, 以start或end的日期左闭右开，或左开右闭；

freq可取值:

​    'D' 日历日，'B' 工作日，'H' 小时，'T' / 'MIN' 分钟，'S' 秒 或其他代表向下更细分的时间单位；

​    'W-MON' 每周从星期一开始；

​    'WOM-2MON' 从每月的第二个星期的星期一开始；

​    'M' 每月的最后一日；'A' 指定月的最后一日，如：'A-JAN'；Q' 把指定的月作为季度末，表示每个季度的最后一日，如：'Q-JAN'；

​    'BM' 每月的最后一个工作日；类似有：'BA', 'BQ'；

​    'MS' 每月的第一个日历日；类似有：'AS', 'QS' 把指定的月作为季度末，表示每个季度==最后一个月==的第一个日历日；

​    'BMS' 每月的第一个工作日；类似有：'BAS', 'BQS' 把指定的月作为季度末，表示每个季度==最后一个月==的第一个工作日；

​    '7D' 七天，'2H30T'，'2MS' 每隔两个月的第一个日历日；



#### Pandas的常用操作

数据读取：.read_table()、.read_csv()、.read_excel()

​    pd.read_table('文件名', delimiter=',', header='infer', index_col=None, ...)  # 用来读取文本数据；header指定用作列名的行序号，从0开始；index_col把某列为行索引，否则为自动索引，从0开始；

​    pd.read_csv('文件名', engine='python', encoding='...', ...)

​    pd.read_excel('文件名', sheetname='...', ...)

.cut(x, bins, right=True, labels=None,...)

​    用来把一组数据分割成==离散的区间==比如有一组年龄数据，可以使用.cut将年龄数据分割成不同的年龄段并打上标签；

​    x 表示被切分的数据，必须是一维的，可以是df的某一列；

​    bins有三种形式：1）int标量，代表将x平分成bins份。x的范围在每侧扩展0.1%，以包括x的最大值和最小值；

​                                   2）标量序列(常用列表)，定义了被分割后每一个bin的区间边缘；

​                                   3）pandas.IntervalIndex，定义要使用的精确区间。

​    right默认为True，表示是否包含区间右部。比如如果bins=[1,2,3]，right=True，则区间为(1,2]，(2,3]。

[.set_index() 和 .reset_index()](https://www.jianshu.com/p/abf38d68829c)



### Matplotlib：数据可视化第三方库

所有可视化效果图: https://matplotlib.org/gallery.html

该库由各种可视化类组成，内部结构复杂；matplotlib.pyplot是绘制各类可视化图形的命令子库，相当于快捷方式。

#### 使用

魔法函数(适用于JupyterNotebook): %matplotlib inline 自动嵌入显示图表；%matplotlib notebook 嵌入显示交互式图标；%matplotlib qt5 弹出窗口显示交互式图标；

import matplotlib.pyplot as plt

0、设置画布大小，绘制区域设置

fig = plt.figure(figsize=(12, 6)), ax1 = fig.add_subplot(221), ax1.plot()... # 面向对象的方式（推荐）

**OR** plt.subplot(nrows, ncols, plot_number), plt.plot(x, -x) ... # pyplot的方式(.subplot()和.add_subplot()方法参数一样)

plt.subplot(3, 2, 4) / plt.subplot(324) 表示将区域分为3行2列六个区域，将当前绘制区域定位在第四区域，再次使用该方法，可改变当前绘图区域；



1、定义图中的值，曲线类型：plt.plot(x, y, format_string, **kwargs)

​    x, y：控制对应轴的数据，可为列表或数组；

​    format_string：控制曲线格式(颜色，风格，标记)的字符串，可选；

​        颜色：'b' 蓝色, 'g' 绿色, 'r' 红色, 'c' 青绿色, 'm' 洋红色, 'k' 黑色 等; 也可用RGB值控制，如：'#008000'; 灰度值控制，如：'0.8'；

​        标记(在每一个数据点用什么样式标记)：'.' 点标记，',' 像素标记，'o' 实心圈，'v' 倒三角，'^' 上三角，'>' 右三角，'<' 左三角 等；

​        曲线风格：'-'实线， '--' 破折线， '-.' 点划线， ':' 虚线， '' 空串为无线条；

除了用字符串控制，也可以用参数来更精确的控制曲线类型，如: color='green', linestyle='dashed', marker='o' 标记风格, markerfacecolor='blue' 标记颜色, ... 

​    **kwargs：第二组或更多(x, y, format_string), 即同一图形中绘制多条曲线，如plt.plot(a, a\*1.5, a, a\*2.5, a, a\*3.5), 其中a = np.arange(10)；

1）plt.plot([2, 3, 4, 1]) 如果只输入一个列表，默认为Y轴的值，X轴的值为索引；当绘制多条曲线时，各条曲线的x值不能省略；

2）plt.plot([3, 2, 1, 2], [4, 2, 2, 1]) 有两个参数列表则依次为X、Y轴的值；



2、设置坐标

1）plt.ylabel("Grade") 同理有xlabel

2）plt.axis([-1, 10, 0, 6]) 设置X、Y坐标的刻度范围，x取值[-1, 10]，y取值[0, 6]；

3）plt.grid(True) 显示网格



3、展示图表

1）plt.show()



3、保存图表

1）plt.savefig('test', dpi=600) 该方法默认将图片保存为PNG格式，dpi调整图片质量；

#### pyplot 的中文显示

第一种方法：

import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei' 会改变包括数字在内的所有文字

​    rcParams的属性：'font.family' 字体类型，常用的有：'SimHei' 中文黑体，'Kaiti'，'LiSu' 中文隶书，'FangSong'，'YouYuan'，'STSong' 华文宋体；

​                                    'font.style' 字体风格，如：'normal' 正常，'italic' 斜体；

​                                    'font.size' 字体大小，用字号或'large'、'x-small'；

第二种方法（推荐）：

在有中文输出的地方，增加一个属性：fontproperties

如：plt.plot('横轴: 振幅', fontproperties='SimHei', fontsize=20)

#### pyplot的文本显示函数

plt.xlabel() / plt.xlabel() 

plt.title() 对图形整体加文本标签

plt.text() 在任意位置加文本

plt.annotate(s, xy=arrow_crd, xytext=text_crd, arrowprops=dict) 在图形中增加带箭头的注解，s表示注解内容， arrow_crd表示箭头显示的位置，text_crd表示文本显示的位置，dict定义箭头显示的属性；

例如：

plt.title(r'正弦波实例 \$y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)

plt.text(2, 1, r'\$\mu=100$', fontsize=15)

\$$之间的是LaTex表达式

plt.annotate(r'\$\mu=100$', xy=(2,1), xytext=(3, 1.5), arrowprops=dict(facecolor='blue', shrink=0.1, width=2)) shrink是箭头离两侧内容按0.1的比例缩进；

#### pyplot的子绘图区域

简单的子绘图区域设置，可以参看使用第0步的.subplot方法介绍；

复杂的可以用

1）plt.subplot2grid(GridSpec, CurSpec, colspan=1, rowspan=1)

​    原理：设定网格，选中网格（编号从0开始），确定选中行列区域数量（跨多少行和列）；

​    如：plt.subplot2grid((3, 3), (1, 0), colspan=2) 

​    重复利用该函数可切换区域；

2）GridSpec类配合.subplot()方法

​    import matplotlib.gridspec as gridspec

​    gs = gridspec.GridSpec(3, 3)

​    ax1 = plt.subplot(gs[0, :]) 第1行，跨3列（全部列）；

​    ax2 = plt.subplot(gs[1, :-1]) 第2行，从第一列到最后一列，不包括最后一列；

​    ...

#### pyplot常用的图表函数

plt.plot(x, y, fmt, ...) 坐标图；.boxplot(data, notch, position) 箱形图；

.bar(left, height, width, bottom) 条形图；.barh(width, bottom, left, height) 横向条形图；

.polar(theta, r) 极坐标图；.pie(data, explode) 饼图；

.psd() 功率谱密度图；.speegram() 谱图；.cohere() X-Y的相关性函数；

.scatter(x, y) 散点图，其中x和y长度相同；.step(x, y, where) 步阶图；

.hist(x, bins, normed) 直方图； .contour() 等值图；.vlines() 垂直图；

.stem() 柴火图；.plot_date() 绘制数据日期；

##### pyplot饼图的绘制

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

sizes = [15, 30, 45, 10]

explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explodes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)  # explode表示哪一块突出，autopct中间显示百分数的方式，startangle表示饼图的起始角度；

plt.axis('equal')  # 饼图x, y方向的尺寸相等

plt.show()

##### 直方图的绘制

np.random.seed(0) 

mu, sigma = 100, 20  # 均值和标准差

a = np.random.normal(mu, sigma, size=100)

plt.hist(a, 10, normed=1, histtype='stepfilled', facecolor='b', alpha=0.75)  # 第二个参数表示直方图中直方的个数；normed取值0或1，表示纵坐标显示频数还是频率；

plt.title('Histogram')

plt.show()

[注](http://dy.163.com/v2/article/detail/DG3OF9N605118F5T.html)：直方图展示数据的分布，柱状图比较数据的大小；所以直方图的横轴为连续的数据，柱状图横轴为离散数据。

##### 极坐标图的绘制

N = 20

theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)

radii = 10 * np.random.rand(N)

width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')

bars = ax.bar(thera, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):  # 使用循环对图中区域颜色进行设置

​    bar.set_facecolor(plt.cm.viridis(r / 10.))

​    bar.set_alpha(0.5)

plt.show()

##### 散点图的绘制（使用面向对象的方法创建图像，官方推荐）

fig, ax = plt.subplots() #.subplots()  # 参数默认是111，返回值是元组；如果参数是22，（~~可以使用axes = ax.flatten(), axes[0]来选取第一个子区域~~ ax[n]直接定位到子画板）；相比.subplot()，.subplots()可以通过ax[n]直接定位到子画板，且其有参数figsize=(12,8)可以直接指定画板大小。

ax.plot(10*np.random.randn(100), 10\*np.random.randn(100), 'o')

ax.set_title('Simple Scatter')

plt.show()

##### 引力波实例

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate_h, hstrain = wavfile.read(r'H1_Strain.wav', 'rb')
rate_l, lstrain = wavfile.read(r'L1_Strain.wav', 'rb') #实验数据
reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose() # 理想数据

htime_interval = 1 / rate_h
ltime_interval = 1 / rate_l

htime_len = hstrain.shape[0] / rate_h
htime = np.arange(-htime_len/2, htime_len/2, htime_interval)
ltime_len = lstrain.shape[0] / rate_l
ltime = np.arange(-ltime_len/2, ltime_len/2, ltime_interval)

fig = plt.figure(figsize=(12, 6)) # 后面的代码要和这行代码在一个cell中，否则会不显示图像
plth = fig.add_subplot(221)
plth.plot(htime, hstrain, 'y')
plth.set_xlabel('Time(seconds)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')
pltl = fig.add_subplot(222)
pltl.plot(ltime, lstrain, 'g')
pltl.set_xlabel('Time(seconds)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')
pltref = fig.add_subplot(212)
pltref.plot(reftime, ref_H1)
pltref.set_xlabel('Time(seconds)')
pltref.set_ylabel('Template Strain')
pltref.set_title('Template')
fig.tight_layout() # 自动调整图像外部边缘
plt.savefig('Gravitational_Waves_Original.png')
plt.show()

#plt.close() 会报错，说没有.close()方法

## 机器学习简介

步骤：

## 

1）数据预处理：数据准备，数据转换，数据的输出

数据转换的四种方法(sklearn)：调整数据尺度(MinMaxScaler)，正态化数据(StandardScaler)，标准化数据(Normalizer)，二值数据(Binarizer)；根据算法的特征和数据的特征来选；

​        调整数据尺度：数据的所有属性标准化，转换为0到1之间的值；适用于梯度下降算法，回归算法，神经网络算法和K近邻算法；

​        正态化数据：是有效处理符合高斯分布的数据的方法，输出结果以0为中位数，方差为1，作为假定数据符合高斯分布的算法的输入，如：线性回归，逻辑回归，线性判别分析；

​        标准化数据：适合处理稀疏数据(很多数据为0)，适合对使用权重输入的神经网络和使用距离的K近邻算法；

​        二值数据：将数据转化为0或1，在生成明确值或特征工程增加属性的时候使用；



2）特征工程

3）选择模型：即评估算法？

4）优化模型

5）确定最终模型，部署结果



## Python常用库的介绍

time、random、pyinstaller、jieba、wordcloud、os

### time库的使用

用法：import time

time库包含三类函数：

​       1）时间的获取：time()，ctime()，gmtime()

.time() 返回秒单位的浮点型的时间戳；.ctime() 以易读的字符串形式返回当前时间；.gmtime() 获取当前时间，表示为计算机可处理的时间格式（返回如：time.struct_time(tm_year=2018, tm_mon=1, ..., tm_isdst=0)）；

​       2）时间格式化：strftime()，strptime()

.strftime(tpl, ts)  tpl表示格式化模板字符串，ts为.gmtime()返回的类型，如：time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

%y 两位数的年份表示（00-99）%Y 四位数的年份表示（000-9999）

%m 月份（01-12）

%d 日（0-31）

%H 24小时制小时数（0-23）      %I 12小时制小时数（01-12） 

%M 分钟数（00-59）

%S 秒（00-59）

%a 本地简化星期名称                   %A 本地完整星期名称

%b 本地简化的月份名称               %B 本地完整的月份名称

...



.strptime() 以给定的时间格式识别字符串类型的时间，返回的是struct_time，如：time.strptime("2018-01-02 23:12:03", "%Y-%m-%d %H:%M:%S")

​       3）程序计时：sleep()，perf_counter()

time.sleep(s) 程序停止s秒；

perf_counter() 用来计算程序用时；start = time.perf_counter(),..., end = time.perf_counter(), used_time = end - start；

### random库的使用

import random

1）基本随机数函数

random.seed(10)  设定随机数种子，设定种子的好处是，下次设定相同的种子，随机数可以复现；如果不设种子，直接调用.random()，那默认以当前时间戳为种子，很难复现；

random.random() 生成[0,1)之间的随机小数(16位)；

2）扩展随机数函数

.randint(a, b) [a,b]之间的随机整数；

.randrange(m, n[, k]) 生成[m, n)之间以k为步长的随机整数；

.getrandbits(k) 生成k比特长的随机整数；

.uniform(a, b) 生成[a, b]之间的随机小数；

.choice(seq) 从序列seq中随机选择一个元素，如：random.choice([1, 45, 2, 16])；

.shuffle(seq) 将seq中的元素打乱后输出；

### PyInstaller库的使用

可以将源代码（.py）变为可执行文件，可执行文件可以在没有python环境的机器（Windows, Linux, Mac OS X）上执行；

PyInstaller是第三方库；

cmd: pip install pyinstaller

cmd: pyinstaller -F <文件名.py> 会在dist目录中生成同名的可执行文件；

PyInstaller命令常用参数：-h 查看帮助；...

### jieba库的使用

是优秀的中文分词第三方库，依据中文词库，确定汉字之间的关联概率；用户也可以添加自定义词组；提供了三种分词模式，全模式（把文中所有可能的词语都扫描出来，有冗余）、精确模式（无冗余）、搜索引擎模式（基于精确模式的结果，对长词再次切分，有冗余）；

安装 cmd: pip install jieba

常用函数：jieba.lcut(x) 精确模式，返回列表；

​                   jieba.lcut(x, cut_all=True) 全模式，返回列表；

​                   jieba.lcut_for_search(s) 搜索引擎模式，返回列表；

​                   jieba.add_word(s) 向词库中增加新词；

### wordcloud库的使用

是词云展示的第三方库

安装：(cmd) pip install wordcloud

使用： import wordcloud; w = wordcloud.WordCloud()

然后通过向对象w增加参数，可以设置文本，颜色等信息；

常用方法：w.generate(txt) 加载字符串txt；w.to_file(filename) 将词云输出为图像文件（.png或.jpg格式）；

w = wordcloud.WordCloud(<参数>)：width,height,min_font_size,max_font_size（词云中字体最大字号）,font_step,font_path（加载指定字体文件）,max_words（指定词云显示的最大单词数量）,stop_words（指定词云中不显示哪些单词）；background_color（指定词云的背景颜色）；

指定词云形状：from scipy.misc import imread; mk = imread("pic.png"); w = wordcloud.WordCloud(mask=mk)；

### os库的使用

提供了通用的、与操作系统（Win、Mac OS、Linux）基本的交互功能的标准库，包含几百个函数；

常见操作：路径操作(os.path子库)、进程管理（启动系统中其他程序）、环境参数等；

常用函数：

​        1）路径操作：os.path子库以path为入口，操作和处理文件；

常用函数：(import os.path as op;) op.abspath(path) 返回当前path在系统中的绝对路径；

op.normpath(path) 归一化表示path，统一用\\\分割路径；

op.relpath(path) 返回当前程序和文件的相对路径；

op.dirname(path) 返回path中文件所在的目录名称；

op.basename(path) 返回path中的文件名称；

op.join(path, *paths) 组合path和paths，返回一个路径字符串；

op.exists(path) 判断path对应的目录或文件是否已存在；

op.isfile(path), op.isdir(path);

op.getatime(path) 返回path对应的目录或文件上一次的访问时间，返回时间戳，外面可以套时间函数time.ctime()结果更加可读；

op.getmtime(path) 最近一次修改时间；op.getctime(path) 创建时间；

op.getsize(path) 返回path对应的文件大小，以字节为单位；

​        2）进程管理：在当前程序，调用系统中的其他程序；

常用函数：

os.system(command)，在windows系统中返回值为cmd的调用返回信息，参数可以前面加空格跟在命令后；

​        3）环境参数：获取或改变系统环境信息；

常用函数：

os.chdir(path) 修改当前程序的操作路径；

os.getcwd() 返回程序的当前路径；

os.getlogin() 获得当前系统登陆用户名；

os.cpu_count() 获得当前CPU数量；

os.urandom(n) 获得n个字节长度的随机字符串，以十六进制表示，通常用于加解密运算； 

### pickle模块的使用

可以通过序列化和反序列化将对象以文件的形式保存到磁盘，以及从文件中读取对象。

import pickle

import os

存储：

data = {'a':[1,2], 'b':1, 'c':'hello world!'}

pic = open("data.pkl","wb")

pickle.dump(data, pic)

pic.close()

读取：

pic2 = open(pkl文件路径, 'rb')

data = pickle.load(pic2)

### datetime模块



