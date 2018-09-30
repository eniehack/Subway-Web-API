import falcon
from src.routes import *


if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8008, app)
    httpd.serve_forever()
