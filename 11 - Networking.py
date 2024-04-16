# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
# mysock.close()

#return ASCII karakter
print(ord('p'))

import urllib, urllib.parse, urllib.error
import urllib.request
#cara lain baca web isi web browser
# counts = dict()
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word,0)+1
#     print(line.decode().strip())
# print (counts);

#cara baca web html
fhand = urllib.request.urlopen('https://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
