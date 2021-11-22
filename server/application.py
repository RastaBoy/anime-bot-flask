from flask import Flask
from settings import Config


def run_server():
    cfg = Config()
    return build_app().run(host=cfg.server_settings.host, port=cfg.server_settings.port)


def build_app():
    app = Flask('Anime Bot Server')
    return app