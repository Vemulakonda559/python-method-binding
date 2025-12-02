"""
Demonstrates method binding when accessed through the class vs an instance.
Matches: 'How Python Binds Methods' diagram.
"""

class Sample:
    def action(x, y):
        return x + y


# Class-level access → raw function (no binding)
print("Class access:", Sample.action(10, 20))   # x=10, y=20


# Instance-level access → bound method (self gets injected)
obj = Sample()
try:
    print("Instance access:", obj.action(10, 20))
except TypeError as e:
    print("Instance access raised TypeError:", e)
