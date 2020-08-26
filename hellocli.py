#!/usr/bin/env python
import click
from hello import marco

@click.command()
@click.option('--name')
def callmarco(name):
    result = marco(name)
    click.echo(click.style(f'{result}', bg='blue', fg='white')) 

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    callmarco()

