需求：每周自动获取鱼乐卡看板上的数据，整合成周报邮件自动发送。

流程：
1.将原始邮件格式变成html形式，其中的表格用字符换占位符{} 方便后续数据动态填充，表格格式css单独用内联样式表写在开头（外联样式邮件html不支持）；
2.将几张表格的数据用sql文件单独保存，后续获取；
3.python odps包通过阿里云执行sql文件获取表格数据；
4.表格中某些数据需要单独拿出作为邮件文本内容填充；
5.填充值和表格加入到邮件html中，形成最终网页版邮件；
6.邮件自动每周六上午11点发送。

服务器crontab自动调用命令：
0 11 * * 6 python3 /home/wywk/ylk_auto_email/ylk_auto_email.py /home/wywk/ylk_auto_email/ >>/home/wywk/ylk_auto_email/run.log  2>&1

