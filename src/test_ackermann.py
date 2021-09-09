def test_ackermann():
    from ackermann import ackermann
    assert ackermann(0, 0) == 1
    assert ackermann(0, 1) == 2
    assert ackermann(0, 2) == 3
    assert ackermann(0, 3) == 4
    assert ackermann(0, 4) == 5
    assert ackermann(1, 0) == 2
    assert ackermann(1, 1) == 3
    assert ackermann(1, 2) == 4
    assert ackermann(1, 3) == 5
    assert ackermann(1, 4) == 6
    assert ackermann(2, 0) == 3
    assert ackermann(2, 1) == 5
    assert ackermann(2, 2) == 7
    assert ackermann(2, 3) == 9
    assert ackermann(2, 4) == 11
    assert ackermann(3, 0) == 5
    assert ackermann(3, 1) == 13
    assert ackermann(3, 2) == 29
    assert ackermann(3, 3) == 61
    assert ackermann(3, 4) == 125
