"""Module used to provide a CLI for the application."""
import click

from advent_of_code.puzzles.Puzzle01 import Puzzle01


@click.group()
def cli() -> None:
    """Entry point for the CLI to bind all commands together."""
    click.echo("Advent of Code 2021")


@cli.command()
def execute():
    """Executes each puzzle"""
    puzzle_01 = Puzzle01()
    puzzle_01.execute()
