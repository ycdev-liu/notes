class A:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

a = A()
a.age = 18
print(a.age)

from functools import 