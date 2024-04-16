class partyAnimal():
    x = 0

    def __init__(self) :
        print("I am constructor Start")

    def party(self):
        self.x = self.x+1
        print("So far", self.x)

    # def __del__(self) :
    #     print("I am destroyed",self.x)

an = partyAnimal()
an.party()
an.party()
an.party()

class partyHuman():
    x = 0
    name = ""
    
    def __init__(self,z) :
        self.name = z
        print(self.name,"Sudah datang")

    def dugem(self):
        self.x = self.x + 1
        print(self.name,"party dugem ada",self.x," orang")

class bolafans(partyHuman):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.dugem()
        print(self.name,"points", self.points)

s = partyHuman("Vivien")
s.dugem()

j = partyHuman("Andrew")
j.dugem()
s.dugem()

z = bolafans("Andro")
z.dugem()
z.touchdown()