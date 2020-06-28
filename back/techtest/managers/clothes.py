from techtest.models.character import Hat


def read_hats():
    hats = Hat.select()
    return hats
