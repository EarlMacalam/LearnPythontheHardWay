## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_age(self):
        print(f"Hi my name is {self.name}.")
        print(f"I'm {self.age} years old.")


# burito = Animal("Burito", 8)
# burito.name_age()

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name, age, cute):
        super().__init__(name, age)
        ## dog has-a name you want to call it
        self.cute = cute

    def cuteness(self):
        print(f"My level of cuteness is {self.cute}.")

x = Dog("mema", 7, "loki")
x.name_age()
x.cuteness()

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name you want to call it
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name you want to name him/her
        self.name = name
        ## Person has-a pet of some kinds
        self.pet = None

## Employeee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## I need to research on this
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has a pet rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## haryy is a Halibut
harry = Halibut()


# class can be an argument just like an object
class A():
    def __init__(self):
        print("Hello")

    def cat(self,name):
        print(f"{name}")
        print(f"{self}")


A.cat(A(),"Tom")
