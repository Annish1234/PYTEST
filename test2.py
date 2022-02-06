import pytest

def test4():
    assert False

    
@pytest.mark.home
def  test5():
    assert 100==100

def test6():
    assert "annish"=="ANNISH"

@pytest.mark.home
def test_login():
    assert "admin"=="admin"