class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        # Infer storage attribute name to avoid collisions
        self.storage_name = f"_{name}"

    def __get__(self, instance, owner):
        # Access from the class itself returns the descriptor object
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        # Type validation check
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Expected {self.expected_type.__name__}, got {type(value).__name__}"
            )
        # Store the value using the instance's __dict__
        setattr(instance, self.storage_name, value)


class Person:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Valid instantiation and modification
p = Person("Alice", 30)
print(p.name)  # Output: Alice
print(p.age)   # Output: 30

# Attempting an invalid assignment
try:
    p.age = "thirty"
except TypeError as e:
    print(e)  