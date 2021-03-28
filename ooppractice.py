# 1. Tulislah code yang di dalamnya terdapat konsep-konsep OOP di bawah ini (kumpulkan dalam bentuk file python):
# Class - done
# Inheritance - done
# Class Attributes - done
# Instance Attributes - done
# Instance Methods - done
# Class Methods - done
# *Staticc method - done
# Overriding - done
# Overloading - done


## Pembuatan class Hero ##
class Hero:
    ## class attributes ##
    identitas = 'Hero'
    tempat_tinggal = "land of dawn"


    ## instance attributes: nama dan tipe_serangan ##
    def __init__(self, nama, tipe_serangan):
        self.nama = nama
        self.tipe_serangan = tipe_serangan
    

    ## instance attributes: hit ##
    ## instance method ##
    def basic_attack(self, hit):
        print(self.nama, "melakukan basic attack", hit)

    ## class method: battle_spell ##
    @classmethod
    def battle_spell(cls, nama_battle_spell):
        print(cls.identitas,"menggunakan battle spell",nama_battle_spell)

    ## static method: skill ##
    @staticmethod
    def spawn(): 
        print(Hero.identitas,"telah respawn")



### Child class ###
## Inheritance ##
# kapabilitas childclass / subclass untuk mewarisi attribute dan method dari parent class
class Hero_mage(Hero):
    identitas = 'Hero Mage'


## Overriding ##
# kapabilitas suatu childclass / subclass yang memiliki behaviour berbeda dengan parent class, namun dengan method yang sama
class Hero_fighter(Hero):
    identitas = 'Hero Fighter'
    def basic_attack(self,hit):
        print(f"{self.nama} memberikan damage dengan {hit}")

## Overloading ##
# kapabilitas suatu childclass / subclass yang memiliki method yang sama namun parameter yang berbeda
class Hero_tank(Hero):
    identitas = 'Hero Tank'
    def basic_attack(self, hit=None):
        if (hit == None):
            print(f"{self.nama} gagal melakukan basic attack")
        else:
            print(f"{self.nama} memberikan damage dengan {hit}")

class Hero_assassin(Hero):
    identitas = 'Hero Assassin'


zilong = Hero("Zilong", "physical")
cecilion = Hero("Cecilion", "magical")


## print class attribute ##
print(Hero.tempat_tinggal)
print(zilong.tempat_tinggal)
print(cecilion.tempat_tinggal)

zilong.basic_attack("serangan tombak")

zilong.spawn()

## Inheritance ##
kagura = Hero_mage("Kagura","magical")
print(kagura.tempat_tinggal) # class attribute inheritance
kagura.basic_attack("serangan payung") # instance method inheritance
kagura.spawn() # static method inheritance
kagura.battle_spell("flameshoot") #class method inheritance

## Overriding ##
lapu_lapu = Hero_fighter("lapu-lapu","physical")
lapu_lapu.basic_attack("serangan pedang") # with overriding method
kagura.basic_attack("serangan payung") # without overriding method

## Overloading ##
tigreal =  Hero_tank("Tigreal","physical")
tigreal.basic_attack() # hit = None
tigreal.basic_attack("serangan pedang dan perisai") # hit != None