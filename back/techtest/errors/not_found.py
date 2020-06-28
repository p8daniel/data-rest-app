class NotFoundError(Exception):
    def __init__(self, resource, resource_id):
        Exception.__init__(self)
        self.resource = resource
        self.resource_id = resource_id


class CharacterNotFoundError(NotFoundError):
    def __init__(self, resource_id):
        NotFoundError.__init__(self, "Character", resource_id)


class ColorNotFoundError(NotFoundError):
    def __init__(self, resource_id):
        NotFoundError.__init__(self, "Color", resource_id)


class ParameterNotFoundError(NotFoundError):
    def __init__(self, resource_id):
        NotFoundError.__init__(self, "Parameter", resource_id)
