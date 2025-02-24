people = [ {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 30}, {'name':
'David', 'age': 20} ]

def sort_people(people):
    sort_croissant = sorted(people,key =lambda x : x['age'])
    return sort_croissant

print(sort_people(people))
    