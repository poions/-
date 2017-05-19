import requests
import json
import threading

def postnumber(phone):
	url = 'xxxx.com'
	number_phone = '1300'+str(phone)
	post_data = 'xxxxxx'
	headers = {'user-agent':'Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI G730-U00 Build/HuaweiG730-U00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
	,'Referer': 'xxxxx.com'}
	r = requests.post(url,data=post_data,headers=headers)
	statusq = (r.text)
	bus = json.dumps(statusq,sort_keys=True,indent=4)
	number_status =  r.json()['status']
	print number_status+':'+str(number_phone)
	if number_status == 'OK':
		with open("number.txt", 'a+') as f:
			f.write(str(number_phone)+'\n')
			print number_phone
	else:
		return None

if __name__=='__main__':
	for i in xrange(60):
		t = threading.Thread(target=postnumber,args=(i,))
		t.start()
		for phone in range(5100000,5199999):
			try:
				postnumber(phone)
			except:
				print "error"
