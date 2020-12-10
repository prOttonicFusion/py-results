from py_results import result


def test_createEmptyResult():
    '''Blank result object'''
    blank_result = result.Result()
    assert blank_result.is_ok() == False and blank_result.is_err(
    ) == False, 'should be neither ok nor err'


def test_createSuccessResult():
    '''Result object with success status'''
    ok_result = result.Result()
    ok_result.ok("Success!")
    assert ok_result.is_ok() == True, 'is_ok() should return true'
    assert ok_result.is_err() == False, 'is_err() should return false'


def test_createFailResult():
    '''Result object with fail status'''
    fail_result = result.Result()
    fail_result.err("Epic fail!")
    assert fail_result.is_ok() == False, 'is_ok() should return false'
    assert fail_result.is_err() == True, 'is_err() should return true'


def test_overrideSuccessResult():
    '''Override success with fail result'''
    fail_result = result.Result()
    fail_result.ok("Success!")
    fail_result.err("Uh, no it was a fail...")
    assert fail_result.is_ok() == False, 'is_ok() should return false'
    assert fail_result.is_err() == True, 'is_err() should return true'


def test_overrideFailResult():
    '''Override fail with success result'''
    fail_result = result.Result()
    fail_result.err("Fail :(")
    fail_result.ok("No, a success!")
    assert fail_result.is_ok() == True, 'is_ok() should return true'
    assert fail_result.is_err() == False, 'is_err() should return false'
