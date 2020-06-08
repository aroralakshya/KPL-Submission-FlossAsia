# all imports below
from astropy import units as u

# vrec = H*d - v is recessional velocity(Km/s), H is the hubble's constant(Km/s/Mpc) and d is the distance
# d = vrec/H (Mpc)


def findDistance(vrec):
	
    HubbleConst = 71*10**-6 * (u.km/u.s)/u.parsec
    distance = vrec/HubbleConst
    
    return distance.to('lyr')


