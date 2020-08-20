import requests
import os

server="202.113.160.165:9081"
img_src="http://"+server+"/KWService/servlet/ImageServlet"
url_cx="http://"+server+"/KWService/zklqcx.do"
url_jg="http://"+server+"/KWService/zklqjg.do"
#添加请求头
headers = {
	'Host':server,
	'Origin':'http://'+server,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
	'Referer':url_cx,
	'Cookie':'JSESSIONID=C3D099CC3FA539EEAF9F47374AA4AA25; BIGipServergaokaochengjifabu=2244520128.37919.0000'
	
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
    plt.figure("验证码")
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    showImage()