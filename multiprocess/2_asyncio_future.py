import time
import asyncio

start = time.time()
async def my_func():
    for i in range(10):
        await asyncio.sleep(0.5) # 이벤트 루프를 블락하지 않는다(time은 블락한다)
        print(i)
    return "Test"

loop = asyncio.get_event_loop()
dd = asyncio.ensure_future(my_func())
loop.run_until_complete(asyncio.gather(
    dd, asyncio.ensure_future(my_func()), asyncio.ensure_future(my_func())
    ))
loop.close()
end = time.time()
print(end - start)
print(dd.result)

# 5.0042359828948975
# <built-in method result of _asyncio.Task object at 0x0000021B7BF81FF0>