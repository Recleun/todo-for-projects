import click
import sqlite3

cursor = None

def connect():
	try:
		connection = sqlite3.connect('./database.db')
		cursor = connection.cursor()
		click.echo('Connected to the DB')
	except Error as err:
		click.echo(err)
