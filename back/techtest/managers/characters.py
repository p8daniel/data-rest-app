from techtest.models.character import Character, Hat, HatColor
from techtest.errors import CharacterNotFoundError, ColorNotFoundError, \
    CharacterNotValidError, ParameterNotFoundError


def get_character_by_id(character_id):
    character = Character.get_or_none(id=character_id)
    if character is None:
        raise CharacterNotFoundError(character_id)
    return character


def check_character(name, age, weight, human, hat):
    message = ""
    if human is False and hat is not None:
        message = "If character is not human it cannot have a hat"

    if int(weight) > 80 and human is True and int(age) <= 10:
        message = "If the weight is greater than 80 and character is " \
                  "a human, the age must be greater than 10"

    if int(age) < 0:
        message = "Age should be positive"

    if 'p' in name.lower() and hat == 'YELLOW':
        message = "Hat cannot be YELLOW if the name contain the letter 'p'"

    if message != "":
        raise CharacterNotValidError(message)


def create_character(name, age, weight, human, hat=None):
    if hat is not None:
        selected_hat_color = HatColor.get_or_none(label=hat)
        if selected_hat_color is None:
            raise ColorNotFoundError(hat)
        hat = Hat.create(color=selected_hat_color)
    else:
        hat = None
    character = Character.create(
        name=name, age=age, weight=weight, human=human, hat=hat)
    return get_character_by_id(character.id)


def update_character(character_id, parameter, new_value):
    character = get_character_by_id(character_id)
    if parameter not in character.get_small_data().keys():
        raise ParameterNotFoundError(parameter)

    if parameter == 'hat':
        if new_value != 'None':
            selected_hat_color = HatColor.get_or_none(label=new_value)
            if selected_hat_color is None:
                raise ColorNotFoundError(new_value)
            new_value = Hat.create(color=selected_hat_color)
        else:
            new_value = None

    character.update(**{parameter: new_value}).where(
        Character.id == character.id).execute()

    return get_character_by_id(character.id)


def read_characters():
    characters = Character.select()
    return characters


def delete_character(character_id):
    character = get_character_by_id(character_id)
    character_hat = Hat.get_or_none(id=character.hat)
    character.delete_instance()
    if character_hat is not None:
        character_hat.delete_instance()
    return True
