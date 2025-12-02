"""
Tests that accessing a function through __dict__
returns the underlying raw function object.
"""

class Alpha:
    def work(x, y):
        return x * y


def test_raw_descriptor_access():
    raw = Alpha.__dict__['work']
    assert raw(3, 4) == 12
