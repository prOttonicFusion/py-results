class Result:
    def __init__(self):
        self.ok_value = None
        self.err_message = None

    def is_ok(self):
        return self.ok_value is not None

    def is_err(self):
        return self.err_message is not None

    def unwrap(self):
        """Unwrap the contained data, returning either the success value or the error message"""
        if self.err_message != None:
            return self.err_message
        else:
            return self.ok_value


class Ok(Result):
    def __init__(self, value):
        super().__init__()
        self.ok_value = value


class Err(Result):
    def __init__(self, message):
        super().__init__()
        self.err_message = message
