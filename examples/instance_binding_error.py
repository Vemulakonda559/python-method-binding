"""
Shows that calling an undecorated method via an instance injects 'self'
and can cause signature mismatches.
"""

class Demo:
    def compute(a, b):
        return a + b


d = Demo()

try:
    # Fails because 'a' becomes the instance
    print(d.compute(3, 4))
except TypeError as e:
    print("Error due to self injection:", e)
