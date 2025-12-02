"""
Tests that static methods are not bound and behave
as ordinary functions for both class and instance access.
"""

class Utility:
    @staticmethod
    def add(a, b):
        return a + b


def test_staticmethod_class_access():
    assert Utility.add(5, 7) == 12


def test_staticmethod_instance_access():
    u = Utility()
    assert u.add(5, 7) == 12
