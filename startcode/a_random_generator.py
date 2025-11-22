import random

bnvgg = ["Super", "Mega", "Ultra", "Toffe", "Magische"]
znvgg = ["Coder", "Ninja", "Expert", "Gamer", "Pokémon"]

def genereer_gebruikersnaam() :
    bngeneratorvgg = random.choice(bnvgg)
    zngeneratorvgg = random.choice(znvgg)
    return bngeneratorvgg + zngeneratorvgg




print("10 willekeurige gebruikersnamen:")
for _ in range(10) :
    print(genereer_gebruikersnaam())