import pytest

def test_passing():
    email = "mickey12922@gmail.com"
    assert email == "luke@stacklok.com"
    with pytest.raises:
        raise ("This is a configuration error")

def test_failing():
    email = "johnsmith222@hotmail.com"
    assert email == "jeffbrown1222@bbc.com"
    with pytest.raises():
        raise ("This is a configuration error")
