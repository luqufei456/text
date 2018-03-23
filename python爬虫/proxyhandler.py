import urllib
import urllib.request
import urllib.parse
import os

# 代理开关，表示是否启用代理
proxyswitch = True

#构建一个handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器ip+端口号
httpproxy_handler = urllib.request.ProxyHandler({"http": "219.135.164.245:3128"}) #这里是代理ip和端口

#构建一个没有代理的处理器对象
nullproxy_handler = urllib.request.ProxyHandler({}) #不写代理 也要写一个空字典

#私密代理时候 账号@密码
urllib.request.ProxyHandler({"http": "username:password@219.135.164.245:3128"})
proxyuser = os.environ.get("proxyuser") #也可以将账号密码放到系统环境变量中，通过os方法获取，这样保证账号密码的安全性
proxypwd = os.environ.get("proxypwd")  # vi ~/.bash_profile 中增加系统环境变量



if proxyswitch: #如果proxyswitch为true
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

# 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带handler的功能，
# 当需要多次调用opener时可以弄，相当于是一个声明
urllib.request.install_opener(opener)

#构建请求
request = urllib.request.Request("http://www.baidu.com/")

#获取响应
response = urllib.request.urlopen(request)

#打印接受结果
print(response.read().decode("utf-8"))