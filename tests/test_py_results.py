import unittest
from py_results import Result, Ok, Err


class TestCreateResult(unittest.TestCase):
    def test_successResultShouldBeOk(self):
        ok_result = Ok("Success!")
        self.assertEqual(ok_result.is_ok(), True)
        self.assertEqual(ok_result.is_err(), False)

    def test_failResultShouldNotBeOk(self):
        fail_result = Err("Epic fail!")
        self.assertEqual(fail_result.is_ok(), False)
        self.assertEqual(fail_result.is_err(), True)


class TestUnwrapResult(unittest.TestCase):
    def test_shouldSupportNoneAsSuccessValue(self):
        blank_result = Ok(None)
        self.assertEqual(blank_result.unwrap(), None)

    def test_shouldUnwrapSuccessResultAsValue(self):
        ok_result = Ok(123)
        self.assertEqual(ok_result.unwrap(), 123)

    def test_shouldUnwrapFailResultAsErrorMessage(self):
        fail_result = Err("Something went wrong...")
        self.assertEqual(fail_result.unwrap(), "Something went wrong...")


def int_divide(a: int, b: int) -> Result[int]:
    if b == 0:
        return Err("Division by zero")
    return Ok(a // b)


class TestUseCaseIntDivide(unittest.TestCase):
    def test_divideByZeroShouldReturnError(self):
        result = int_divide(10, 0)
        self.assertIsInstance(result, Err)
        self.assertEqual(result.is_ok(), False)
        self.assertEqual(result.is_err(), True)
        self.assertEqual(result.unwrap(), "Division by zero")

    def test_divideByNonZeroShouldReturnOk(self):
        result = int_divide(10, 2)
        self.assertIsInstance(result, Ok)
        self.assertEqual(result.is_ok(), True)
        self.assertEqual(result.is_err(), False)
        self.assertEqual(result.unwrap(), 5)
