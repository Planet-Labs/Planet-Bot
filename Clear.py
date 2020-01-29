import discord
import asyncio


async def clear(message, client):
    ms = message.content.split(" ")
    try:
        ammount = int(ms[1])
    except:
        await client.send_message(message.channel, "메시지 수를 정확히 입력하세요")
        return

    msg = []
    if len(ms) == 2:
        async for m in client.logs_from(message.channel, limit=ammount):
            msg.append(m)
        await client.delete_messages(msg)

    if len(ms) == 3:
        async for m in client.logs_from(message.channel, limit=ammount):
            if str(m.author.id) == str(ms[2]):
                msg.append(m)
        await client.delete_messages(msg)

