import logging
import socket
import threading

logger = logging.getLogger()


def messageToAddress(data):
    ip, port = data.decode('utf-8').strip().split(':')
    return (ip, int(port))


def sendTo(sock, addr):
    while 1:
        message = input(f"\r向{addr}发送：").encode()
        sock.sendto(message, addr)


def receive(sock):
    while 1:
        data, address = sock.recvfrom(1024)
        print('\r 接收信息: 地址：{} 内容：{}'.format(address, data))


def main(host='127.0.0.1', port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b'0', (host, port))
    print(f"向服务器{host}发送")

    while True:
        print("开始等待接收1")
        data, address = sock.recvfrom(1024)
        print('1、接收: 地址：{} 内容：{}'.format(address, data))
        address = messageToAddress(data)
        print(f"2、获取新地址{address}地址并开始发送")
        sock.sendto(b'0', address)
        break

    t2 = threading.Thread(target=receive, args=(sock,))
    t2.start()
    t1 = threading.Thread(target=sendTo, args=(sock, address,))
    t1.start()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    main()
