"""
Application Instance
====================

tiny piece of app
"""
from Flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()