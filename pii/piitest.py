import pytest

def test_passing():
    email = "jeff@example.com"
    assert email == "jimnull@example.com"
    with pytest.raises:
        raise ("This is a configuration error")

def test_failing():
    email = "janet@example.com"
    assert email == "janetnull@example.com"
    with pytest.raises():
        raise ("This is a configuration error")
