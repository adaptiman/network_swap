import netifaces

myinterface = "wlan0"

def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)[2][0]["addr"]
    if addr:
        return addr
    else:
        return False

if __name__ == '__main__':
    print(is_interface_up(myinterface))
