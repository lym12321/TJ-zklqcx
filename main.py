import requests
import re
import sys
import os

##Settings
server="202.113.160.165:9081"
url_cx="http://"+server+"/KWService/zklqcx.do"
url_jg="http://"+server+"/KWService/zklqjg.do"

ksh=sys.argv[1]
zwh=sys.argv[2]

#添加请求头
headers = {
	'Host':server,
	'Origin':'http://'+server,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
	'Referer':url_cx,
	'Cookie':'JSESSIONID=C3D099CC3FA539EEAF9F47374AA4AA25; BIGipServergaokaochengjifabu=2244520128.37919.0000'
	
}

##验证码部分开始

os.system("start code.py")
yzm=input("请输入验证码：")

##验证码部分结束

##查询部分开始（POST）

data={
"ksh":ksh,
"zwh":zwh,
"code":yzm
}
res = requests.post(url=url_jg,headers=headers,data=data)
#print(res.text)
print("----------------------查询结果-------------------------")
print("\t考生号："+ksh+"\n\t座位号："+zwh+"\n\t验证码："+yzm)
buff=res.text
buff = buff.replace('\n','')
buff = buff.replace('\r','')
buff = buff.replace('\t','')

w1 = '考生姓名：</th><td>'
w2 = '</td>'
pat = re.compile(w1+'(.*?)'+w2,re.S)
name = ''.join(pat.findall(buff))

w1 = '<th width="150px">录取批次：</th><td>'
w2 = '</td></tr><tr><th>'
pat = re.compile(w1+'(.*?)'+w2,re.S)
lqpc = ''.join(pat.findall(buff))

w1 = '录取学校：</th><td>'
w2 = '</td>'
pat = re.compile(w1+'(.*?)'+w2,re.S)
lqxx = ''.join(pat.findall(buff))
if(name==''):
	w1 = '<div id="main_content" style="text-align: center">'
	w2 = '</div><div id="main_content" style="text-align: center"><form method="post" action="zklqcx.do">'
	pat = re.compile(w1+'(.*?)'+w2,re.S)
	error_msg = ''.join(pat.findall(buff))
	print("\n\t"+error_msg)
else:
	print("\t考生姓名："+name+"\n\t录取批次："+lqpc+"\n\t录取学校："+lqxx)
print("-------------------------------------------------------")
##查询部分结束
os.system("pause>>nul")
