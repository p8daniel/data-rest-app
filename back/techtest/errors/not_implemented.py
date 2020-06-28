class NotImplementedError(Exception):
    def __init__(self, message, item):
        Exception.__init__(self)
        self.message = message
        self.item = item


class FileFormatNotImplementedError(NotImplementedError):
    def __init__(self, item):
        NotImplementedError.__init__(
            self, "File extension not yet supported", item)


class DataTypeNotImplementedError(NotImplementedError):
    def __init__(self, item):
        NotImplementedError.__init__(
            self, "Type of data not yet implemented:", item)
