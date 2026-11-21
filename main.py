from telethon import TelegramClient
from telethon import errors
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterDocument

api_id = ""
api_hash = ""
client = TelegramClient("anon", api_id, api_hash)


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


async def downloadAll(chat_id):
    async for message in client.iter_messages(chat_id, filter=None):
        path = await message.download_media()
        print("File saved to", path)


try:

    async def main():
        print("1) Fotos\n" "2) Vídeos\n" "3) Arquivos\n" "4) Tudo\n")
        option = list(map(int, input("Digite a(s) opção(es) desejada(s): ").split()))
        chatId = int(input("Digite o ID do canal/grupo: "))
        if option[0] == 1:
            await downloadPhotos(chatId)
        elif option[0] == 2:
            await downloadVideos(chatId)
        elif option[0] == 3:
            await downloadFiles(chatId)
        elif option[0] == 1 and option[1] == 2 or option[0] == 2 and option[1] == 1:
            await downloadPhotos(chatId)
            await downloadVideos(chatId)
        elif option[0] == 2 and option[1] == 3 or option[0] == 3 and option[1] == 2:
            await downloadFiles(chatId)
            await downloadVideos(chatId)
        elif option[0] == 1 and option[2] == 3 or option[0] == 3 and option[1] == 3:
            await downloadPhotos(chatId)
            await downloadFiles(chatId)
        elif option[0] == 4:
            await downloadAll(chatId)

except errors.FloodWaitError as e:
    print("Flood for", e.seconds)
with client:
    client.loop.run_until_complete(main())
