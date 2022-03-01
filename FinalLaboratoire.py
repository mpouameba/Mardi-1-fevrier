import math
def dm(a,b,c):
    return(a+(b/60)+c/3600)

parislong = 25
parislatitude = 82
parisseconde = 63

POLE_NORD_longitude = 86
POLE_NORD_latitude = 172
POLE_NORD_seconde =0

print(dm(parislong,parislatitude,parisseconde))
print(dm(POLE_NORD_longitude,POLE_NORD_latitude,POLE_NORD_seconde))


def distance(a1,a2,b1,b2):

    return(math.sqrt((a2-a1)**2 + (b2-b1)**2))

print(distance(POLE_NORD_longitude,parislong,POLE_NORD_latitude,parislatitude))





