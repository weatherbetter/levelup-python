import time
import asyncio

start = time.time()
async def my_func():
    for i in range(10):
        await asyncio.sleep(0.5) # 이벤트 루프를 블락하지 않는다(time은 블락한다)
        print(i)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(my_func(), my_func(), my_func()))
loop.close()
end = time.time()
print(end - start) # 5.025529623031616