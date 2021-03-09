def somme (a,b):
  return a+b


def puissance(a, b):
  return a ** b


def fonct(a,b,c):
  print(a, b,c)
  return a,b,c

def somme1(a,b,c):
  return a+b+c


valeurs = 1,2
c = valeurs[0]
d = valeurs[1]

res = somme(*valeurs)
print()
print(res)