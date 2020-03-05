from flask import Flask, render_template, request
import mysql.connector
import random
import socket

app = Flask(__name__)


# TODO Update once the database is created
config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '8889',
    'database': 'budget_db',
    'autocommit': True
}


def query_database(command):
	"""Helper function that connects to a database and queries it given the
	command parameter.

	returns: a list of records retrieved from the database
	"""
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	cursor.execute(command)
	records = cursor.fetchall()
	cursor.close()
	connection.close()

	return records


""" ############################ UAuth API #############################@  """
@app.route('/sign_in')
def sign_in():
	"""Function that queries the database to see if the sign in data a user 
	provided is valid.

	:returns a relevant string regarding the outcome of the sign in process
	"""
	username = request.args.get('username')
	password_hash = request.args.get('password_hash')
	
	# Check if a username exists in the database for the given password hash
	command = 'SELECT * FROM users WHERE password_hash = {}'.format(password_hash)
	#records = query_database(command)
	
	# TODO Remove once the database is created
	records = None

	if records is None:
		return 'Invalid username or password'
	elif records[0][0] == username:
		return 'Welcome, {}!'.format(username)
	else:
		return 'Invalid username or password'


@app.route('/sign_up')
def sign_up():
	"""Method that allows a user to sign up.
	
	returns: a relevant string regarding the outcome of the sign up process"""
	username = request.args.get('username')
	password_hash = request.args.get('password_hash')
	
	# Check if a username is already in the database
	command = 'SELECT * FROM users WHERE username = {}'.format(username)
	#records = query_database(command)
	
	# TODO Remove once the database is created
	records = None

	if records is not None:
		return 'Username already in use'
	else:
		return 'Sign up successful, {}'.format(username)


""" ########################### Expenses API ###########################@  """

def compute_average(records):
	computed_sum = 0
	for i in range(len(records)):
		computed_sum += records[i][2]
	return (float) computed_sum / len(records)


@app.route('/average_daily_expenses')
def average_daily_expenses():
	"""Method that returns the average income sum for a user per day.
	"""
	command = 'SELECT * FROM expenses WHERE username = {}'.format()
	# records = query_database(command)
	
	# TODO Remove once the database is created
	records = None
	
	if records not None:
		average = compute_average(records)
	else:
		return 'No data'


@app.route('/average_weekly_expenses')
def average_weekly_expenses():
	return 'No data'

	
@app.route('/average_monthly_expenses')
def average_monthly_expenses():
	return 'No data'


@app.route('/daily_detailed_expenses')
def daily_detailed_expenses():
	"""Method that returns the expenses detailed per day for a user.
	"""
	command = 'SELECT * FROM expenses WHERE username = {}'.format()
	# records = query_database(command)
	
	# TODO Remove once the database is created
	records = None
	
	if records not None:
		return records
	else:
		return 'No data'


@app.route('/expenses_between_dates')
def expenses_between_dates():
	"""Method that returns the expenses that happened between two dates.
	"""
	date1 = request.args.get('date1')
	date2 = request.args.get('date2')

	command = 'SELECT * FROM expenses WHERE username = {} AND \
	expense_date BETWEEN {} AND {}'.format(username, date1, date2)
	# records = query_database(command)
	
	# TODO Remove once the database is created
	records = None
	
	if records not None:
		return records
	else:
		return 'No data'

""" ########################## Incomes API #############################@  """

@app.route('/average_daily_incomes')
def average_daily_incomes():
	"""Method that returns the average income sum for a user per day.
	"""
	command = 'SELECT * FROM incomes WHERE username = {}'.format()
	# records = query_database(command)
	
	# TODO Remove once the database is created
	records = None
	
	if records not None:
		average = compute_average(records)
	else:
		return 'No data'


@app.route('/average_weekly_incomes')
def average_weekly_incomes():
	return 'No data'

	
@app.route('/average_monthly_incomes')
def average_monthly_incomes():
	return 'No data'


@app.route('/daily_detailed_incomes')
def daily_detailed_incomes():
	"""Method that returns the incomes detailed per day for a user.
	"""
	command = 'SELECT * FROM incomes WHERE username = {}'.format()
	# records = query_database(command)
	
	# TODO Remove once the database is created
	records = None
	
	if records not None:
		return records
	else:
		return 'No data'


@app.route('/incomes_between_dates')
def incomes_between_dates():
	"""Method that returns the incomes that happened between two dates.
	"""
	date1 = request.args.get('date1')
	date2 = request.args.get('date2')

	command = 'SELECT * FROM incomes WHERE username = {} AND \
	income_date BETWEEN {} AND {}'.format(username, date1, date2)
	# records = query_database(command)
	
	# TODO Remove once the database is created
	records = None
	
	if records not None:
		return records
	else:
		return 'No data'


@app.route('/')
def root():
	"""Root of the server
	"""
	return 'Budget app server works!'

if __name__ == "__main__":
	app.run(host="0.0.0.0")
