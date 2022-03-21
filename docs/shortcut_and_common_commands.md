[toc]

# Windows

- 文件、目录重命名：F2 <br>

- windows terminal生成目录结构命令:  
1. `cd /d xxx` 到指定目录  
2. - `tree /f` 循环生成目录结构；
   - `tree` 生成目录结构；

# Linux

- 查看当前进程: `ps -aux` 详细信息

- 查看系统版本：`lsb_release -a`

- 查看文本行数：`wc -l filename.txt`

- 打包文件：`tar cvf filename.tar *`
  - filename.tar: 指定生成的压缩包名
  - *: 可以指定文件要压缩的若干文件名

- 打包并压缩文件：`tar -zcvf filename.tar.gz *`
  - -z  gzip   .tar.gz
  - -j  bzip2  .tar.bz2
  - -J  xz     .tar.xz

- 解压文件：`tar -xf filename.tar.gz -C /path/`

- 解压tar.xz命令: `tar xvJf ***.tar.xz`

- 编写完shell脚本后，更改权限使其成为可执行文件(shell脚本中不用写#!什么的): `chmod 764 filename.sh `

- 调用接口命令：`curl  -H "Content-Type: application/json" -X POST -d '{"student_id":384003,"teacher_id":5731309}' "http://gateway.idc.cedu.cn/bicourseevalu/api/v1/ifCheckTchStu/"`

- vim中,
  - 查找关键字：命令模式下输入：`/keystr` 就是查找keystr 
  - 显示行号 `:set nu` 取消显示 `:set nonu`

# python-pip & conda

## pip

- 当环境中存在多版本py环境时，指定python版本运行pip: `./python -m pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple`

- 查看py环境的包版本: `pip show numpy`

- pip卸载包: `pip uninstall numpy`

- pip安装包指定源(清华大学镜像站): `pip install keras==2.3.1 -i https://pypi.tuna.tsinghua.edu.cn/simple`

- 列出已经安装的python包
  - `pip list`
  - `pip freeze` 以requirements格式输出当前python环境已安装的包，不包含自带包; 后面跟参数`- all`可以打印出所有包

- 使用requirements.txt批量安装包: `pip install -r requirements.txt`

## conda

- conda安装本地包：
  1. 官网下载包对应的.whl文件, 放到./anaconda/pkgs目录下;
  2. 打开anaconda, environments, 环境箭头选择 open Terminal, 切换到/anaconda/pkgs目录下;
  3. 执行命令：`pip install ./xxx.whl`

- conda上查看指定包可用版本：`conda search package_name`

- 查看某个包版本：`conda list package_name`

- 升级包: `conda update package_name`

### windows下使用conda虚拟环境

以下命令需要在anaconda prompt环境输入<br>
- 查看当前所有虚拟环境：`conda env list`
- 创建虚拟环境：`activate`初次使用需要 `conda create -n py_3.6 python=3.6`  py_3.6 是环境名称<br>
- 激活虚拟环境：`conda activate py_3.6` 即进入指定虚拟环境
- 退出虚拟环境：`deactivate`
- 删除某个虚拟环境：`anaconda env remove -n xxx` 
- 设置conda下载源：`conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/`

### 常见问题

- 所需的包在conda下没有怎么办？
  - 在conda虚拟环境下，使用pip安装；

#  Jupyter快捷键

- 删除cell: 选中要删除的cell, 在命令模式下, 连按两次d, 或者按x;
- 方法参数提示：shift + TAB

# Pycharm

- 格式化脚本 `ctrl + alt + L`

- 代码设置标签 `ctrl + f11` 点击标签可以增加描述; `shift + f11`  展示所有标签

- debug 
  - Show Execution Point 显示当前程序执行点
  - Step Over 调试一行代码
  - setup out 

# VS Code

- 比较两个文件的不同，命令行：`code -r -d a.txt b.txt`

- 列出目录中的所有文件名： `ls | code -`

- 脚本模板设置: ctrl + shift + p, 输入 snippets

- 使用conda虚拟py环境：在设置的'python.pythonPath'值改为: D:\Apps\anaconda3\envs，ctrl+shift+p选择python环境就能看到多个可选环境



