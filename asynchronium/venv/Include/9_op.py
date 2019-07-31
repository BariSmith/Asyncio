from time import time
import asyncio
import aiohttp

def write_immage(data):
    filename = 'file-{}-jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)



async def fetch_content(url, session):
    async with session.get(url, allow_redirect=True) as response:
        data = await response.read()
        write_immage(data)


async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks) # star - that mean unpacked list

if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)