# definition of class Parent
class Parent(object):

    # method
    def override(self):
        print("PARENT override()")

    # method
    def implicit(self):
        print("PARRENT implicit()")

    # method
    def altered(self):
        print("PARENT altered()")

# class Child inherits from Parent
class Child(Parent):

    # ovverides funtion from Parent
    def override(self):
        print("CHILD override()")

    # ovverides function from Parent
    def altered(self):
        print("CHILD, BEFORE PARENT altered()") # ovverides
        super(Child, self).altered() # using function from Parent (super keyword)
        print("CHILD, AFTER PARENT altered()") # again, ovverides function from Parent

dad = Parent() # creates instance for Parent class
son = Child() # creates instance for child class

dad.implicit() # calling implicit function on dad object
son.implicit() # caling implicit function on son object (inherited from Parent class)

dad.override() # calling ovveride function on dad object
son.override() # caling ovveride function on son object which ovverides function from Parent

dad.altered()  # calling altered function on dad object
son.altered()  # caling altered function on son object - first - ovverides, second - calling Parent class, third - ovverides
