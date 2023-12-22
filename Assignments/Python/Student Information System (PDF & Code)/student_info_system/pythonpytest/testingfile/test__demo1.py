import pytest

def test_demo():
    assert 'prakhar' == 'prakhar', 'both strings are equal'

@pytest.mark.test1
def test_demo2():
    assert 'prakhar mishra' == 'prakhar', 'both strings are not equal'