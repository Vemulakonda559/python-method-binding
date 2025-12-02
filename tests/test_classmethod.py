"""
Tests that class methods receive 'cls' as the first argument
for both class and instance access.
"""

class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count


def test_classmethod_class_access():
    Counter.count = 0
    assert Counter.increment() == 1


def test_classmethod_instance_access():
    Counter.count = 0
    c = Counter()
    assert c.increment() == 1
