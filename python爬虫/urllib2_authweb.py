import urllib.request
import urllib
import urllib.parse


test = "test"

password = "123456"

webserver = "192.168.21.52"

# 构建一个密码管理对象，用来保存和HTTP请求相关的授权账号信息
passwordMgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 添加授权用户信息，第一个参数realm如果没指定，就写none，后面三个分别是站点ip 账号 密码
passwordMgr.add_password(None, webserver, test, password)

httpauth_handler = urllib.request.HTTPBasicAuthHandler(passwordMgr)

proxyauth_handler = urllib.request.ProxyBasicAuthHandler(passwordMgr)  # 同理，用来处理代理基础验证相关的处理器类

opener = urllib.request.build_opener(httpauth_handler, proxyauth_handler)  # 也可以添加多个处理器 用,隔开

# urllib.request.install_opener(opener) 之后使用urlopen就是opener

request = urllib.request.Request("http://" + webserver + "/")

response = opener.open(request)

# response = urllib.request.urlopen(request)  没有的话会报错401 表示需要用户名密码

print(response.read())