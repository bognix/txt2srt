class Error(Exception):
    pass


class BadTypeException(Error):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)