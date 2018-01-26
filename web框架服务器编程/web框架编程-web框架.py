import time

#from MyWebServer import HTTPServer

HTML_ROOT_DIR = "./html"
class Application(object):
    """框架的核心部分，也就是框架的主题程序，框架是通用的"""
    def __init__(self,urls):
        #设置路由信息
        self.urls = urls

    def __call__(self, env, start_response): #让类能像函数一样被调用起来
        path = env.get("PATH_INFO","/")
        if path.startswith("/static"):
            #要访问静态文件
            file_name = path[7:]
            #打开文件 读取内容
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")  # 以二进制的方式打开 因为有可能要打开图片
            except IOError:
                # 代表未找到路由信息，404错误
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "not found"
            else:
                file_data = file.read()
                file.close()

                status = "200 OK"
                headers = []
                start_response(status, headers)
                return file_data.decode("utf-8")
        else:
            for url, handler in self.urls:
                if path == url:
                    return handler(env, start_response)
        #代表未找到路由信息，404错误
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found"

def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()

def say_hello(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello chunjue"

urls = [
    ("/", show_ctime),
    ("/ctime", show_ctime),
    ("/sayhello", say_hello)
    ]
app = Application(urls)
#if __name__ == "__main__":
    #urls = [
        #("/", show_ctime),
        #("/ctime", show_ctime),
        #("/sayhello", say_hello)
        #]
    #app = Application(urls)
    #http_server = HTTPServer(app)
    #http_server.bind(8000)
    #http_server.start()