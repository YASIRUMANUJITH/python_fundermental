class Vault:
    def __init__(self,galleons=0,sickles=0,kunuts=0):
        self.galleons=galleons
        self.sickles=sickles
        self.kunuts=kunuts

    def __str__(self):
        return f"{self.galleons} Gallenons, {self.sickles} sickles, {self.kunuts} kunuts"
    
    
    def __add__(self,other):
        galleons=self.galleons + other.galleons
        sickles=self.sickles + other.sickles
        kunuts=self.kunuts + other.kunuts
        return Vault(galleons,sickles,kunuts)
    

potter = Vault(100 ,50 ,25)
print(potter)

weasley= Vault(25 ,50 ,100 )
print(weasley)


total=potter+weasley
print(total)



