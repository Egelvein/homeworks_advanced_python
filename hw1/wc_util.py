# python3 wc_util.py example.txt

import click
import os


@click.command()
@click.argument('textfiles',
        nargs=-1,
        type=click.Path(exists=True))


def reading(textfiles='--'):
    if textfiles == '--':
        print('Error. Please choose textfile')
        return 0
    
    for textfile in textfiles:
        with open(textfile, 'r') as file:
            lines = file.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i][:-1]

        num1, num2 = processing(lines)
        num3 = os.path.getsize(textfile)

        print(num1, '\t', num2, '\t', num3, '\t', textfile)


def processing(lines):
    num1 = len(lines)
    num2 = 0
    
    for i in range(num1):
        num2 += len(lines[i].split())

    return num1, num2


if __name__ == '__main__':
    reading()
    
