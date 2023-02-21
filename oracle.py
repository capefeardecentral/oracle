import click
from commands import code


@click.group()
def cli():
    pass

cli.add_command(code.unit_test)

if __name__ == '__main__':
    cli()
