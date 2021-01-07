[toc]

# Windows环境使用Anaconda

## 常用命令
以下命令需要在anaconda prompt环境输入<br>
---
- 查看当前所有虚拟环境：`conda env list`
- 创建虚拟环境：`conda create -n py_3.6 python=3.6`  py_3.6 是环境名称<br>
- 激活虚拟环境：`conda activate py_3.6` 即进入指定虚拟环境
- 退出虚拟环境：`deactivate`
- 删除某个虚拟环境：`anaconda env remove -n xxx` 
- 设置conda下载源：`conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/`
- 查看某个包版本：`conda list package_name`
- 升级包: `conda update package_name`
- conda上查看指定包可用版本：`conda search package_name`
## 常见问题
- 所需的包在conda下没有怎么办？<br>
  在conda虚拟环境下，使用pip安装；