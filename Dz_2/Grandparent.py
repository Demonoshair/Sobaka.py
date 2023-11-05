class Grandparent:
    height = 170
    satieti = 100
    age = 60



class Parent(Grandparent):
    age=40


class Child(Parent):
    height = 50

nick=Child

print(nick.height)
print(nick.satieti)
print(nick.age)