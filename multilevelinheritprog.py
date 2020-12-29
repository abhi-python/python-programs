class Electronic_Dvice:
    Television = 10
    Fridge = 5
    def device(self):
        return f"Yes it is a electronic device"

class Pocket_gadgets(Electronic_Dvice):
    Earphone = 6
    def gadgets(self):
        return f"Yes, I have {self.Earphone}  earphone in my pocket" 

class Phone(Pocket_gadgets):
    iphone = 4
    def gadgets(self):
        return f"I have {self.iphone} i phone in my pocket"    

abhi = Electronic_Dvice()
aman = Pocket_gadgets()
akash = Phone()
print(akash.device()) 
print(akash.gadgets()) 
print(akash.Fridge)             