import json


pydata = {
        'name' : 'ishan',
        'cgpa' : 4.67,
        'passed' :True,
        'courses' : ['Biology', 'civil']
}

jsonstr = json.dumps(pydata)

print(jsonstr)
