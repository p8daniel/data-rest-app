class NotValidError(Exception):
    def __init__(self, resource, message):
        Exception.__init__(self)
        self.resource = resource
        self.message = message


class CharacterNotValidError(NotValidError):
    def __init__(self, message):
        NotValidError.__init__(self, "Character:", message)
