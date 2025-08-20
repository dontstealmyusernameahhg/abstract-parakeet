from abc import ABC, abstractmethod

class Abs_Class(ABC):
    def print_value(self, x):
        print("passed value: ", x)

    @abstractmethod
    def task(self):
        pass

class TestClass(Abs_Class):
    def task(self):
        print("we are inside test class")

test_obj = TestClass()
test_obj.print_value(10)
test_obj.task()