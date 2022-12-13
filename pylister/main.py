import click
import data.main as data

@click.group()
def cli():
	pass

@cli.command(name='list', help='Lists current projects.')
def lst():
	data.lst()

@cli.command(name='addproject', help='Creates a new project.')
@click.option('--desc', help='Description of the project.')
@click.argument('name')
def projectAdd(desc, name):
	data.projectAdd(desc, name)

@cli.command(name='removeproject', help='Removes a project.')
@click.argument('name')
def projectRemove(name):
	data.projectRemove(name)

@cli.command(name='set', help='<projectName> <type: name/description> <new name/description>')
@click.argument('project')
@click.argument('type')
@click.argument('new')
def set(project, type, new):
	data.set(project, type, new)

@cli.command(name='show', help='Shows information and tasks of a project')
@click.argument('name')
def show(name):
	data.show(name)

@cli.command(name='removetask', help='<projectName> <taskID>')
@click.argument('project')
@click.argument('id')
def taskRemove(project, id):
	data.taskRemove(project, int(id))

@cli.command(name='addtask', help='<projectName> <taskName>')
@click.argument('project')
@click.argument('task')
def taskAdd(project, task):
	data.taskAdd(project, task)
