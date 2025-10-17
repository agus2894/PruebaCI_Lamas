from app import suma

def test_suma():
    assert suma(1, 2) == 3
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(-1, -1) == -2
    assert suma(2.5, 2.5) == 5.0
    assert suma(1000, 2000) == 3000


    