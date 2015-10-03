
from flask import Flask, jsonify, url_for, render_template,request,redirect

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
	return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)