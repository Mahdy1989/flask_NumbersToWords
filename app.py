from flask import Flask, jsonify
from numbers import NumberToWords

app = Flask(__name__)

@app.route('/towords/<string:variable>')
def get_number(variable):
	x = NumbersToWords()
	return x.english(variable)