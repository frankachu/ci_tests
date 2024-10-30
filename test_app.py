import pytest
from app import square, cube, check

def test_square():
    assert square(2) == 4
    assert square(-3.5) == 12.25
    assert square(0) == 0
    with pytest.raises(ValueError):
        square("text")    # Ошибка, так как "text" не является float

def test_cube():
    assert cube(2.0) == 8.0
    assert cube(-3.0) == -27.0
    assert cube(0.0) == 0.0
    with pytest.raises(ValueError):
        cube("text")    # Ошибка, так как "text" не является float