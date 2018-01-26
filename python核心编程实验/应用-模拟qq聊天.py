from  threading import Thread
from socket import *

#收数据，然后打印
def recvDate():
    while True:
        recvInfo = udpSocket.recv(1024)
        print("\r>>%s:%s>>"%(str(recvInfo[1]),recvInfo[0].decode("gb2312")))

#检测键盘，发数据
def sendData():
    while True:
        sendInfo = input("<<")
        udpSocket.sendto(sendInfo.encode("gb2312"),(destIp,destPort))

udpSocket = None #因为线程不能共用局部变量 所以先定义一个
destIp = ""
destPort = 0

def main():
    global udpSocket #因为修改了全局变量
    global destIp
    global destPort

    destIp = input("对方的ip")
    destPort = int(input("对方的端口"))

    udpSocket = socket(AF_INET,SOCK_DGRA)
    udpSocket.bind("",4567)

    tr = Thread(target=recvDate)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == "__main__":
    main()