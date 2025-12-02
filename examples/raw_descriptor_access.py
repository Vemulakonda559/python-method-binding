"""
Shows how to retrieve the raw function object from the class namespace.
Helpful for understanding that methods are stored as plain functions.
"""

class Alpha:
    def work(x, y):
        return x * y


# Direct dictionary access returns raw function
raw_fn = Alpha.__dict__['work']

print("Raw function call:", raw_fn(3, 4))   # Same as Alpha.work(3, 4)
