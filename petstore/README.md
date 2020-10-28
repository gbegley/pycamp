# Petstore

For this assignment, we are going to create and work classes and objects.
A class is a structure that that can contain other named properties or attributes which can be strings, numbers, or even other objects.
For example:

```
class MyClass:
  x = 5
```

can be used to create MyClass objects with an 'x' property whose initial value is 5.
You can then create an instance of MyClass with

`mc = MyClass()`

You can allow initialization of an objects properties by defining an `__init__` method on the object. To initialize the 'x' property of a 'MyClass' object you might define the class like this

```
class MyClass:
	def __init__(self,x):
		self.x = x
```

And then create an intance of MyClass with `m = MyClass(10)`, which would create a new Object instance of the 'MyClass' class the 'x' property intialized to 10.




A Pet Class might look like

```
class Pet:
	def __init__(self,type,breed,name)
		self.type=type
		self.breed=breed
		self.name=name
```

and then create instances of the 'Pet' class like this.

```
	patty = Pet('dog','dalmation','Patty')
	cole = Pet('dog','pug','Cole')
	brandon = Pet('cat','demon','Boo')
	tweety = Pet('bird',"Canary','Tweety')
```

You can create a Petstore Object like this:

```
class Petstore:
	pets = {"cats":list(),"dogs":list(),"birds":list()}

	def getPets( self, type ):
		k = pet.type + 's'
		return self.pets[ k ]
	
	def add( self, pet ):
		try:
  			self.getPets(pet.type).append(pet)
		except:
  			print("We don't carry pets of type {}".format(k))
```

You can find the first Item in a list with filtering and the 'next' function

```
l = list(range(10))
matches = list(x for x in l if x>6)
first = next((x for x in l if x>6))
```

so to find a particular pet in the petstore, you would need to get the list for the pet type, and then find the pet by name.
```
ps = # the PetStore

l = ps.getPets('dogs')
myPet = next((p for p in l if p.name=='Patty'))

```
