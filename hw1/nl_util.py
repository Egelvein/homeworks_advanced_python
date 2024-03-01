# python3 nl_util.py --textfile example.txt

import click
import sys

@click.command()
@click.option('--textfile',
        default='--',
        help='Textfile for reading and processing')


def reading(textfile='--'):
    if textfile == '--':
        return sys.stdin
    else:
        with open(textfile, 'r') as file:
            lines = file.readlines()

    for i in range(len(lines)):
	    lines[i] = lines[i][:-1]
    for i in range(len(lines)):
        if lines[i].isspace() or lines[i].strip() == '':
            pass
        else:
            print(f'{i+1} {lines[i]}')


if __name__ == '__main__':
    reading()
