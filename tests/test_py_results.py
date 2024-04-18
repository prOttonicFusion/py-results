import unittest
from py_results import result


class TestCreateResult(unittest.TestCase):
    def test_emptyResultShouldNotBeOk(self):
        blank_result = result.Result()
        self.assertEqual(blank_result.is_ok(), False)

    def test_successResultShouldBeOk(self):
        ok_result = result.Result()
        ok_result.ok("Success!")
        self.assertEqual(ok_result.is_ok(), True)
        self.assertEqual(ok_result.is_err(), False)

    def test_failResultShouldNotBeOk(self):
        fail_result = result.Result()
        fail_result.err("Epic fail!")
        self.assertEqual(fail_result.is_ok(), False)
        self.assertEqual(fail_result.is_err(), True)


class TestOverrideResult(unittest.TestCase):
    def test_shouldOverrideSuccessWithFail(self):
        fail_result = result.Result()
        fail_result.ok("Success!")
        fail_result.err("Uh, no it was a fail...")
        self.assertEqual(fail_result.is_ok(), False)
        self.assertEqual(fail_result.is_err(), True)

    def test_shouldOverrideFailWithSuccess(self):
        fail_result = result.Result()
        fail_result.err("Fail :(")
        fail_result.ok("No, a success!")
        self.assertEqual(fail_result.is_ok(), True)
        self.assertEqual(fail_result.is_err(), False)


class TestUnwrapResult(unittest.TestCase):
    def test_shouldUnwrapEmptyResultAsNone(self):
        blank_result = result.Result()
        self.assertEqual(blank_result.unwrap(), None)

    def test_shouldUnwrapSuccessResultAsValue(self):
        ok_result = result.Result()
        ok_result.ok(123)
        self.assertEqual(ok_result.unwrap(), 123)

    def test_shouldUnwrapFailResultAsErrorMessage(self):
        fail_result = result.Result()
        fail_result.err("Epic fail!")
        self.assertEqual(fail_result.unwrap(), "Epic fail!")
