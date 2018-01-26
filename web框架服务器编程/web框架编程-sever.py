import socket
import re
from multiprocessing import Process
import sys

#设置静态文件根目录 必须全部大写
HTML_ROOT_DIR = "./"

WSGI_PYTHON_DIR = "./wsgipython"

class HTTPServer(object):
    """"""
    def __init__(self, application):
        """构造函数，application指的是框架的app"""
        self.app = application
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  # 当这里收到一个socket实例的时候，修改socket级别的 选项的重用地址 值设置为1

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
        self.response_headers = response_headers  #将值放到对象中

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
        file_name = re.match(r"\w+\s+(/[^ ]*)\s", request_start_line.decode("utf-8")).group(1)  # 正则表达式  [^ ]只要不是空格，就一直往后走 提取第一个 只能切字符串类型
        method = re.match(r"(\w)+\s+/[^ ]*\s", request_start_line.decode("utf-8")).group(1)

        env = {
                    "PATH_INFO": file_name,
                    "METHOD": method
                }
        response_body = self.app(env, self.start_response)  #模块中必须有的函数
        response = self.response_headers + "\r\n" + response_body

        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))  # python3要转换成字节

        # 关闭客户端连接
        client_socket.close()

    def bind(self,port):
        self.server_socket.bind(("", port))


def main():
    sys.path.insert(1, WSGI_PYTHON_DIR) #先从当前路径找 找不到去WSGI_PYTHON_DIR的目录找
    if len(sys.argv) <2:
        sys.exit("python MyWebServer.py Module:app")
    # python MyWebServer.py  MyWebFrameWork:app
    module_name, app_name = sys.argv[1].split(":")
    #module_name = "MyWebFrameWork"
    #app_name = "app"
    m = __import__(module_name)
    app = getattr(m, app_name) #从某个对象中获取什么
    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start()


if __name__ == "__main__":
    main()