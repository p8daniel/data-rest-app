import json

from click.testing import CliRunner
from techtest.cli import cli


def test_techtest_cli():
    runner = CliRunner()

    # Add a new character
    result = runner.invoke(cli,
                           ['add', 'character', 'Person1', '45', '77', 'True',
                            '--hat', 'GREEN'])
    assert result.exit_code == 0
    created_character = result.output.split('\n')[1].lstrip(
        'Character created: ')
    json_acceptable_string = created_character.replace("'", "\"")
    character = json.loads(json_acceptable_string.replace('True', 'true'))

    # Retrive the new character
    result = runner.invoke(cli, ['get', 'characters', '--character_id',
                                 character['id']])
    assert result.exit_code == 0
    assert result.output.split('\n')[1].lstrip(
        'Character: ') == created_character

    # Delete the created character
    result = runner.invoke(cli, ['delete', 'character', str(character['id'])])
    assert result.exit_code == 0

    # Si human est faux, il est impossible d’avoir un hat associé
    result = runner.invoke(cli,
                           ['add', 'character', 'Person1', '45', '77', 'False',
                            '--hat', 'GREEN'])
    assert result.exit_code == 1

    # Si weight est supérieur à 80, et human est vrai, l’âge doit être
    # supérieur à 10
    result = runner.invoke(cli,
                           ['add', 'character', 'Person1', '9', '89', 'True',
                            '--hat', 'GREEN'])
    assert result.exit_code == 1

    # L'âge est forcément un nombre positif
    result = runner.invoke(cli,
                           ['add', 'character', 'Person1', '"-45"', '77',
                            'True', '--hat', 'GREEN'])
    assert result.exit_code == 1

    # Si name contient la lettre p, le hat ne peut pas être YELLOW
    result = runner.invoke(cli,
                           ['add', 'character', 'Person1', '"-45"', '77',
                            'True', '--hat', 'YELLOW'])
    assert result.exit_code == 1

    # Load a sample table with data
    result = runner.invoke(cli, ['load', 'data', 'datatable.csv'])
    assert result.exit_code == 0
