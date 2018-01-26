from bs4 import BeautifulSoup
import requests
import time
from urllib.parse import urljoin

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = 'https://en.wikipedia.org/wiki/Philosophy'
article_chain = [start_url]

def continue_crawl(search_history,target_url,max_num=25):
    if search_history[-1] == target_url:
        print("zhao dao le")
        return False
    elif len(search_history) > max_num:
        print("bu zhao le")
        return False
    elif search_history[-1] == search_history[:-1]: #因为切片出最后的一个元素也是列表 字符串不会与列表相等
        print("si xun huan")
        return False
    else:
        return True

def find_first_link(url):
    #从“url”获取HTML，使用请求库
    response = requests.get(url)
    html = response.text
    #将html输入到Beautiful Soup
    soup = BeautifulSoup(html,"lxml")
    #找到文章的第一个链接
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return
    #将第一个链接作为字符串返回，如果没有链接，则返回一个链接
    first_link = urljoin('https://en.wikipedia.org/', article_link)

    return first_link


while continue_crawl(article_chain,target_url):
    print(article_chain[-1])
    # 在article_chain中下载最后一篇文章的html
    # 在html中找到第一个链接
    first_link = find_first_link(article_chain[-1])
    if first_link==False: #当达到一个没有链接的文章时
        print("zhe shi yi ge mei you lian jie de wen zhang")
        break
    # 将第一个链接添加到article_chain
    article_chain.append(first_link)
    # 延迟大约两秒钟
    time.sleep(2)