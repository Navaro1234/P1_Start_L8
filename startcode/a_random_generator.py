import random

keuze = str(input("Geef je keuze. "))

bnvgg = ["Super", "Mega", "Ultra", "Toffe", "Magische"]
znvgg = ["Coder", "Ninja", "Expert", "Gamer", "Pokémon"]

def genereer_gebruikersnaam() :
    bngeneratorvgg = random.choice(bnvgg)
    zngeneratorvgg = random.choice(znvgg)
    return bngeneratorvgg + zngeneratorvgg

def keuze1() :
    print("10 willekeurige gebruikersnamen:")
    for _ in range(10):
        print(genereer_gebruikersnaam())

if keuze == "1" :
    keuze1()

