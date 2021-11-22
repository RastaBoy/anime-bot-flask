from telebot import TeleBot


class TBot():
    def __init__(self):
        pass

    def echo(self):
        ...

    def initialize(self, token: str):
        self.bot = TeleBot(token=token)

    def poll(self):
        self.bot.infinity_polling()

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance
