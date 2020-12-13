from app.calc import add


def test_add_numbers():
    """Test that two numbers are added together"""
    assert add(3, 8) == 11
