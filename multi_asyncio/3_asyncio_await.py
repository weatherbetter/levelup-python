import asyncio

async def add(a,b):
    print(f"add : {a} + {b}")
    await asyncio.sleep(1)
    return a+b

async def print_add(a,b):
    result = await add(a,b)
    print(f"print_add : {a} + {b} = {result}")

loop = asyncio.get_event_loop()
loop.run_until_complete(print_add(1,2))
loop.close()