"""
Application Instance
====================

tiny piece of app
"""
import base64

from flask import Flask, render_template, redirect, request, url_for

from models import db


def encode_niu(niu):
    to_encode = "".join([chr(ord(x)+3) for x in niu])
    return base64.b64encode(to_encode)


app = Flask(__name__)

app.config.update(dict(
    DATABASE=db,
    DEBUG=True,
    SECRET_KEY='ada deh'
))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    niu = request.form['niu']
    return redirect(url_for('show_kelas', niu=niu))


@app.route('/mahasiswa/<niu>')
def show_kelas(niu):
    return render_template('kelas.html', niu=niu)


@app.route('/kelas/<id>')
def detail_kelas(id):
    return True


@app.route('/update')
def update():
    return True


if __name__ == '__main__':
    app.run()