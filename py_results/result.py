class Result():
    """Stores the result of an operation"""

    def __init__(self):
        self.ok_value = None
        self.err_value = None

    def ok(self, ok_value):
        """The result is a success, store the relevant return value"""
        self.ok_value = ok_value
        self.err_value = None

    def err(self, err_value):
        """The result is a fail, store the relevant return value"""
        self.err_value = err_value
        self.ok_value = None

    def is_ok(self):
        return self.ok_value is not None

    def is_err(self):
        return self.err_value is not None