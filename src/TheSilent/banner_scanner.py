import asyncio

async def banner_connect(host, port):
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port), 15)
        data = await asyncio.wait_for(reader.read(4096), 15)
        writer.close()
        if len(data) > 0:
            return f"port {port}: {data.decode(errors='ignore')}"

    except:
        pass

async def banner_gather(host):
    tasks = []
    for port in range(1,65535):
        tasks.append(banner_connect(host, port))

    hits = await asyncio.gather(*tasks)
    results = []
    for hit in hits:
        if hit != None:
            results.append(hit)

    return results

def banner_grabber(host):
    banners = asyncio.run(banner_gather(host))
    banners = list(dict.fromkeys(banners[:]))
    return banners
