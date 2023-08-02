"""
Date: 12/25/2022
Miguel Ángel Bustamante Pérez

Match
"""

serie = 'N-02'

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case _:
        print('No match found')


client = {
    'name':'Federico',
    'age': 45,
    'job': 'teacher'
    }

movie = {
    'title':'Matrix',
    'key':{
        'protagonist':'Keanu Reeves',
        'director':'Lana and Lilly Wachowski'
    }
}

elements = [client, movie, 'book']

for element in elements:
    match element:
        case {
            'name':name,
            'age': age,
            'job': job}:
            print('Its a client')
            print(name, age, job)
        case {
            'title':title,
            'key':{
                'protagonist':protagonist,
                'director':director
                }}:
            print('It is a movie')
            print(title, protagonist, director)
        case _:
            print('I dont know what this is')