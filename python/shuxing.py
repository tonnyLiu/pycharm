class Person():
    def fget(self):
        return self._age

    def fset(self, age):
        self._age = int(age)

    def fdel(self):
        self._name = "NoName"

    age = property(fget, fset, fdel, "success")

p1 = Person()
p1.age = 34.6
print(p1.age)
