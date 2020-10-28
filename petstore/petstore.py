class Pet:
	def __init__(self,petType,breed,name,cost):
		self.petType=petType
		self.breed=breed
		self.name=name
		self.cost=cost
		
	def __repr__(self):
		return "Pet<{}-{}#{}:{:3.2f}>".format(self.petType,self.breed,self.name,self.cost)


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

