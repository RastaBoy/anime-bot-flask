from settings import Config
from server.application import run_server

Config()

def run():
    print('Hello world!')
    print('Server will be run on ' + Config().server_settings.url)
    run_server()


if __name__ == '__main__':
    run()