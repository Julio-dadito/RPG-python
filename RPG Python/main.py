from rich import print
from rich.panel import Panel
from time import sleep
from RPG import *
from rich.traceback import install
from random import shuffle


install()

arquiv = "Personas.txt"
versao = "v0.761"

personagens = []
a = "S"
while a in "S":

   cont = "[blue]R[yellow]Python[blue]G[/] :snake:\n"
   cont += f"{f' :knife: :star: [red] {versao}[/]':>20}"
   Ti1 = Panel(cont, border_style="blue", width=20)
   print(Ti1)
   sleep(0.3)

   print()
   con = ("\n"
          "1- Da pra atacar\n"
          "2- Da pra curar\n"
          "3- Duas classes (Mago, Guerreiro)\n"
          "4- 1 modo de jogo (All vs)\n"  
          "5- Da pra salvar e importar personas")
   Ti2 = Panel(con, title=f"Status {versao}", width=40)
   print(Ti2)

   a = str(input("Play > S/N ")).upper()
   sleep(0.2)
   print()

   if a not in "S":
      break

   perg1 = 2
   while True:

      print("O que deseja fazer?\n"
            "( [green]1[/] ) Ver personagens criados\n"
            "( [yellow]2[/] ) Criar novo personagem\n"
            "| [blue]3[/] | Salvar Personagem\n"
            "| [blue3]4[/] | Importar Personagem\n"
            "[ [red]5[/] ] BATALHA\n"
            "[deep_pink4]< 6 > Sair[/]")
      perg1 = int(input(">"))
      print()

      cont = 0
      match perg1:
         case 1: # vendo personagens criados -------------------------------

            print("[bright_blue]-[/]"*40)

            if len(personagens) == 0:
               print("Nao ha nehum personagem ainda :{   cria um ai")
            else:
               for p, c in enumerate(personagens):
                  print(f"{f'Persona [green]Nº {p + 1}[/]':^35}")
                  c.Ficha(painel=True)
                  sleep(0.2)
            sleep(0.2)

            print("[bright_blue]-[/]"*40)

         case 2: # criando novo personagem ------------------------------

            cont += 1

            print(f"Qual sera o [cyan]nome[/] do personagem [green]Nº {cont}[/]?", end="")
            nom = str(input("       "))

            print(f"Quantos pontos de [green]vida[/] [cyan]{nom}[/] vai ter? ", end="")
            vida = int(input("  "))
            print()
            sleep(0.2)

            while True:
               print(f"Qual vai ser a [yellow]classe[/] do personagem [cyan]{nom}[/]? \n"
                                f"( [blue]1[/] ) [blue]Guerreiro[/]\n"
                                f"( [magenta]2[/] ) [magenta]Mago[/]\n")
               clas = int(input(">"))

               if clas == 1:
                     P1 = Guerreiro(nom, vida)
                     break
               elif clas == 2:
                     P1 = Mago(nom, vida)
                     break
               else:
                  print("Classe nao encontrada")
                  sleep(0.3)

            personagens.append(P1)
            print(f"{f'[blue]--[yellow]Personagem {P1.nome} criado com sucesso[blue]--[/]':^50}")
            print()
            sleep(0.5)

         case 3:  # salvando um personagem -----------------------------------------

            print("Qual personagem deseja salvar?")

            print("( -1 ) Todos")
            for p, o in enumerate(personagens):

               print(f"( {p} ) {o.nome}")

            sal = int(input(">"))

            if sal == -1:

               for o in personagens:
                  o.Save("Personas.txt")

            elif -1 < sal <= len(personagens):
               personagens[sal].Save("Personas.txt")
               sleep(0.2)
            else:
               print("[red]Personagem nao encontrado[/]")

            sleep(0.3)

         case 4: # trazendo de volta --------------------------------------------------

            print("Arquivo utilizado = 'Personas.txt'")
            sleep(0.2)
            print()

            print("Deseja importar um personagem especifico ou TODOS do arquivo?\n"
                  "( 0 ) TODOS\n"
                  "( 1 ) especifico")

            est = int(input(">"))

            match est:

               case 0:

                  Ar = open("Personas.txt", "rt")
                  Arl = Ar.readlines()

                  numpesi = len(Arl)//6  # quantos personagens tem

                  if numpesi > 0:
                     r = 1
                     for p in range(0, numpesi): # pra cada personagem q tiver

                        pi = Guerreiro("", 0)

                        pi.Import("Personas.txt", Arl[p+r].strip())
                        sleep(0.2)
                        r += 5
                        personagens.append(pi)
                  else:
                     print("Nao encontrei nenhum personagem no arquivo descrito :{")
                     sleep(0.3)

               case 1:

                  pi = Guerreiro("", 0)
                  a = pi.Import("Personas.txt", str(input("Qual o nome do personagem?")))
                  sleep(0.3)

                  if pi.nome not in "":
                     personagens.append(pi)
                  else:
                     print("Arquivo vazio.......")
                  sleep(0.3)

         case 5: # BATALHA ---------------------------

            print("[red]-<[/] Entao partiremos a batalha! [red]>-[/]")
            sleep(0.5)

            while True:

               print("Como sera a batalha? \n"
                        "[yellow]( [red]1 [yellow]) [dark_orange]Todos contra todos \n"
                        "[blue]( [red]2 [magenta])[dark_orange] Times \n"
                        "[bright_black]( [red]3 [bright_black])[dark_orange] Contra PC[/]")
               bat = int(input(">"))

               if bat == 1 or bat == 2 or bat == 3:
                  break
               else:
                  print("Escolha invalida")

            if bat == 1: # todos contra todos -----------------------
               print(f"{'--Todos contra todos--':^50}")
               sleep(0.4)

               shuffle(personagens)

               print(f"Ordem de acoes:\n")

               for p, i in enumerate(personagens):

                  print(f"{p} - {i.Ficha()}")
                  sleep(0.3)

               # variaveis da batalha:
               ndmorts = 0
               emgame = True
               turnos = 0
               while True:

                  ndmorts = 0

# comeca turno ----------------------------------------------------------------
                  for i in personagens: # turnos

                     print(f"Turno de {i.nome}")

                     i.Ficha(painel=True)

                     if i.vida <= 0: # morto no inicio do turno
                        print(f"[red]{i.nome} esta morto [/]:skull:")
                        sleep(0.3)
                        ndmorts += 1

                     else:

                        print(f"Qual Acao [blue]{i.nome}[/] fara? \n"
                                   f"( [cyan]1[/] ) [cyan]Atacar :knife:[/]\n"
                                   f"( [green]2[/] ) [green]Curar :heart:[/]\n")
                        aca = int(input(">"))

                        match aca:
                           case 1:

                              alv = -1
                              while alv == -1:

                                 print(f"Quem [blue]{i.nome}[/] ira atacar?")
               # lista de alvos usa o O -------------------------------
                                 for p, o in enumerate(personagens):

                                    if o.nome != i.nome:
                                       print(f"( {p} )  {o.nome}")
                                       sleep(0.3)

               # no final pergunta quem vai atacar ----------------------

                                    if p == len(personagens) - 1:

                                       alv = int(input(">"))

               # caso seja maior q a lista ------------------------------------
                                    if alv > len(personagens)-1:
                                       print("[red]Esse alvo nao existe[/]")
                                       alv = -1

               # se nao varre a lista e coloca o alvo no O -------------------
                              for p, o in enumerate(personagens):
                                 if alv == p:
                                       alv = o

                              dan = int(input("Quanto de dano voce vai tentar dar?"))

                              i.Atacar(alv, dan)

                              if alv.vida == 0: # morreu pelo ataque
                                 ndmorts += 1

                              sleep(0.5)

                           case 2:

                              i.Curar()
                              sleep(0.5)

                     if ndmorts == len(personagens)-1: # a cada fim de turno chega se sobra um personagem vivo

                        for o in personagens:
                           if o.vida > 0: # quem ainda tem vida
                              print(f"O vencedor e [magenta]{o.nome}[/]")
                              sleep(0.5)
                              print("\nBatalha encerrada\n")
                              sleep(0.5)
                              emgame = False

                     if not emgame:
                        break
# termina turno ------------------------------------------------------

                  if not emgame:
                     break

                  turnos += 1
                  print(f"--- 1 Turno passa --- ")
                  sleep(0.6)
                  print(f"Turno atual : {turnos+1}\n")
                  sleep(0.6)

            elif bat == 2 and len(personagens) >= 3:

               print("Quantos times tera?")

               if len(personagens) >= 3:
                  print("( 2 ) Dois Times\n")
                  dT = True
               if len(personagens) >= 4:
                  print("( 3 ) Tres Times\n")
                  tT = True

               numti = int(input(">"))

               print("Havera fogo amigo? S/N  >", end="")
               friendfire = str(input(""))

               print("batalha modo time ainda em construcao....\n")
               sleep(0.5)

            elif bat == 2:
               print("[red]Numero invalido de personagens para modo time[/]")
               sleep(0.5)

            elif bat == 3:
               print("batalha contra PC ainda em construcao...\n")
               sleep(0.5)

         case 6:
            a = "N"
            break


print("Ate mais ver, guerreiro")