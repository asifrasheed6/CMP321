#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 3 Exercise 4

serverInfo = ( "id=0;role=admin;username=joe;surname=naysmith","surname=suffi;username=sam;role=guest;id=421","id=33;surname=lee;username=mia;role=staff"  )
db = {}

for x in serverInfo:
    x = x.split(';')
    
    id = 0
    role = 'null'
    username = 'null'
    surname = 'null'

    for info in x:
        info = info.split('=')
        
        if info[0] == 'id':
            id = info[1]
        elif info[0] == 'role':
            role = info[1]
        elif info[0] == 'username':
            username = info[1]
        elif info[0] == 'surname':
            surname = info[1]

    buffer = {'username':username, 'surname':surname, 'role':role}
    db[id] = buffer

print(db)
print('\n\n\n\n')
for employee in  db.values():
    print(employee['username'].upper(),employee['surname'].upper(),employee['role'].upper())
print('\n\n\n\n')
index =sorted(db.keys())
for i in index:
    print(db[i]['username'].upper(),db[i]['surname'].upper(),db[i]['role'].upper())

