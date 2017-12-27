class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        return '< "{0}", "{1}" >'.format(self.type, self.value or '')
