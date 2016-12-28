import os

from lib.config import *
from lib import data_postgresql as pg

from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def mainIndex():
	if request.method == 'POST' and 'day' in request.form:
		pg.new_event(request.form['name'], request.form['day'], request.form['usr_time'], request.form['location'], request.form['username'])
		
	# get today's activities
	results = pg.get_todays_events()

	return render_template('index.html', events=results)

@app.route('/add')
def mainAdd():
	print ("starting server")
	return render_template('add.html')

@app.route('/join')
def mainJoin():
	return render_template('join.html')

@app.route('/join2', methods=['POST'])
def submitJoin():
	pg.add_member(request.form['name'], request.form['phone'], request.form['emailZ'], request.form['pw'], request.form['about'])
	print "HERE"
	return redirect('/')

	
@app.route('/showall')
def showAll():
	results = pg.get_all_events()
	return render_template('show.html', events= results)

# start the server
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
