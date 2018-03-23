import urllib
import urllib.request
import urllib.parse


url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=None"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.2.1.17116"}

# formdata和url中有重合的可以删除掉url中重合的部分
formdata = {
    "start": "20", #起始页
    "limit": "20" #一页多少数据
}

data = urllib.parse.urlencode(formdata).encode("utf-8")

request = urllib.request.Request(url, data=data, headers=headers)

response = urllib.request.urlopen(request).read().decode("utf-8")
print(response)