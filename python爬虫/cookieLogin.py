import urllib
import urllib.parse
import urllib.request
import ssl


# 忽略ssl安全认证
context = ssl._create_unverified_context()

url = "http://www.renren.com/963117453/profile"
headers = {
    "Accept": "text/plain, */*; q=0.01",
    # Accept-Encoding:gzip, deflate
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    # Content-Length:94
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "ick_login=bca75dad-b81a-4f0c-832b-42fda78e9220; anonymid=jexwx7c87739qp; t=92e61c46a6b69b1afbd101f5899718e56; societyguester=92e61c46a6b69b1afbd101f5899718e56; id=964801666; xnsid=c2d35d85; JSESSIONID=abcHlHHv2GdiZ790kl9iw; springskin=set; jebe_key=ec2cfc11-fef9-4158-8d85-03001bf5a361%7Cb117fd564bd695c53aa334ed60182f91%7C1521444763359%7C1%7C1521444763729; vip=1; ch_id=10015; wp_fold=0; ver=7.0; loginfrom=null",
    "Host": "www.renren.com",
    "Origin": "http://www.renren.com",
    "Referer": "http://www.renren.com/964801666",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.2.1.17116",
    "X-Requested-With": "XMLHttpRequest"
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request).read().decode("utf-8")

print(response)