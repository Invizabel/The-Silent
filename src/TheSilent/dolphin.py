import asyncio

async def bottlenose(host, port):
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port), 15)
        writer.close()
        return port

    except:
        pass

async def pink_dolphin(host):
    tasks = []
    for port in range(1,65535):
        tasks.append(bottlenose(host, port))

    hits = await asyncio.gather(*tasks)
    results = []
    for hit in hits:
        if hit != None:
            results.append(hit)

    return results

def dolphin(host):
    ports = asyncio.run(pink_dolphin(host))
    ports = list(dict.fromkeys(ports[:]))
    return ports
