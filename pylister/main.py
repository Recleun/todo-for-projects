import click
import data.main as data

class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail(f"Too many matches: {', '.join(sorted(matches))}")

    def resolve_command(self, ctx, args):
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args

@click.group(cls=AliasedGroup)
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
