"""
4. Metaclasses
Write a metaclass that logs every time a new class is created using it.
"""





class MetaclassLogger(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class TestClass1(metaclass=MetaclassLogger):
    pass
class TestClass2(TestClass1):
    pass


# Creating an instance of TestClass
my_instance = TestClass1()
my_instance = TestClass2()


