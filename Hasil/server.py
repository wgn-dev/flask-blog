from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")
	
@app.route('/home/<name>')
def home(name):
	from main import Console
	sin = Console('usr/kimin.FCstd')
	doc = sin.OpenDoc()
	obj = sin.OpenObj()
	ttl_obj = len(obj)
	return render_template("home.php", len = len(obj), Dokumen = doc, username=name, obj=obj)

@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		nama = request.form['username']
		return redirect(url_for('home', name=nama))
	else:
		nama = request.args.get('username')
		return redirect(url_for('home', name=nama))

if __name__=='__main__':
	app.run(port=80, debug=True)