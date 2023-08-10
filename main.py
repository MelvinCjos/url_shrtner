from urllib.parse import urlencode
from urllib.request import urlopen
import contextlib
import sys

def short_url(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

def main():
    for url in map(short_url, sys.argv[1:]):
        print(url)

if __name__ == '__main__':
    main()
