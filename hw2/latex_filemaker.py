import os
from latex_generator import make_table, paste_picture


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
        'Russia']


if __name__ == '__main__':
    file = 'table.tex'
    file_pdf = 'table.pdf'
    path_to_pic = 'images/picture'

    
    if os.path.exists(file):
        os.remove(file)

    s1 = make_table(a, b)
    s2 = paste_picture(path_to_pic, s1)

    with open(file, 'w') as file:
        file.write(s2)

    if os.path.exists(file_pdf):
        os.remove(file_pdf)

    os.system('pdflatex table.tex')

    print('Success')
