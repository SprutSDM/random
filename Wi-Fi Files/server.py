# coding: utf8

# Server for sending file
import socket, math, os


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(10)
sock.bind(('', 9090))
sock.listen(5)
conn, addr = sock.accept()

fin = open('input_output.txt')
inp = fin.readline().split('=')[1].strip()
outp = fin.readline().split('=')[1].strip()
servIP = fin.readline().split('=')[1].strip()
fin.close()

fin = open(inp, mode='rb')
length = math.ceil(os.path.getsize(inp) / (4096 * 16))
print('File size:', length * 4096 * 16)
x = 0
print('Start sending file')
for i in range(length + 1):
    if x != i * 100 // length:
        print(i * 100 // length, '%', sep='')
        x = i * 100 // length
    n = fin.read(4096 * 16)
    conn.send(n)
conn.send('end'.encode('utf-8'))
fin.close()
print('File sent')
input()