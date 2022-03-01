import math
def dm(a,b,c):
    return(a+(b/60)+c/3600)

Parislong = 25
parislatitude = 82
parisseconde = 63

pole_nord_longitude = 86
pole_nord_latitude = 172
pole_nord_seconde =0

print(dm(Parislong,parislatitude,parisseconde))
print(dm(pole_nord_longitude,pole_nord_latitude,pole_nord_seconde))


def distance(a1,a2,b1,b2):

    return(math.sqrt((a2-a1)**2 + (b2-b1)**2))

print(distance(pole_nord_longitude,Parislong,pole_nord_latitude,parislatitude))





