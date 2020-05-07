import json

jsonstr = '''
            {
                    "name":"ishan",
                    "country":"india",
                    "degree":"engineering",
                    "cgpa": 4.6,
                    "Passed":true,
                    "subjects":["biology", "civil"]
                    }
            '''

data = json.loads(jsonstr)
for k, v in data.items():
    print(k, type(v),  v)

