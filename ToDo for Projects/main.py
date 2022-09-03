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

@cli.command(name='remove', help='Removes a project')
@click.argument('name')
def remove(name):
	data.remove(name)

@cli.command(name='set', help='<project name> <type: name/description> <new name/description>')
@click.argument('project name')
@click.argument('type')
@click.argument('new')
def set(name, type, new):
	data.set(name, type, new)
