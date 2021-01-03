#
# # Implicit Inheritance
# class Parent(object):
#
#     def implicit(self):
#         print("PARENT IMPLICIT()")
#
# class Child(Parent):
#     pass
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()
#
# # Override Explicitly
# class Parent(object):
#
#     def override1(self):
#         print("PARENT override()")
#
#     def another_fn(self):
#         print("ANOTHER fn")
#
# class Child(Parent):
#
#     def override(self):
#         print("asddd sads")
#
#     def another_fn(self):
#         print("ss fn")
#
# dad = Parent()
# son = Child()
#
# dad.override1()
# son.override1()
# dad.another_fn()
# son.another_fn()

#
# # Alter before or after
# class Parent(object):
#
#     def altered(self):
#         print("PARENT altered()")
#
# class Child(Parent):
#
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")
#
# dad = Parent()
# son = Child()
#
# dad.altered()
# son.altered()

# # All three combined
# class Parent(object):
#
#     def override(self):
#         print("PARENT override()")
#
#     def implicit(self):
#         print("PARENT implicit()")
#
#     def altered(self):
#         print("PARENT altered()")
#
# class Child(Parent):
#
#     def override(self):
#         print("CHILD override()")
#
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()
#
# dad.override()
# son.override()
#
# dad.altered()
# son.altered()

# Composition
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()
son.implicit()
son.override()
son.altered()
