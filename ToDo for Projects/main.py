import click
import database.main as database

@click.group()
def cli():
	pass

@click.command(name='list', help='Lists current projects.')
def lst():
	database.connect()

cli.add_command(lst)
