import asyncio

from asyncping import ping

async def main(*args, **kwargs):
    loop = kwargs['loop']
    test_ips = args
    tasks = [loop.create_task(ping(i)) for i in test_ips]
    # task = loop.create_task(ping('10.0.0.1'))
    # await task
    res = await asyncio.gather(*tasks)
    print(res)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task_list = ['127.0.0.1', '10.0.0.1', '10.0.0.2', '192.168.31.1', 'google.com', 'baidu.com']
    loop.run_until_complete(main(*task_list, loop=loop))