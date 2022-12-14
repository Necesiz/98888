Öimport os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5681957815:AAFwaUUAXcY7_-4ZyAnS8_u8HFcmluL1Qls")

    APP_ID = int(os.environ.get("APP_ID", 17568815))

    API_HASH = os.environ.get("API_HASH", "177622d39f23e7c3d015f3d6ebaacd31")
