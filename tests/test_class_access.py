"""
Tests that class-level access returns raw function
and does not inject an instance.
"""

class Sample:
    def action(x, y):
        return x + y


def test_class_access_raw_function():
    assert Sample.action(10, 20) == 30
