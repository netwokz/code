from fileinput import filename
from http import server
import platform
import subprocess

server_list = []

filename = 'ip.txt'
with open(filename, 'r') as reader:
    content = reader.read();
    server_list = content.split('\n')

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '2', host]
    try:
        response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except Exception:
        print('Something went wrong!')
    if response == 0:
        print('{} is Online'.format(host))
    else:
        print('{} is Offline'.format(host))

for ip in server_list:
    ping(ip)

