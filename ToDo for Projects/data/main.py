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
	data = load()
	click.echo(data['projects'])

def create(desc, name):
	data = load()
	projects = data['projects']
	for project in projects:
		if project['name'] == name:
			click.echo('\n [FAILED] A project with the same name already exists.')
			return
	projects.append({"name": name, "description": desc, "tasks": []})
	print(projects)
	save(projects)
