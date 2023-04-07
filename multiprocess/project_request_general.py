from time import time
from urllib.request import Request, urlopen

urls = ["https://www.google.com/search?q=" + keyword for keyword in ["apple", "orange", "grape"]]

begin = time()
result = []
for url in urls:
    request = Request(url, headers={'User-Agent':"Mozilla/5.0"})
    response = urlopen(request)
    page = response.read()
    result.append(len(page))

print(result)
end = time()
print("run time : {0}".format(end-begin))

# [93423, 105970, 103914]
# run time : 2.7727653980255127