# Understanding Python Method Binding Through the Descriptor Protocol

Python’s object model is elegant but subtly powerful.  
One of its most misunderstood behaviors is **method binding**—specifically:

- Why a function defined inside a class behaves differently when accessed through a **class** vs an **instance**.
- Why **no error** occurs when calling `ClassName.method(arg1, arg2)` even though the method “expects” a `self`.
- Why `instance.method(arg1, arg2)` *may* raise a `TypeError`.
- What roles `@staticmethod` and @classmethod actually play.
- How the descriptor protocol (`__get__`) governs all of this.

This document provides a clear and faithful explanation of the mechanism behind method binding in Python.

---

## 1. Functions Inside Classes Are Descriptors

A function defined inside a class is not automatically a method; it becomes one only when accessed through an instance.

### Example

```python
class Sample:
    def action(x, y):
        return x + y
```

Inside the class dictionary, the entry:

```python
Sample.__dict__['action']
```

is a **plain function object**, not a method.

Python transforms this into a **bound method** only when accessed through an instance.

This is because functions implement:

```python
function.__get__(instance, owner)
```

This descriptor method is the core of method binding.

---

## 2. What Happens When Accessing Through the Class?

Accessing:

```python
Sample.action
```

invokes:

```
function.__get__(instance=None, owner=Sample)
```

Since `instance=None`, the descriptor returns the **raw function** unchanged.

### Meaning:

- No `self` is injected  
- No binding occurs  
- You receive the plain function

Thus:

```python
Sample.action(10, 20)
```

executes as:

```python
action(10, 20)
```

with:

```
x = 10
y = 20
```

---

## 3. What Happens When Accessing Through an Instance?

Accessing:

```python
obj = Sample()
obj.action
```

invokes:

```
function.__get__(instance=obj, owner=Sample)
```

This creates a **bound method** where the instance is automatically injected:

```
x = obj
y = 10
```

So:

```python
obj.action(10, 20)
```

internally becomes:

```python
Sample.action(obj, 10, 20)
```

If the function does not accept this extra argument, Python raises:

```
TypeError: action() takes 2 positional arguments but 3 were given
```

---

## 4. Static Methods Remove Binding Entirely

```python
class Utility:
    @staticmethod
    def add(a, b):
        return a + b
```

`staticmethod` suppresses binding:

- No instance injected  
- No class injected  

So these behave identically:

```python
Utility.add(5, 6)
Utility().add(5, 6)
```

---

## 5. Class Methods Inject the Class Instead

```python
class Counter:
    @classmethod
    def increment(cls):
        return cls
```

The class method descriptor always injects the **class**:

- Class access → `cls = Counter`
- Instance access → `cls = Counter`

Thus, both forms call:

```python
increment(Counter)
```

---

## 6. The Role of __dict__ (Raw Access)

Accessing:

```python
Sample.__dict__['action']
```

bypasses the descriptor protocol entirely.

This returns the **raw function object**, unchanged.

---

## 7. Why ClassName.method() Works Without self

Because class attribute access does **not** bind, Python never injects `self`.

Thus:

```python
Sample.action(10, 20)
```

is just a plain function call, not a method call.

---

## 8. Matching Examples in This Repository

The `examples/` directory demonstrates:

- Class vs instance access  
- Signature mismatch  
- Static methods  
- Class methods  
- Raw descriptor access  

---

## 9. Matching Tests in This Repository

The `tests/` directory validates:

- Class access → no binding  
- Instance access → binding  
- Static method behavior  
- Class method behavior  
- Raw access via `__dict__`  

Run using:

```
pytest
```

---

## 10. Diagrams

Two diagrams in the `docs/` directory:

- `python-method-binding-diagram.svg`
- `python-method-binding-method-types.svg`

---

## 11. Summary

Python’s method binding rules come entirely from the descriptor protocol.

| Access Type      | Descriptor Behavior | First Arg Injected |
|------------------|----------------------|---------------------|
| Class access     | No binding           | None                |
| Instance access  | Bound method         | Instance (`self`)   |
| @staticmethod    | No binding           | None                |
| @classmethod     | Bound method         | Class (`cls`)       |

Understanding this reveals the elegant consistency of Python’s object model.
