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
        chatId = int(input("Digite o ID do canal/grupo: "))
        print("1) Fotos\n" "2) Vídeos\n" "3) Arquivos\n" "4) Tudo\n")
        optionList = list(
            map(
                int,
                input(
                    "Digite a(s) opção(es) desejada(s) separadas por espaço: "
                ).split(),
            )
        )

        if 1 in optionList:
            await downloadPhotos(chatId)
        if 2 in optionList:
            await downloadVideos(chatId)
        if 3 in optionList:
            await downloadFiles(chatId)
        if 4 in optionList:
            await downloadAll(chatId)
        else:
            print("Opção inválida. Tente novamente.")
            return

except errors.FloodWaitError as e:
    print("Flood for", e.seconds)
with client:
    client.loop.run_until_complete(main())
