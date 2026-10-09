from rich import print
from abc import ABC, abstractmethod
from random import randint
from rich.panel import Panel

class Personagem(ABC):

   def __init__(self, nome, vida):

      self.nome = nome
      self.vida = vida
      self.golpes = []

   def Ficha(self, painel=False):

      cont = f"[blue]Nome: {self.nome}[/]   [green]Vida: {self.vida}[/]"

      if painel:
         p = Panel(cont, title=f"{self.__class__.__name__}", width=30, border_style="blue")
         print(p)
         return None
      else:
         return cont

   # indo embora ----------------------------------------------------------------
   def Save(self, arquivo):

      try:
         Pers = open(arquivo, "rt")
         Pers.close()
      except:
         Pers = open(arquivo, "wt+")
         print("O arquivo de personagens foi criado")
         Pers.close()

      try:
         Pers = open(arquivo, "at")

         Pers.write(f"Nome: \n{self.nome}\n")
         Pers.write(f"Vida:  \n{self.vida}\n")
         Pers.write(f"Classe: \n{self.__class__.__name__}\n")

         print(f"Personagem {self.nome} salvo com sucesso")
      except:
         print("Nao consegui escrever nada :{")

   def Import(self, arquivo, nomepersona):

      try:
         Pers = open(arquivo, "rt")
         Pers.close()
      except:
         Pers = open(arquivo, "wt+")
         print("O arquivo foi criado")

      try:
         Pers = open(arquivo, "rt")
         Plinha = Pers.readlines()

         for a in range(0, len(Plinha)):  # procurando o nome em cada linha

            if Plinha[a].find(nomepersona) == 0: # achou na linha  A

               nom = Plinha[a].strip()
               vid = int(Plinha[a + 2].strip())
               cla = Plinha[a + 4].strip()

               match cla:

                  case "Guerreiro":

                     self.__class__ = Guerreiro
                     #p = Guerreiro(nom, vid)
                  case "Mago":
                     self.__class__ = Mago
                     #p = Mago(nom, vid)

               #print(f"Personagem {p.nome} de vida {p.vida} importado com sucesso")
               #return p

               self.nome = Plinha[a].strip()
               self.vida = int(Plinha[a + 2].strip())
               print(f"Personagem {self.nome} de vida {self.vida} importado com sucesso")
               break

            if a == len(Plinha) - 1: # nao achou em nenhuma mesmo
               print("Personagem nao encontrado")
               return 0

      except:
         print("Deu nao")
   # voltando ------------------------------------------------------------------

   def Atacar(self, alvo, forca):

      if self.vida > 0:

         dano = randint(0, forca)

         ataque = self.golpes[randint(0, len(self.golpes)-1)]

         print(f"O [blue]{self.__class__.__name__} {self.nome}[/] ataca [magenta]{alvo.nome}[/] com um [yellow]{ataque}[/] para tentar causar [red]{forca} de dano[/]")

         alvo.Receber_Dano(dano)
      else:

         print(f"[red]{self.nome} esta caido!!! Ele nao pode atacar[/]")

   def Receber_Dano(self, dano):

      self.vida -= dano
      print(f"O [magenta]{self.nome}[/] tomou [red]{dano} de dano[/]")
      if self.vida <= 0:
         print(f"[red on black]O {self.__class__.__name__} {self.nome} Chegou a 0 pontos de vida!!! [/]\n"
               f"[red on black]O {self.nome} caiu![/]")

   @abstractmethod
   def Curar(self):
      print("Caiu no lugar errado")

class Guerreiro(Personagem):

   def __init__(self, nome, vida):

      super().__init__(nome, vida)

      self.golpes = ["Soco", "Chute", "Espada"]

   def Curar(self):

      cura = randint(10, 50)

      self.vida += cura
      cont = (f"O [blue]{self.__class__.__name__} {self.nome}[/] toma uma pocao de cura\n"
               f"e restaura [green]{cura}[/] de pontos de vida\n"
               f"[green]Vida atual: {self.vida}[/]")

      p = Panel(cont, title=":heart: Curando :heart:", width=50, border_style="green")

      print(p)

class Mago(Personagem):

   def __init__(self, nome, vida):

      super().__init__(nome, vida)

      self.golpes = ["Bola de Fogo", "Bola de Raio", "Fazer sangrar", "Misseis Magicos"]

   def Curar(self):

      cura = randint(6, 18)

      self.vida += cura * 5

      cont = (f"O [purple]{self.__class__.__name__} {self.nome}[/] usa a magia toque curativo\n"
                f"e restaura [green]{cura}[/] de pontos de vida\n"
                f"[green]Vida atual = {self.vida}[/]")

      p = Panel(cont, title=":heart: Curando :heart:", width=50, border_style="green")

      print(p)
