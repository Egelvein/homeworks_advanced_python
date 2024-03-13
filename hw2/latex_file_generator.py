import os
from latex_table_generator import make_table


a = ['Name',
        'Surname',
        'Age',
        'Sex',
        'Job',
        'Education',
        'Kids',
        'Citizenship']

b = ['Viacheslav',
        'Siniaev',
        '23',
        'Male',
        'AI Researcher / Master Student',
        'ITMO University (in process)',
        '0',
        'Westeros']


if __name__ == '__main__':
    file = 'table.tex'
    
    if os.path.exists(file):
        os.remove(file)

    with open(file, 'w') as file:
        file.write(make_table(a, b))
    
    print('Success')
