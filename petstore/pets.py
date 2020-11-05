from petstore import PetStore, Pet


def showPets( Type, petList ):
	print( Type,':')
	for i, d in enumerate(petList):
		print("{:>4}: {:>10} - ${:3.2f}".format(i,d.name,d.cost))
	
 

# Create a new PetStore
ps = PetStore()

# Create some pets 
patty = Pet('dog','Dalmation','Patty',20)
cole = Pet('dog','Pug','Cole',14)
rufus = Pet('dog','Rottwieler','Rufus',16)
jaws = Pet('fish','Great White', "Jabber Jaw",40)

# add the pets to the store
ps.addPet( patty )
ps.addPet( cole )
ps.addPet( rufus )
ps.addPet( jaws )

# Show all of the dogs
# dogs = ps.getPets('dog')
#print('Dogs:')
#for i, d in enumerate(dogs):
#	print("{:>4}: {:>10} - ${:3.2f}".format(i,d.name,d.cost))


# Show all of the dogs
dogs = ps.getPets('dog')
fishes = ps.getPets('fish')
showPets('Dog',dogs)
showPets('Fish', fishes)




# find a dog in the petstore named 'Patty'
l = ps.getPets('dog')
myPet = next((p for p in l if p.name=='Patty'))
print(myPet)

# Your assignment is to add a function to the pet store that will 
# take the pet type (e.g. 'dog', 'cat', 'fish', etc) and the pet name
# and return the Pet Object. The logic for doing this is already done for you
# in the code just above this comment. You only need to add a function to the 
# petstore that will perform this logic
#	
#	def getPet( self, petType, name ):
#		# do the logic above
#
# Test by calling your new function on the petstore, 
# e.g. 
# myDog = ps.getPet('dog','Patty')
# print(myDog)
