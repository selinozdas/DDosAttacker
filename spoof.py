import random
def ip_spoof():
    ip_int = [str(random.randint(0,255)) for i in range(4)]
    ip = '.'.join(ip_int)
    return ip
