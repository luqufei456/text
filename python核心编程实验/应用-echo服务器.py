from socket import *


def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)

    binAddr = ("", 8080)

    udpSocket.bind(binAddr)

    num = 1
    # 收，打印
    while True:
        recvData = udpSocket.recvfrom(1024)
        content, destIfo = recvData
        # 将接收到的数据发给对方
        udpSocket.sendto(content, destIfo)

        print("已经将接收到的第%d个数据返回给对方，内容为%s" % (num, content.decode("gb2312")))
        num += 1


if __name__ == "__main__":
    main()