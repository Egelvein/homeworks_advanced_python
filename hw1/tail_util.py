# python3 tail_util.py example.txt

import sys
import os
import click

@click.command()
@click.argument('textfiles',
        nargs=-1,
        type=click.Path(exists=True))

def reading(textfiles=''):
    if textfiles == '':
        print('stdin:')
        print(sys.stdin)
        return 0
    
    for textfile in textfiles:
        with open(textfile, 'r') as file:
            lines = file.readlines()
            # print(lines)

        for i in range(len(lines)):
            lines[i] = lines[i][:-1]
        # print(lines)
        if len(textfiles) > 1:
            print(textfile, '\n')
        processing(lines)

def processing(lines):
    length = len(lines)
    # print(length)
    for i in range(length):
        if length - i <= 10: # and lines[i].strip(): # If you don't want to see empty raws comment second condition
            print(lines[i])


if __name__ == '__main__':
    reading()
