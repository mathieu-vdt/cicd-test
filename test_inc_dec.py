import inc_dec

def test_increment():
    assert inc_dec.increment(5) == 6
    assert inc_dec.increment(-10) == -9
    assert inc_dec.increment(0) == 1
    print("Increment function passed all tests.")

def test_decrement():
    assert inc_dec.decrement(5) == 4
    assert inc_dec.decrement(-10) == -11
    assert inc_dec.decrement(0) == -1
    print("Decrement function passed all tests.")

if __name__ == "__main__":
    test_increment()
    test_decrement()