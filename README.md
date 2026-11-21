# downtel

Downtel is a open-source Telegram downloader built in Python, using the `dotenv` and `telethon` libraries.

## About the script

### What it can do

- [x] Login on Telegram
- [x] Choose downloading different filetypes
- [x] Download from private channels and groups
- [x] Support all video, photos and documents
- [x] Download all channel/group/chat content
- [ ] Downloading more filetypes (like stickers, etc)
- [ ] Delete massing messages

### How to run this script

#### First of all, clone this repository with:

```
git clone https://github.com/scrola/downtel.git
cd downtel
pip install -r requirements.txt
```

#### After that create an `.env` file containing you API ID and API HASH informations got on [Telegram account website](my.telegram.org).

Your `.env` file may look like this:

```
API_ID = 11111111
API_HASH = "1kshwll2n39smjwdh27jlsha1ksw9a21"

```

#### Run the script with

```
python3 main.py

```

The script will require your phone number and the code sent on your Telegram. The phone number format must be like: +5500000000000, that is, your country code, the regional code and the rest of the number.
