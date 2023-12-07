import socket
import random
import string

LISTLEN = 10
TIMEOUT = 100
MAXDEPTH = 6


def generateToken(length=16):
    # 生成包含大小写字母和数字的随机字符串
    characters = string.ascii_letters + string.digits
    token = ''.join(random.choice(characters) for _ in range(length))
    return token


def socketToString(sock):  # 将socket转换为字符串
    localAddress = sock.getsockname()
    remoteAddress = sock.getpeername()
    socketStr = f"{localAddress[0]}:{localAddress[1]} - {remoteAddress[0]}:{remoteAddress[1]}"
    return socketStr


def stringToSocket(socketStr):  # 将字符串转换为socket
    localAddressStr, remoteAddressStr = socketStr.split(" - ")
    localAddress = tuple(localAddressStr.split(":"))
    remoteAddress = tuple(remoteAddressStr.split(":"))
    sock = socket.socket()
    sock.bind(localAddress)
    sock.connect(remoteAddress)
    return sock
