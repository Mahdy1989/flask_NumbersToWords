from flask import Flask
from NumberToWord import NumberToWord

app = Flask(__name__)

@app.route('/towords/<string:variable>')
def get_number(variable):
	x = NumberToWord()
	return x.english(variable)

if __name__=='__main__':
	app.run(debug = True)