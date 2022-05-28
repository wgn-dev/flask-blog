from flask import Flask, request, render_template, url_for, redirect
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

@app.route('/cms', methods=['GET', 'POST'])
def cms():
	# read main.txt file
	#judu = []
	l = listdir('pages')
	return render_template('list.html', konten=l)

@app.route('/cms/<path:nama>', methods=['GET'])
def cmd_form(nama):
	f = open(f"pages/{nama}",'r')
	isi = f.read()
	f.close()
	judul = isi[isi.find("title:")+6:isi.find("date:")]
	tgl = isi[isi.find("date:")+5:isi.find('category')]
	data = isi[isi.find('\n\n'):]
	return render_template('cms.html',isi=data.strip(), judul=judul, tgl=tgl)

@app.route('/save', methods=['GET','POST'])
def save():
	if request.method == "POST":
		nama = request.form["title"]
		tgl = request.form["date"]
		isi = request.form["paste-text"]
		f = open(f"pages/{nama}.md",'w')
		f.write(f"title: {nama}\ndate: {tgl}\ncategory: general\n\n\n{isi}")
		f.close()
		return redirect(url_for('cms'))

@app.route("/<path:nama>")
def hapus(nama):
	# return nama.replace("hapus",'pages')
	if os.path.exists(nama.replace("hapus","pages")):
		os.remove(f"{nama.replace('hapus','pages')}")
	return redirect(url_for('cms'))
	
@app.route('/edit/<path:nama>', methods=['GET'])
def my_form(nama):
	# read main.txt file
	isi = open(nama, "r")
	baca = isi.read()
	judu = judul(nama)
	return "Hello Word"
	# return render_template('index.html', isi=baca, judul=judu)

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
		app.run(host='0.0.0.0', port=5000, debug=True)
