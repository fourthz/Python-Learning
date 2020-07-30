
# Exercise 12-4

# This will prompt the user for a URL and attempt to read the web page. It will then count the
# number of paragraph tags and display how many paragraphs there are on the page.

# This doesn't run on a lot of web pages for some reason, probably to do with security settings.
# You can test it with https://docs.python.org.

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

    # Retrieve all of the paragraph tags and count them
    
    paragraph_count = 0
    paragraphs = soup('p')
    
    for paragraph in paragraphs:
        paragraph_count = paragraph_count + 1

    print('\nThere are', paragraph_count, 'paragraphs on this web page.\n')

except:
    print('\nInvalid url.\n')
