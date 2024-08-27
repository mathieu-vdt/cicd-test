import sum

# test_sum.py


def test_sum():
    assert sum.add(2, 3) == 5
    assert sum.add(0, 0) == 0
    assert sum.add(-1, 1) == 0
    assert sum.add(10, -5) == 5

test_sum()