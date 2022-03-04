
import math                     # Il faut toujours commenter ton code ligne par ligne pour facilité sa comprenhension à ton partenaire
def dm(a,b,c):
    return(a+(b/60)+c/3600)     # Utiliser des variables simple à comprendre, éviter les a ou a1, utiliser des variables qui ont un lien avec notre programme  

parislong = 25                  
parislatitude = 82
parisseconde = 63

POLE_NORD_longitude = 86
POLE_NORD_latitude = 172
POLE_NORD_seconde =0            # On nous a déjà donnée le DD du pôle nord par défault, alors il n'est plus nécessaire de le déclarer en DMS  
                                # remplacer POLE_NORD_LONGITUDE par DEGRE_POLE_NORD et POLE_NORD_LATITUDE par DECIMAL_POLE_NORD
                                # Supprimer l'affectation et la déclaration POLE_NORD_seconde, on a pas besoin
print(dm(parislong,parislatitude,parisseconde))
print(dm(POLE_NORD_longitude,POLE_NORD_latitude,POLE_NORD_seconde))


def distance(a1,a2,b1,b2):

    return(math.sqrt((a2-a1)**2 + (b2-b1)**2))

print(distance(POLE_NORD_longitude,parislong,POLE_NORD_latitude,parislatitude))





