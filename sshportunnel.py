#!/usr/bin/env python
# -*- coding:utf-8 -*-
#ssh port forward tunnel
#Author: joe
#Date: 2019-12-16
import time
import threading
from sshtunnel import open_tunnel

def sshTunnel(local_ip,local_port,remote_host,remote_port,sshuser,sshpasswd,private_ip,private_port):
 with open_tunnel(
    (remote_host, remote_port),
    ssh_username = sshuser,
    ssh_password = sshpasswd,
    remote_bind_address=(private_ip, private_port),
    local_bind_address=(local_ip, local_port),
    set_keepalive = 60
) as server:
   while True:
    time.sleep(1)

if __name__ == '__main__':
  tunnel_config = [('127.0.0.1',9000,'8.8.8.8',22,'username','password','192.168.0.222',27017)
]
  threads = []
  for tunnel in tunnel_config:
    th=threading.Thread(target=sshTunnel,args=(tunnel))
    th.start()
    threads.append(th)
  for tunnel_thread in threads:
    tunnel_thread.join()
