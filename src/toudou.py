import datetime

import click
import uuid

from dataclasses import dataclass


@dataclass
class Todo:
    id: uuid.UUID
    task: str
    date: datetime
    complete: bool



@click.group()
def cli():
    pass


@cli.command()
@click.option("-t", "--task", prompt="Your task", help="The task to remember.")
def display(task: str):
    todo = Todo(uuid.uuid4(), task)
    click.echo(todo)
