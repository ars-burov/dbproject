import os
from sys import argv

from aiohttp.web import run_app
from argparse import Namespace
from aiomisc import bind_socket
from setproctitle import setproctitle

from dbproject.api.app import create_app

def main():
    args = Namespace()

    socket = bind_socket(address='0.0.0.0', port=8081, proto_name='http')

    setproctitle(os.path.basename(argv[0]))

    app = create_app(args)
    run_app(app, sock=socket)

if __name__ == '__main__':
    main()
