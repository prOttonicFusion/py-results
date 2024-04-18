from typing import TypeVar, Generic

T = TypeVar("T")


class Result(Generic[T]):
    def __init__(self, ok_value: T, err_message: str | None = None):
        self._ok_value = ok_value
        self._err_message = err_message

    def is_ok(self):
        return self._err_message is None

    def is_err(self):
        return self._err_message is not None

    def unwrap(self) -> T | str:
        """Unwrap the contained data, returning either the success value or the error message"""
        if self._err_message != None:
            return self._err_message

        return self._ok_value

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Result)
            and self._ok_value == other._ok_value
            and self._err_message == other._err_message
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __repr__(self) -> str:
        if self._err_message is not None:
            return f"Err({self._err_message})"
        return f"Ok({self._ok_value})"


class Ok(Result, Generic[T]):
    def __init__(self, value: T):
        super().__init__(ok_value=value)

    def unwrap(self) -> T:
        """Unwrap the contained value"""
        return self._ok_value


class Err(Result):
    def __init__(self, message: str):
        super().__init__(ok_value=None)
        self._err_message = message

    def unwrap(self) -> str:
        """Unwrap the error message"""
        return self._err_message
