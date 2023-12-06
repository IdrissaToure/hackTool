import socket
import threading

for ping in range(1 ,254):
    address = "192.168.1."+str(ping)
    print(address)
    hostname = None
    alias = None
    socket.setdefaulttimeout(1)
try:
    hostname, alias,addresslist = socket.gethostbyaddr(address)
except socket.herror:
    hostname = None
    alias = None
    addresslist = address
    print(addresslist,'=>', hostname)
Host={host}
class NetscanThread(threading.thread):
    def _init_(self, address):
        self.address= address
        threading.Thread.daemon_init_(self)
        def run(self):
            self.lookup(self.address)
    try:
        hostname, alias,addresslist = socket.gethostbyaddr(address)
        global host
        host[address] = hostname
    except socket.herror:
        host[address] = None
        if _name_=='_main_':
            address=[]
            for ping in range(1 ,254):
                address.append(" 192.168.0."+str(ping)
                               threads=[]
                               netscanthreads= [NetscanThread(address) for address in address]
                               thread.start()
                               thread.append(thread)
                               for t in thread:
                               t.join()
                               for address , hostname in host.i


