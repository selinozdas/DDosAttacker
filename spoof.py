import random
def ip_spoof():
    ip_int = [random.randint(0,255) for i in range(4)]
    ip = '.'.join(ip_int)
    return ip

def random_src():
    src_port = random.randint(1000,9999)
    src_seq = random.randint()
    src_window  = random.randint(1000)
    return src_port,src_seq,src_window



