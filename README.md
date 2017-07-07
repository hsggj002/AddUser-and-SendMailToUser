# AddUser-and-SendMailToUser
输入用户邮箱，以邮箱@前段为用户名，密码自动生成，添加完成后以用户所输入邮箱为准发送用户名与密码到这个邮箱！


#### 程序运行方法 ######

1、进入openvpn_control/bin目录下：
	执行 python main.py -h可获取帮助信息；

2、命令使用方法：
	python main.py -h
		获取帮助信息
	python main.py -i
		初始化数据库
	python main.py -a xxx@xxx.com
		添加用户，并发送用户名、密码到所输入的邮箱中
	python main.py -r xxx
		删除用户