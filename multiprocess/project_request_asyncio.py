from time import time
from urllib.request import Request, urlopen
import asyncio

urls = ["https://www.google.com/search?q=" + keyword for keyword in ["apple", "orange", "grape"]]

async def fetch(url):
    request = Request(url, headers={'User-Agent':"Mozilla/5.0"})
    response = await loop.run_in_executor(None, urlopen, request)
    page = await loop.run_in_executor(None, response.read)
    return len(page)

async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
    result = await asyncio.gather(*futures)
    print(result)

begin = time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
end = time()
print("run time : {0}".format(end-begin))

# [93430, 108004, 103933]
# run time : 1.259434461593628