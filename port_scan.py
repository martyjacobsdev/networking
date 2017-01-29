#!/usr/bin/python

################
# Port Scanner - A Multi-threaded approach
# Scans well-known system ports and returns if they are open or closed.
# To increase performance of scanning, adjust delay where necessary.
################

import socket, threading

host = raw_input("Enter an address to scan: ")
ip = socket.gethostbyname(host)
threads = []
open_ports = {}

def try_port(ip, port, delay, open_ports):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET, socket.SOCK_STREAM
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(delay)
    result = sock.connect_ex((ip, port))

    if result == 0:
        open_ports[port] = 'open'
        return True
    else:
        open_ports[port] = 'closed'
        return None


def scan_ports(ip, delay):

    for port in range(0, 1023):
        thread = threading.Thread(target=try_port, args=(ip, port, delay, open_ports))
        threads.append(thread)

    for i in range(0, 1023):
        threads[i].start()

    for i in range(0, 1023):
        threads[i].join()

    for i in range (0, 1023):
        if open_ports[i] == 'open':
            print '\nport number ' + str(i) + ' is open'
        if i == 1022:
            print '\nscan complete!'

if __name__ == "__main__":
    scan_ports(ip, 3)
