#(1)
#ctime.py
import time


def application(env, start_response):  # env 用户请求信息
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()


#(2)
#动态web服务器运行python脚本程序编写
import socket
import re
from multiprocessing import Process
import sys

# 设置静态文件根目录 必须全部大写
HTML_ROOT_DIR = "./"

WSGI_PYTHON_DIR = "./wsgipython"


class HTTPServer(object):
    """"""

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                      1)  # 当这里收到一个socket实例的时候，修改socket级别的 选项的重用地址 值设置为1

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s:%s]用户连接上了" % (client_address[0], client_address[1]))
            handle_clien_process = Process(target=self.handle_clien, args=(client_socket,))
            handle_clien_process.start()
            client_socket.close()

    def start_response(self, status, headers):
        """
        status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
        """
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s:%s\r\n" % header
        self.response_headers = response_headers  # 将值放到对象中

    def handle_clien(self, client_socket):
        """处理客户端请求"""
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print("request_data:", request_data)

        requese_lines = request_data.splitlines()
        for line in requese_lines:
            print(line)

        # 解析请求报文
        # 'GET / HTTP /1.1'
        request_start_line = requese_lines[0]  # 这个是b''类型
        # 提取用户请求的文件名
        file_name = re.match(r"\w+\s+(/[^ ]*)\s", request_start_line.decode("utf-8")).group(
            1)  # 正则表达式  [^ ]只要不是空格，就一直往后走 提取第一个 只能切字符串类型
        if file_name.endswith(".py"):
            m = __import__(file_name[1:-3])  # 传一个包名或者模块名就能导入 返回来的就是一个模块
            env = {}
            response_body = m.application(env, self.start_response)  # 模块中必须有的函数
            response = self.response_headers + "\r\n" + response_body
        else:
            if "/" == file_name:
                file_name = "/index.html"

            # 打开文件，读取内容
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")  # 以二进制的方式打开 因为有可能要打开图片
            except IOError:
                response_satrt_line = "HTTP/1.1 404 Not Found\r\n"
                reponse_headers = "Server: My server\r\n"
                response_body = "The file is not found"
            else:
                file_data = file.read()

                file.close()

                # 构造响应数据
                response_satrt_line = "HTTP/1.1 200 OK\r\n"
                reponse_headers = "Server: My server\r\n"

                response_body = file_data.decode("utf-8")

            response = response_satrt_line + reponse_headers + "\r\n" + response_body  # 也可以放到finally里面 代表不管怎么样都会执行
            print("response data:", response)

        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))  # python3要转换成字节

        # 关闭客户端连接
        client_socket.close()

    def bind(self, port):
        self.server_socket.bind(("", port))


def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)  # 先从当前路径找 找不到去WSGI_PYTHON_DIR的目录找
    http_server = HTTPServer()
    http_server.bind(8000)
    http_server.start()


if __name__ == "__main__":
    main()