import pytest

def test_passing():
    email = "lukehinds@gmail.com"
    assert email == "luke@stacklok.com"
    with pytest.raises:
        raise ("This is a configuration error")

def test_failing():
    email = "johnsmith@hotmail.com"
    assert email == "jeffbrown@bbc.com"
    with pytest.raises():
        raise ("This is a configuration error")
