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


class TestRawResult(unittest.TestCase):
    def test_shouldNotAllowAmbiquousStates(self):
        result = Result(ok_value="Success!", err_message="Fail!")
        self.assertEqual(result.is_ok(), False)
        self.assertEqual(result.is_err(), True)
        self.assertEqual(result.unwrap(), "Fail!")

    def test_shouldBeUsableByItself(self):
        result = Result(ok_value="Success!")
        self.assertEqual(result.is_ok(), True)
        self.assertEqual(result.is_err(), False)
        self.assertEqual(result.unwrap(), "Success!")


class TestOperatorsAndUtils(unittest.TestCase):
    def test_shouldSupportEqualityOperator(self):
        self.assertTrue(Ok(42) == Ok(42))
        self.assertTrue(Ok(None) == Ok(None))
        self.assertTrue(Err("Nope!") == Err("Nope!"))

        self.assertFalse(Ok(41) == Ok(42))
        self.assertFalse(Ok("Nope!") == Err("Nope!"))
        self.assertFalse(Ok(None) == Err("Nope!"))

        self.assertTrue(Result(42) == Ok(42))
        self.assertTrue(Result(ok_value=None, err_message="Nope!") == Err("Nope!"))

    def test_shouldSupportUnequalityOperator(self):
        self.assertTrue(Ok(41) != Ok(42))
        self.assertTrue(Err("Nope!") != Err("Error!"))

    def test_shouldBeRepresentable(self):
        self.assertEqual(repr(Ok(42)), "Ok(42)")
        self.assertEqual(repr(Err("Nope!")), "Err(Nope!)")
        self.assertEqual(repr(Result(42)), "Ok(42)")
        self.assertEqual(repr(Result(ok_value=None, err_message="Nope!")), "Err(Nope!)")


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
