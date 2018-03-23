import urllib
import urllib.request
import urllib.parse


#通过抓包的方式获取url，而不是浏览器上显示的
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

key = input("请输入需要翻译的文字：")

formdata = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1521438546181",
    "sign": "f55b052d85585157faf2eaa5dfd49054",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false"
}

data = urllib.parse.urlencode(formdata).encode("utf-8") #data需要转换为utf-8

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.2.1.17116"}

request = urllib.request.Request(url, data=data, headers=headers)

response = urllib.request.urlopen(request).read().decode("utf-8")

print(response)