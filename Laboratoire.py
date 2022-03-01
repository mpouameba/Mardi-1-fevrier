"""print("Bienvenue à la rechercher du Pole Nord ")

degre = input("Veuillez entrez le degré de votre position :")
minute = input("Veuillez entrez le nombre minute :")
seconde = input("Veuillez entrez le nombre de seconde :")

print("Votre position en DD est : ",str(degre2),"°",str(minute2),"°",str(seconde2))"""


def degredecimaux(degre,minute,seconde):
    return(degre+(minute/60)+seconde/3600)

degre =100
minute =150
seconde = 369

a = print(degredecimaux(degre,minute,seconde))


def polenord(x,y):
    return(x+(y/60))

x = 86
y = 172

b =print(polenord(x,y))

def difference(a,b):
    return(a-b)
y = a-b

print(difference(y))


