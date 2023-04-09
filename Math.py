
print("           ╭━━┳━━┳━┳━━┳━━╮                         ┃━┳┻┃┃┫╋┃━━╋╮╭╯                         ┃╭╯╭┃┃┫╮╋━━┃┃┃                          ╰╯ ╰━━┻┻┻━━╯╰╯")
print("Zadej příklad trojčlenky")
print("Je to přímá nebo nepřímá úměrnost?")
umera=input("Přímá: P. Nepřímá: N\n")
print("Neznámá se píše jako 0")
a=input("Číslo 1: ")
b=input("Číslo 2: ")
c=input("Číslo 3: ")
d=input("Číslo 4: ")

a = float(a)
b = float(b)
c = float(c)
d = float(d)
if (umera == "P"):
  if (a == 0):
   result = c * b / d;
   print(result)
  elif (b == 0):
   result = d / c * a
   print(result)
  elif (c == 0):
   result = a * d / b
   print(result)
  else:
    result = b / a * c
    print(result)
   
  mapa=input("Jedná se o měřítko mapy?")

  if (mapa == "ano"):
   result = result / 100000;
   result = str(result)
   print(result + "km")
  elif (mapa == "ne"):
   print("ok")
  else:
   print("chyba při rozeznávání")
   
elif (umera == "N"):
  if (a == 0):
    result = c / b * d
    print(result)
  elif (b == 0):
    result = c / a * d
    print(result)
  elif (c == 0):
    result = a * b / d

    print(result)
  elif (d == 0):
    result = a * b / c
    print(result)
elif (umera == "Petr je gay"):
  print("             ╭╮╱╱╭┳━━━┳━━━┳╮                         ┃╰╮╭╯┃╭━━┫╭━╮┃┃                         ╰╮╰╯╭┫╰━━┫╰━━┫┃                         ╱╰╮╭╯┃╭━━┻━━╮┣╯                         ╱╱┃┃╱┃╰━━┫╰━╯┣╮                         ╱╱╰╯╱╰━━━┻━━━┻╯")
