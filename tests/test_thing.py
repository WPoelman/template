import pytest


def test_thing():
    assert True

    with pytest.raises(ValueError, match="Invalid value"):
        raise ValueError("Invalid value")
