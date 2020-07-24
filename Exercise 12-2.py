
# Exercise 12-2

# This will prompt the user for a URL and attempt to read the web page. It will stop displaying text
# after it has shown 3000 characters and will provide the total count of the number of characters.

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

# Count the characters and print up until 3000 characters.

character_count = 0

while True :

    data = mysock.recv(512)

    if len(data) < 1 :
        break

    character_count = character_count + len(data)
    
    if character_count <= 3000 :
        print(data.decode(), end="")
    
    elif (character_count - len(data)) < 3000 :
        str_remainder = data.decode()
        str_remainder = str_remainder[:(3000 - (character_count - len(data)))]
        print(str_remainder, end = "")

print("\nThe number of characters (including the header) is", character_count)

mysock.close()
