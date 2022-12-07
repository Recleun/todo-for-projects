import os
import click
import json

p = os.path.abspath(__file__)
path = p.split("main.py")
filePath = f'{path[0]}/projects_data.json'

def load():
	try:
		file = open(filePath, 'r+')
		try:
			return json.load(file)
		except json.decoder.JSONDecodeError as err:
			click.echo('\n [ERROR] Failed to load data file. If you edited the file manually, check for extra commas (trailing commas) and delete them.')
			quit()

	except FileNotFoundError:
		create = open(filePath, 'w+')

		toWrite = {
			"projects": []
		}

		json.dump(toWrite, create)
		create.close()

		file = open(filePath, 'r+')
		return json.load(file)

def save(toSave):
	toWrite = {
		"projects": toSave
	}
	jObj = json.dumps(toWrite, indent=4)
	with open(filePath, 'w') as file:
		file.write(jObj)

def lst():
	data = load()['projects']
	click.echo(f'\n Projects ({len(data)}):')
	if len(data) > 0:
		for i in data:
			click.echo(' - {}'.format(i['name']))
	else:
		click.echo(' - No projects found')

def getProject(projectName):
	data = load()
	projects = data['projects']
	indexOfProject = 0
	success = False
	for project in projects:
		if project['name'] == projectName:
			return indexOfProject
		indexOfProject += 1
	if not success:
		return 'not found'

def projectAdd(desc, name):
	data = load()
	projects = data['projects']
	check = getProject(name)
	if check == 'not found':
		projects.append({"name": name, "description": desc, "tasks": []})
		save(projects)
		click.echo('\n [SUCCESS] Added project')
	else:
		click.echo('\n [FAILED] A project with the same name already exists.')

def projectRemove(name):
	index = getProject(name)
	if index != 'not found':
		data = load()
		data['projects'].pop(index)
		save(data['projects'])
		click.echo('\n [SUCCESS] Removed project')
	else:
		click.echo('\n [FAILED] Project not found')

def set(project, type, new):
	index = getProject(project)
	if index != 'not found':
		data = load()
		if type == 'name':
			data['projects'][index]['name'] = new
			save(data['projects'])
			click.echo('\n [SUCCESS] Updated project')
		elif type == 'description':
			data['projects'][index]['description'] = new
			save(data['projects'])
			click.echo('\n [SUCCESS] Updated project')
		else:
			click.echo('\n [FAILED] Type specified is unknown')
	else:
		click.echo('\n [FAILED] Project not found')

def show(name):
	index = getProject(name)
	if index != 'not found':
		data = load()
		projectName = data['projects'][index]['name']
		projectDesc = data['projects'][index]['description']
		if projectDesc == '':
			projectDesc = 'No Description Set'
		projectTasks = data['projects'][index]['tasks']
		click.echo(f'\n PROJECT NAME: {projectName}')
		click.echo(f' DESCRIPTION: {projectDesc}')
		click.echo(f' TASKS ({len(projectTasks)}):\n')
		if len(projectTasks) > 0:
			for i in range(len(projectTasks)):
				click.echo(f'    {i+1} - {projectTasks[i]}')
		else:
			click.echo(' - No tasks found')
	else:
		click.echo('\n [FAILED] Project not found')

def taskAdd(project, task):
	projectIndex = getProject(project)
	if projectIndex != 'not found':
		data = load()
		data['projects'][projectIndex]['tasks'].append(task)
		save(data['projects'])
		click.echo('\n [SUCCESS] Task added successfully')
	else:
		click.echo('\n [FAILED] Project not found')


def taskRemove(project, id):
	projectIndex = getProject(project)
	if projectIndex != 'not found':
		data = load()
		data['projects'][projectIndex]['tasks'].pop(id-1)
		save(data['projects'])
		click.echo('\n [SUCCESS] Task finished successfully')
	else:
		click.echo('\n [FAILED] Project not found')
