from socket import *

def main():
    udpSocket = socket(AF_INET,SOCK_DGRAM)

    binAddr = ("",8080)

    udpSocket.bind(binAddr)

    #收，打印
    while True:
        recvData = udpSocket.recvfrom(1024)
        content,destIfo = recvData
        print("[%s]:%s"%(str(destIfo),content.decode("gb2312")))

if __name__ == "__main__":
    main()