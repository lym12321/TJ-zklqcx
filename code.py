import requests
import os
import sys
from PIL import Image, ImageDraw
import pytesseract

server_list = [
	'111.160.75.143:9081',
	'221.238.12.35:9081',
	'202.113.160.165:9081'
]

if sys.argv[1]=='about':
	print('Code.py 验证码获取\n数据来源：招考资讯网')
	os.system("pause>nul")
	exit()
server=server_list[int(sys.argv[1])-1]
print("服务器："+server)
img_src="http://"+server+"/KWService/servlet/ImageServlet"
url_cx="http://"+server+"/KWService/zklqcx.do"
url_jg="http://"+server+"/KWService/zklqjg.do"
##读Cookies开始
cf = open(r"Cookies","r")
cookies = cf.read()
cookies = cookies.replace('{"','')
cookies = cookies.replace('"}','')
cookies = cookies.replace('", "',';')
cookies = cookies.replace('": "','=')
##读Cookies结束
print(cookies)
#添加请求头
headers = {
	'Host':server,
	'Origin':'http://'+server,
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
	'Referer':url_cx,
	'Cookie':cookies
}
def getImage(imgUrl):

	r = requests.get(imgUrl, stream=True, headers=headers)
	extension = os.path.splitext(imgUrl)[1] # 获取扩展名
	imgName = ''.join(["./image",extension])
	with open(imgName, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
				f.flush()
		f.close()
	return imgName


def showImage():
	image = getImage(img_src)
	from PIL import Image
	import matplotlib.pyplot as plt
	img = Image.open(image)
	img = img.convert('RGBA')
	pixdata = img.load()
	up=210 #上阈值
	down=35 #下阈值
	for y in range(img.size[1]):
		for x in range(img.size[0]):
			#print(pixdata[x, y])
			if pixdata[x, y][0]<=down and pixdata[x, y][1]<=down and pixdata[x, y][2]<=down:
				pixdata[x, y] = (255, 255, 255, 255)
			if pixdata[x, y][0]>=up and pixdata[x, y][1]>=up and pixdata[x, y][2]>=up:
				pixdata[x, y] = (255, 255, 255, 255)
	code = pytesseract.image_to_string(img)
	exclude_char_list='.:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥‘ '
	code=''.join([x for x in code if x not in exclude_char_list])
	print("（OCR）仅供参考："+code)
	plt.figure("验证码")
	plt.imshow(img)
	plt.show()

	
if __name__ == "__main__":
	showImage()
