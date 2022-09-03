import click
import data.main as data

@click.group()
def cli():
	pass

@cli.command(name='list', help='Lists current projects.')
def lst():
	data.lst()

@cli.command(name='create', help='Creates a new project.')
@click.option('--desc', default='', help='Description of the project.')
@click.argument('name')
def create(desc, name):
	data.create(desc, name)
