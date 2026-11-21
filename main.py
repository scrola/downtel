from telethon import TelegramClient
from telethon import errors
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterDocument

api_id = ""
api_hash = ""
client = TelegramClient("anon", api_id, api_hash)


async def mainMenu(option):
    list = []
    list.append(option)
    return list


async def downloadVideos(chat_id):
    async for message in client.iter_messages(chat_id, filter=InputMessagesFilterVideo):
        path = await message.download_media()
        print("File saved to", path)


async def downloadPhotos(chat_id):
    async for message in client.iter_messages(
        chat_id, filter=InputMessagesFilterPhotos
    ):
        path = await message.download_media()
        print("File saved to", path)


async def downloadFiles(chat_id):
    async for message in client.iter_messages(
        chat_id, filter=InputMessagesFilterDocument
    ):
        path = await message.download_media()
        print("File saved to", path)


try:

    async def main():
        print("1) Fotos\n" "2) Vídeos\n" "3) Arquivos\n" "4) Tudo\n")
        option = int(input("Digite a(s) opção(es) desejada(s): "))
        download = await mainMenu(option)
        channelId = int(input("Digite o ID do canal: "))
        if download[0] == 1:
            await downloadPhotos(channelId)
        elif download[0] == 2:
            await downloadVideos(channelId)
        elif download[0] == 3:
            await downloadFiles(channelId)
        elif (
            download[0] == 1
            and download[1] == 2
            or download[0] == 2
            and download[1] == 1
        ):
            await downloadPhotos(channelId)
            await downloadVideos(channelId)
        elif (
            download[0] == 2
            and download[1] == 3
            or download[0] == 3
            and download[1] == 2
        ):
            await downloadFiles(channelId)
            await downloadVideos(channelId)
        elif (
            download[0] == 1
            and download[2] == 3
            or download[0] == 3
            and download[1] == 3
        ):
            await downloadPhotos(channelId)
            await downloadFiles(channelId)
        elif download[0] == 4:
            await downloadPhotos(channelId)
            await downloadVideos(channelId)
            await downloadFiles(channelId)

except errors.FloodWaitError as e:
    print("Flood for", e.seconds)
with client:
    client.loop.run_until_complete(main())
