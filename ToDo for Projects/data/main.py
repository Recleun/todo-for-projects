import click
import json

def load():
	filePath = './data/projects_data.json'
	try:
		file = open(filePath, 'r+')
		return json.load(file)
	except:
		create = open(filePath, 'w+')

		toWrite = {
			"tasks": []
		}

		json.dump(toWrite, create)
		create.close()

		file = open(filePath, 'r+')
		return json.load(file)

def lst():
	data = load()
	click.echo(data['tasks'])
