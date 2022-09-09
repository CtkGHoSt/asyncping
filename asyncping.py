import asyncio
import platform
 
if platform.system().lower() == 'windows':
    OS = 'w'
elif platform.system().lower() == 'linux':
    OS = 'l'

sem = asyncio.Semaphore(20) 

async def ping(ip, timeout:int=1):
    async with sem:
        proc = await asyncio.create_subprocess_exec('ping', '-n' if OS=='w' else '-c', str(timeout),'-w','1', ip, stdout=asyncio.subprocess.PIPE)
        stdout = await proc.communicate()
        # print(str(stdout[0]))
        res = str(stdout[0])#, encoding='GBK')
        if res.find('%')!=-1 and res.find('100%')==-1:
            return True
        return False

def simping(ip, timeout:int=1):
    return asyncio.run(ping(ip, timeout=timeout))

if __name__ == '__main__':
    print(simping('127.0.0.1'))