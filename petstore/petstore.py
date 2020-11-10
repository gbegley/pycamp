class Pet:
	def __init__(self,petType,breed,name,cost,behaviour='naughty'):
		self.petType=petType
		self.breed=breed
		self.name=name
		self.cost=cost
		self.behaviour=behaviour
		
	def __repr__(self):
		return "Pet<{}-{}#{}:{:3.2f} - {}>".format(self.petType,self.breed,self.name,self.cost,self.behaviour)


class PetStore:
	pets = {"cats":list(),"dogs":list(),"birds":list(),"fishs":list()}

	def getPets( self, t ):
		k = "{}s".format(t)
		return self.pets[ k ]
		
	def showPets( self, petType ):
		petList = self.getPets(petType)
		print( petType,':')
		for i, d in enumerate(petList):
			print("{:>4}: {:>10} - ${:3.2f} - {}".format(i,d.name,d.cost,d.behaviour))

	
	def addPet( self, pet ):
		try:
  			l = self.getPets(pet.petType)
  			l.append(pet)
		except:
  			print("We don't carry pets of type {}".format(pet.petType))

	def getPet( self, petType, name ):
		l = self.getPets(petType)
		myPet = next((p for p in l if p.name==name))
		return myPet
