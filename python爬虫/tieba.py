import urllib
import urllib.parse
import urllib.request



def loadPage(url, filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    url：需要爬取的url地址
    filename:处理的文件名
    """
    print("正在下载" + filename)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.2.1.17116"}
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request).read().decode("utf-8") #爬取的网页汉字未解码，这里用utf-8解码


def writePage(html, filename):
    """
    作用：将html内容写入到本地
    html：服务器响应的内容
    """
    print("正在保存" + filename)
    #自动调用close方法 文件写入
    with open(filename, "w") as f:
        f.write(html)
    print("-" * 30)


def tiebaSpider(url, beginPage, endPage):
    """
    作用：贴吧爬虫调度器，负责组合处理每个页面的url
    url：贴吧url的前部分
    beginPage：起始页
    endPage：结束页
    """
    for page in range(beginPage, endPage+1): #因为range最后一个取不到 所以+1
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        #print(fullurl)
        html = str(loadPage(fullurl, filename))
        #print(html)
        writePage(html, filename)
    print("谢谢使用")

if __name__ == "__main__":
    kw = input("请输入需要爬取的贴吧名：")
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入结束页："))

    url = "https://tieba.baidu.com/f?"
    # urlencode转码 将汉字转为%E6%9D%8E%E6%AF%85之类的东西  例如这里转成
    #kw=%E6%9D%8E%E6%AF%85
    key = urllib.parse.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)