from metaconfig import ConfigRoot, Fieldset, StrField, IntField, JsonFileConfigIO

class ServerSettings(Fieldset):
    host = StrField(label='Ip', default='127.0.0.1')
    port = IntField(label='Port', default=8080)

    @property
    def url(self):
        return 'http://' + self.host + ':' + str(self.port) + '/'


class Config(ConfigRoot):
    __io_class__ = JsonFileConfigIO('main_config.json')
    server_settings = ServerSettings(label='Server Settings', default={})
    telebot_token = StrField(label='Telegram Bot Token', default='')
