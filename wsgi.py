"""
Application Instance
====================

tiny piece of app
"""
import base64

from Flask import Flask


def encode_niu(niu):
    to_encode = "".join([chr(ord(x)+3) for x in niu])
    return base64.b64encode(to_encode)


app = Flask(__name__)

if __name__ == '__main__':
    app.run()