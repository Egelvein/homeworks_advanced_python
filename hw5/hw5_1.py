import os
import aiofiles
import aiohttp
import asyncio


async def download_image(session: aiohttp.ClientSession,
        url: str,
        filename: str):
    async with session.get(url) as response:
        async with aiofiles.open(filename, 'wb') as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)

async def download_images(num_img: int, path: str):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, num_img + 1):
            url = f'https://picsum.photos/200/300?random={2*i}'
            filename = os.path.join(path, f'img_{2*i}.jpg')
            tasks.append(download_image(session, url, filename))
        await asyncio.gather(*tasks)

async def main(num_img: int, path: str):
    await download_images(num_img, path)


num_img = 50
path = 'artifacts'

if not os.path.exists(path):
    os.makedirs(path)


asyncio.run(main(num_img, path))

