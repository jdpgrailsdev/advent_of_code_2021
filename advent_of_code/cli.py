"""Module used to provide a CLI for the application."""
import click
import re

from os import listdir
from os import path


@click.group()
def cli() -> None:
    """Entry point for the CLI to bind all commands together."""
    click.echo("Advent of Code 2021")


@cli.command()
def execute():
    """Executes each puzzle"""
    modules = listdir(path.dirname(__file__) + '/puzzles')

    for m in modules:
        if re.search("Puzzle\\d+\\.py", m):
            class_name = m.replace('.py', '')
            module = __import__(f"advent_of_code.puzzles.{class_name}")
            puzzles = getattr(module, 'puzzles')
            puzzle_module = getattr(puzzles, class_name)
            puzzle_class = getattr(puzzle_module, class_name)
            puzzle_instance = puzzle_class()
            puzzle_instance.execute()
