import click
import data.main as data

@click.group()
def cli():
	pass

@click.command(name='list', help='Lists current projects.')
def lst():
	data.lst()

cli.add_command(lst)
