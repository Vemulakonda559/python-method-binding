"""
Tests that instance-level access injects 'self'
and raises TypeError when the signature mismatches.
"""

class Demo:
    def compute(a, b):
        return a + b


def test_instance_binding_causes_type_error():
    d = Demo()
    try:
        d.compute(10, 20)
        assert False, "Expected TypeError due to self injection"
    except TypeError:
        assert True
