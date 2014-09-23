#from urllib2 import Request, urlopen, URLError
import requests

base_url = 'http://localhost/'
url = base_url + ''
r = requests.get(url)

try:
    response = urlopen(request)
    kittens = response.read()
    print kittens[559:1000]
except URLError, e:
    print 'No kittez. Got an error code:', e


