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
	def __init__(self,petType,breed,name,cost):
		self.petType=petType
		self.breed=breed
		self.name=name
		self.cost=cost
		
	def __repr__(self):
		return "Pet<{}-{}#{}:{:3.2f}>".format(self.petType,self.breed,self.name,self.cost)
```

and then create instances of the 'Pet' class like this.

```
	patty = Pet('dog','dalmation','Patty',20)
	cole = Pet('dog','pug','Cole',18)
	brandon = Pet('cat','demon','Boo',4)
	tweety = Pet('bird',"Canary','Tweety',8)
```

You can create a Petstore Object like this:

```
class PetStore:
	pets = {"cats":list(),"dogs":list(),"birds":list(),"fishs":list()}

	def getPets( self, t ):
		k = "{}s".format(t)
		return self.pets[ k ]
	
	def addPet( self, pet ):
		try:
  			l = self.getPets(pet.petType)
  			l.append(pet)
		except:
  			print("We don't carry pets of type {}".format(pet.petType))
```

You can find the first Item in a list with filtering and the 'next' function

```
l = list(range(10))
matches = list(x for x in l if x>6)
first = next((x for x in l if x>6))
```

so to find a particular pet in the petstore, you would need to get the list for the pet type, and then find the pet by name.
```
ps = PetStore()

l = ps.getPets('dogs')
myPet = next((p for p in l if p.name=='Patty'))

```

Your assignment is to add a function to the pet store that will 
take the pet type (e.g. 'dog', 'cat', 'fish', etc) and the pet name
and return the Pet Object. The logic for doing this is already done for you
in the code just above this comment. You only need to add a function to the 
petstore that will perform this logic

```	
	def getPet( self, petType, name ):
		# do the logic above
```

Test by calling your new function on the petstore, 
e.g. 
```myDog = ps.getPet('dog','Patty')`
print(myDog)```
