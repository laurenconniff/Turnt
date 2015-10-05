
from flask import Flask, jsonify, url_for, render_template,request,redirect

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
	return render_template('index.html')


@app.route('/home', methods=['POST','GET'])
def home():
	if request.method == "POST" and request.form['term'] != "NaN":
		print request.form['dial']
		return render_template('friends.html')

	return render_template('home.html')


@app.route('/friends',methods=['POST','GET'])
def friends():
	return render_template('friends.html')


@app.route('/chats',methods=['POST','GET'])
def chats():
	return render_template('chats.html')

if __name__ == "__main__":
	app.run(debug=True)