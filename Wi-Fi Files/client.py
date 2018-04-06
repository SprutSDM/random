#coding: utf8

#Client for receiving file
import os, math, socket


fin = open('input_output.txt')
inp = fin.readline().split('=')[1].strip().encode('utf-8')
outp = fin.readline().split('=')[1].strip().encode('utf-8')
servIP = fin.readline().split('=')[1].strip().encode('utf-8')
fin.close()
fout = open(outp, mode='wb')
n = b'  '
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect((servIP, 9090))
y = 0
print('Start receiving file')
while True:
    y += 1
    n = sck.recv(4096 * 16)
    if n == 'end'.encode('utf-8'):
        break
    fout.write(n)
fout.close()
print('File received')
input()