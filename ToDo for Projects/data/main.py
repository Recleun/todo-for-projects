import click
import json

filePath = './data/projects_data.json'

def load():
	try:
		file = open(filePath, 'r+')
		return json.load(file)
	except:
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
	click.echo('\n')
	click.echo(f'Projects ({len(data)}):')
	if len(data) > 0:
		for i in data:
			click.echo(' - {}'.format(i['name']))
	else:
		click.echo(' - No projects found')

def create(desc, name):
	data = load()
	projects = data['projects']
	for project in projects:
		if project['name'] == name:
			click.echo('\n [FAILED] A project with the same name already exists.')
			return
	projects.append({"name": name, "description": desc, "tasks": []})
	click.echo('\n [SUCCESS] Added project')
	save(projects)

def remove(name):
	data = load()
	projects = data['projects']
	index = 0
	success = False
	for project in projects:
		if project['name'] == name:
			projects.pop(index)
			success = True
			save(projects)
			click.echo('\n [SUCCESS] Removed project')
		index += 1
	if success:
		pass
	else:
		click.echo('\n [FAILED] Project not found')

def set(name, type, new):
	pass
