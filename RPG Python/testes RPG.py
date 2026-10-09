from RPG import *

P2 = Mago("Hakidr", 20)
P3 = Guerreiro("Carlos", 200)

P2.Ficha(painel=True)

P3.Import("PersonasT.txt", "Hak")

#P3.Ficha(painel=True)

print(P2.__dict__)
print(P3.__dict__)

P3.Ficha(painel=True)
