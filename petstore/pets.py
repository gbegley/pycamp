from petstore import PetStore, Pet

ps = PetStore()

patty = Pet('dog','Dalmation','Patty',20)
cole = Pet('dog','Pug','Cole',14)

ps.addPet( patty )
ps.addPet( cole )


dogs = ps.getPets('dog')

print('Dogs:')
for i, d in enumerate(dogs):
	print("{:>4}: {:>10} - ${:3.2f}".format(i,d.name,d.cost))
