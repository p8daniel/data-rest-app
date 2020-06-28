import click
import json

from techtest.managers import characters
from techtest.managers import clothes
from techtest.managers.data import load_data_from_csv, store_data_to_db


@click.group()
def cli():
    click.echo('## Python_technical_test ##')


@cli.group()
def get():
    pass


@get.command('characters')
@click.option('--character_id')
def get_characters(character_id):
    for character in characters.read_characters():
        if character_id is None or character.id == int(character_id):
            click.echo(f'Character: {character.get_small_data()}')


@get.command('hats')
def get_hats():
    for hat in clothes.read_hats():
        click.echo(f'Hat: {hat.get_small_data()}')


@cli.group()
def add():
    pass


@add.command('character')
@click.argument('name')
@click.argument('age')
@click.argument('weight')
@click.argument('human')
@click.option('--hat')
def add_character(name, age, weight, human, hat):
    human = json.loads(human.lower())
    characters.check_character(name, age, weight, human, hat)
    character = characters.create_character(name, age, weight, human, hat)
    click.echo(f"Character created: {character.get_small_data()}")


@cli.group()
def delete():
    pass


@delete.command('character')
@click.argument('character_id')
def delete_character(character_id):
    characters.delete_character(character_id)
    click.echo('Character deleted')


@cli.group()
def update():
    pass


@update.command('character')
@click.argument('id')
@click.argument('parameter')
@click.argument('new_value')
def update_character(id, parameter, new_value):
    if parameter == 'human':
        new_value = json.loads(new_value.lower())
    updated_character = characters.update_character(id, parameter, new_value)
    click.echo(f'Character updated: {updated_character.get_small_data()}')


@cli.group()
def load():
    pass


@load.command('data')
@click.argument('file_path')
def load_datatable(file_path):
    data = load_data_from_csv(file_path)
    store_data_to_db(data, 'csv')
    click.echo('Data loaded')
