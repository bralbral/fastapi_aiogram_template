import click

from .utils import configure_webserver


@click.command()
def start():
    s = configure_webserver()
    s.run()


__all__ = ["start"]
