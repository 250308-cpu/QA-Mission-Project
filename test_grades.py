from grades import is_pass, result


def test_is_pass():
    assert is_pass(90) == True
    assert is_pass(70) == True
    assert is_pass(20) == False


def test_result_pass():
    assert result(90) == "Pass"
