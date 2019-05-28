import requests
url="https://en.wikipedia.org/wiki/Blog"
var=requests.get(url)
print url.content
