
# Exercise 12-3

# This will prompt the user for a URL and attempt to read the web page. It will stop displaying text
# after it has shown 3000 characters and will provide the total count of the number of characters.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('\nEnter your URL: ')

try:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    the_text = soup.get_text()
    print('\n' + the_text[0:2999])
    print('\nThere are', len(the_text), 'characters on this web page.\n')

except:
    print('\nInvalid url.\n')
