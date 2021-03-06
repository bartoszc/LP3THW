from abc import ABCMeta, abstractmethod

## Animal is-a object (yes, sort of confusion) look at the extra credit
class Animal(object):
    pass

## is-a
class Dog(Animal):

    def __init__(self, name):
        ## has-a
        self.name = name

## is-a
class Cat(Animal):

    def __init__(self, name):
        ## has-a
        self.name = name

## is-a
class Person(object):
    total = 0
    def __init__(self, surname, name = 'Bart'):
        ## has-a
        self.name = name
        self.__surname = surname

        ## Person has-a pet of some kind
        self.pet = None
        Person.total += 1

    @staticmethod
    def status():
        print("\nThe total number of persons is", Person.total)

    def __str__(self):
        human = self.name + self.__surname
        return human

## is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? inheritance, parent method
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary

## is-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass


print(Person.status())
## rover is-a Dog
rover = Dog("Rover")

## is-a
satan = Cat("Satan")

## is-a
mary = Person("Mary")

## has-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## is-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()

print(Person.total)
print(Person)
print(mary)
