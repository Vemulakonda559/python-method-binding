"""
Illustrates that static methods do not receive any implicit first argument.
Matches: '@staticmethod' section in the method types diagram.
"""

class Utility:
    @staticmethod
    def add(a, b):
        return a + b


# Class call
print("Class access:", Utility.add(5, 6))

# Instance call
u = Utility()
print("Instance access:", u.add(5, 6))
