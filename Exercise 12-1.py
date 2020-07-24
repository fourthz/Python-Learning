
# Exercise 12-1

# This will prompt the user for a URL and attempt to read the web page.

import socket

# Obtain a valid url page and open the page if it is valid

url_name = input("Enter a URL using the format <host>/<page>: ")
host = url_name.split("/")
host = host[0]
url_name = "http://" + url_name

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = "GET " + url_name + " HTTP/1.0\r\n\r\n"
    cmd = cmd.encode()
    mysock.send(cmd)

except:
    print("No such URL. Make sure you use the format <host>/<page>.")
    quit()

# Print the data from the page    

while True :

    data = mysock.recv(512)

    if len(data) < 1 :
        break

    print(data.decode(), end='')

mysock.close()
