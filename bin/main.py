#-*- coding:utf-8 -*-
#Author: Guangjie Guo


import sys
import random
import re,os
from optparse import OptionParser


base_dir = os.path.dirname(os. path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)


from core import core



checkcode=''

for i in range(8):
	current = random.randrange(0,8)
	if current !=i:
		temp = chr(random.randint(65,90))
	else:
		temp = random.randint(0,9)

	checkcode+=str(temp)


if __name__ == "__main__":
	parser = OptionParser()

	parser.add_option("-i","--init_db",dest="initdb",action="store_true",help="initialization the database")

	parser.add_option("-a","--adduser",dest="mail",action="store",help="write your mail_address")

	parser.add_option("-r","--remove_user",dest="rmuser",action="store",help="keep up wiht a name")

	(options, args) = parser.parse_args()


	if options.mail:
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", options.mail) != None:
			name = options.mail.split('@')[0]
			core.add_user(name,checkcode,options.mail)
		elif options.mail == "":
			print('input a args')
		else:
			print('input a mailaddress')
	if options.rmuser:
		if re.match("^[a-zA-Z0-9]+",options.rmuser) != None:
			core.del_user(options.rmuser)
	if options.initdb:
		core.init_sql()




