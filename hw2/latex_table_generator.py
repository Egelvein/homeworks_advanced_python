
_a = ['Name',
        'Surname',
        'Age',
        'Sex',
        'Job',
        'Education',
        'Kids',
        'Citizenship']

_b = ['Kurt',
        'Vonnegut',
        '84',
        'Male',
        'Writer',
        'Cornell University (unfinished)',
        '4',
        'USA']


def make_table(list1: list, list2: list):
    table = ''
    table += '\documentclass{article}\n\\begin{document}\n\\begin{tabular}{|r|l|}\n\hline\n'
    
    for item in zip(list1, list2):
        table += item[0]
        table += ' & '
        table += item[1]
        table += '\\\\'
    
    table += '\n\hline\n\end{tabular}\n\end{document}'
    
    return table

if __name__ == '__main__':
    latex_table = make_table(_a, _b)
    print(latex_table)

