import socket
import fcntl
import struct


def get_ipv4_address(interface):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ipv4_address = socket.inet_ntoa(fcntl.ioctl(
            sock.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', interface[:15].encode())
        )[20:24])
        return ipv4_address
    except IOError:
        return None
    finally:
        sock.close()


# 获取 eth0 网卡的 IPv4 地址
eth0_ipv4_address = get_ipv4_address('eth0')
print(eth0_ipv4_address)
