import unittest
from py_results import Result, Ok, Err


class TestCreateResult(unittest.TestCase):
    def test_emptyResultShouldNotBeOk(self):
        blank_result = Result()
        self.assertEqual(blank_result.is_ok(), False)

    def test_successResultShouldBeOk(self):
        ok_result = Ok("Success!")
        self.assertEqual(ok_result.is_ok(), True)
        self.assertEqual(ok_result.is_err(), False)

    def test_failResultShouldNotBeOk(self):
        fail_result = Err("Epic fail!")
        self.assertEqual(fail_result.is_ok(), False)
        self.assertEqual(fail_result.is_err(), True)


class TestUnwrapResult(unittest.TestCase):
    def test_shouldUnwrapEmptyResultAsNone(self):
        blank_result = Result()
        self.assertEqual(blank_result.unwrap(), None)

    def test_shouldUnwrapSuccessResultAsValue(self):
        ok_result = Ok(123)
        self.assertEqual(ok_result.unwrap(), 123)

    def test_shouldUnwrapFailResultAsErrorMessage(self):
        fail_result = Err("Something went wrong...")
        self.assertEqual(fail_result.unwrap(), "Something went wrong...")
