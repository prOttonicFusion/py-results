from typing import TypeVar, Generic

T = TypeVar("T")


class Result(Generic[T]):
    def __init__(self, ok_value, err_message: str | None = None):
        self.ok_value = ok_value
        self.err_message = err_message

    def is_ok(self):
        return self.ok_value is not None

    def is_err(self):
        return self.err_message is not None

    def unwrap(self) -> T | str:
        """Unwrap the contained data, returning either the success value or the error message"""
        if self.err_message != None:
            return self.err_message

        return self.ok_value


class Ok(Result, Generic[T]):
    def __init__(self, value: T):
        super().__init__(ok_value=value)

    def unwrap(self) -> T:
        """Unwrap the contained value"""
        return self.ok_value


class Err(Result):
    def __init__(self, message: str):
        super().__init__(ok_value=None)
        self.err_message = message

    def unwrap(self) -> str:
        """Unwrap the error message"""
        return self.err_message
