"""
Manipulating keys and valuesin dictionaries in python
"""

people = {}

##

# creanting an key 
# people['name'] = 'Pedro Sbardelotto'

# creanting danimic  key 
key = 'nome_people'

people[key] = 'Pedro'
people['sobrenome'] = "sbardelotto"

print(people[key])

print(people)

del people['sobrenome']

print(people[key])

print(people)

if people.get('sobrenome') is None:
    print('not exist')
else: 
    print(people['sobrenome'])