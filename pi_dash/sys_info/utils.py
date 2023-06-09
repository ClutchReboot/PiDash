import socket
import platform
import netifaces


def get_private_ips():
    interfaces = netifaces.interfaces()

    local_ipv4 = dict()
    for interface in interfaces:

        ipv4_info = netifaces.ifaddresses(interface).get(2)
        if ipv4_info:
            ipv4_addr = ipv4_info[0].get('addr')
            local_ipv4[interface] = ipv4_addr

    return local_ipv4


def get_sys_info():
    hostname = socket.gethostname()

    return {
        "hostname": hostname,
        "hostByHostname": socket.gethostbyname(hostname),
        "hostByAddress": list(socket.gethostbyname_ex(hostname)),
        "localIpV4": get_private_ips(),
        "platform": {
            "system": platform.system(),
            "version": platform.version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
    }


if __name__ == '__main__':
    print(get_private_ips())
