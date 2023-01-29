import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6032076608:AAFXge7_JrykpXnRIotIvl-EDa4Cdqr00_Y")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 17983098))
    API_HASH = "ee28199396e0925f1f44d945ac174f64"
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1186940323").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    LOG_CHANNEL = int(-1001683878954)
    MAX_FILE_SIZE = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    TG_MAX_FILE_SIZE = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    FREE_USER_MAX_FILE_SIZE = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "159.223.126.245:1994")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
