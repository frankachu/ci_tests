import pytest
from app import square, cube, check

def test_square():
    assert square(2) == 4
    assert square(-3.5) == 12.25
    assert square(0) == 0
    with pytest.raises(ValueError):
        square("text")    # "text" is not accecptable type

def test_cube():
    assert cube(2.0) == 8
    assert cube(-3) == -27
    assert cube(0.0) == 0
    with pytest.raises(ValueError):
        cube("text")    # "text" is not accecptable type