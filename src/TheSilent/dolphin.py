import asyncio

ports = []

async def bottlenose(host, port):
    global ports

    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port),10)
        ports.append(port)
        writer.close()

    except:
        pass

async def pink_dolphin(host):
    tasks = []
    for port in range(1,65535):
        tasks.append(bottlenose(host, port))

    await asyncio.gather(*tasks)

def dolphin(host):
    asyncio.run(pink_dolphin(host))
    return ports
