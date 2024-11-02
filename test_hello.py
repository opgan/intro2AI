from hello import injest

def test_injest():
    assert injest().shape == (6, 3)