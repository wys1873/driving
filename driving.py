age= input('请输入年龄：')
age=int(age)
country=input('请输入国家：')
if country=='中国':
	if age>=18:
		print('可以考驾照')
	else:
		print('不可以')
elif country=='美国':
	if age>=16:
		print('可以考驾照')
	else:
		print('不可以')
else:
	print('只能输入中国或美国')

