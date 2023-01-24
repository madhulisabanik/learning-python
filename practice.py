# A dictionary is a set of unordered key, value pairs. In a dictionary, the keys must be unique and 
# they are stored in an unordered manner.

# Create Dictionary
person_info = {"city": "Kolkata", "name": "Ria", "food": "biriyani"}
print(person_info) # o/p - {'city': 'Kolkata', 'name': 'Ria', 'food': 'biriyani'}

# Get value from Dictionary
print(person_info["name"]) # o/p - Ria

# Get value of the dictionary using 'get' method
print(person_info.get("city")) # o/p - Kolkata

# Get the default value if key not present
print(person_info.get("place", "default")) # o/p - default

# Looping dictionary
for k, v in person_info.items():
    print("Key is: %s" % k)
    print("Value is: %s" % v)
    print("------------")

# Add element to dictionary
person_info["state"] = "Bengal"
print(person_info)

# Combine two dictionaries
food_info = {"dish": "Cake", "price": "10"}
person_info.update(food_info)
print(person_info) # o/p -{'city': 'Kolkata', 'name': 'Ria', 'food': 'biriyani', 'state': 'Bengal', 'dish': 'Cake', 'price': '10'}

# Delete element from dictionary
del person_info["food"]
print(person_info) # o/p - {'city': 'Kolkata', 'name': 'Ria', 'state': 'Bengal', 'dish': 'Cake', 'price': '10'}

# Pop item from dictionary (Better than del methos, as we can pass default value if key is not present)
print(person_info.pop("price", None))

# A set is an unordered collection data type with no duplicate elements. Sets are iterable and mutable.
# The elements appear in an arbitrary order when sets are iterated.

# Creatingset with a string that has some repeated characters
setA = set("HellowThere")
print(setA) # o/p - {'h', 'H', 'w', 'l', 'T', 'o', 'r', 'e'}

# Creating set with a list
setB = set(['C', 'C++', 'Python'])
print(setB) # o/p - {'Python', 'C++', 'C'}

# Add elements to a set
setA.add(8)
print(setA)

# Add a tuple (9, 10) to a set
setA.add((9, 10))
print(setA)

# Update Set (pass a list of element)
setA.update([11, 12])
print(setA)

# Update with a list and a new set
setA.update([13, 14], {15, 16})
print(setA)

# Note: Using add, elements can be added but can not add another iterable like set, list, or tuple. 
# Update can be used to add iterable or iterables of hashable elements.

# Removes element from set
setA.discard(8)
print(setA)

setA.remove(11)
print(setA)

# Note: Both discard and remove take a single argument, the element to be deleted from the set. 
# If the value is not present, discard() does not do anything. Whereas, remove will raise a KeyError exception.

# Set copy() - Creates a shallow copy of the set with which it is called
# Using assignment here instead of copy() will create a pointer to the already existing set.
shallow_copy_of_setA = setA.copy()
print(shallow_copy_of_setA)

# Set clear() Will remove all elements from set
shallow_copy_of_setA.clear()
print(shallow_copy_of_setA) # o/p - set()

# Popping an element from set
print(setA.pop())

# Print a new set with the values present in two sets
setC = setD = set()
setC.update([1, 2, 3, 7])
setD.update([2, 3, 4, 5])
print(setC & setD)

# Above operation and the method intersection shows same results
print(setC.intersection(setD))

# Set difference (-)
print(setC.difference(setD)) # Not working for me

# Set isdisjoint() returns true if intersection of sets is empty otherwise false
print(setC.isdisjoint(setD))
setE = set()
setE.update([9, 10])
print(setC.isdisjoint(setE)) # returns true as setC and setE has no elements in common

# difference_update()/(-=) setA.difference_update(setB) removes all elements of setB from setA
setC.difference_update(setD)
print("difference_update - ", setA)

# Similarly, setA.intersection_update(setB) removes elements from setA which are not present in the 
# intersection set of setA and setB.

# issubset() / (<=)
# setA.issubset(setB) returns True if setA is subset of setB, False if not.
print(setA.issubset(setB))
print(setB.issubset(setA))

# issuperset()
print(setA.issuperset(setB))

# Python Expressions:
# List comprehension
print([x for x in range(10)]) # o/p - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary comprehension { k, v for k in iterable }
print({x:x**2 for x in range(5)}) # o/p - {0: 0, 1: 1, 2: 4, 3: 9, 4: 16} (** - power of operator)

# Generator expression
print((x for x in range(10))) # o/p - <generator object <genexpr> at 0x7f64a09adb30>
print(list(x for x in range(10))) # o/p - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Conditional Expressions
x = "1" if True else "2"
print(x)

# Create Class
class Test:
    name = "Ria" # set an attribute `name` of the class
    
test = Test() # Classs Instantiation
print(test.name) # o/p - Ria

# class with attribute and method
class Snake:
    name = "Python"
    
    def change_name(self, new_name): # note that the first argument is self
        self.name = new_name # access the class attribute with the self keyword
        
snake = Snake()
print(snake.name)

snake.change_name("Anaconda")
print(snake.name)

# Provide the values for the attributes at runtime, using __init__ method
class Testing:
    def __init__(self, name):
        self.name = name
        
    def change_name(self, new_name):
        self.name = new_name
        
Test1 = Testing("Test 01")
Test2 = Testing("Test 02")

print(Test1.name)
print(Test2.name)

Test2.change_name("New Test 2")
print(Test2.name)

# Class Inheritance
class Walk:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        
    def has_walked(self):
        return "%s has walked %s km today" % (self.name, self.distance)
    
person1 = Walk("Ria", "10")
print(person1.has_walked())

class Till(Walk):
    def __init__(self, name, distance, till_where):
        Walk.__init__(self, name, distance)
        self.till_where = till_where
        
    def get_till_where(self):
        return "%s walked till %s" % (self.name, self.till_where)
    
person2 = Till("Subha", "25", "Sakher Bazar")
print(person2.has_walked())
print(person2.get_till_where())

# Python Composition: Instead of inheriting base class, instantiate base glass as an attribute to another class
class Till_Where():
    def __init__(self, name, distance, till_where):
        self.walk = Walk(name, distance)
        self.till_where = till_where
        
    def get_till_where(self):
        print(self.walk.has_walked())
        return "%s walked till %s" % (self.walk.name, self.till_where)
    
person3 = Till_Where("Rohit", "15", "Notunhat")
print(person3.get_till_where())

# Error and Exception
while True:
    try:
        user = int(input())
        if user < 0:
            raise ValueError("Please give positive number")
        else:
            print("User input: %s" % user)
    except ValueError as e:
        print(e)