from flask import Flask, request, render_template
from os import listdir
import os
import sys
from admin import *
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

Bootstrap(app)

@app.route('/')
def index():
    return render_template('home.html', pages=pages)



@app.route('/admin')
def admin():
    return "halo"



@app.route('/<path:path>.html')
def page(path):
    print("View function activated!")
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@freezer.register_generator
def pagelist():
    for page in pages:
        yield url_for('page', path=page.path)


@app.route('/cms')
def cms_index():
    return render_template('list.html', pages=pages)


@app.route('/cms/<path:nama>', methods=['GET'])
def cmd_form(nama):
    # read main.txt file
    #isi = open(nama, "r")
    #baca = isi.read()
    #judu = judul(nama)
    kon = konten(nama)
    #tg = tgl(nama)
    return render_template('cms.html', pages=pages, konten=kon)


@app.route('/edit/<path:nama>', methods=['GET'])
def my_form(nama):
    # read main.txt file
    isi = open(nama, "r")
    baca = isi.read()
    judu = judul(nama)
    return render_template('index.html', isi=baca, judul=judu)

@app.route('/edit/<path:nama>', methods=['POST'])
def my_form_post(nama):
    input_nopol = request.form['text_box']

    if request.method == 'POST':
        with open(nama, 'w') as f:
            f.write(str(input_nopol))
    isi = open(nama, "r")
    baca = isi.read()
    return render_template('index.html', nopol=input_nopol, isi=baca)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=5000)
