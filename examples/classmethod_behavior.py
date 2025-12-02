"""
Demonstrates classmethod behavior where 'cls' is injected for both
class-level and instance-level access.
Matches: '@classmethod' section in method types diagram.
"""

class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count


# Class call
print("Class access:", Counter.increment())

# Instance call
c = Counter()
print("Instance access:", c.increment())
