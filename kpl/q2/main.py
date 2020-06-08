from astropy import units as u

# Please provide the function with float type variable without astropy units , The returned value is the distance of the galaxy in light years
# vrec = H*d where vrec is recessional velocity (Km/s), H is the hubble's constant((Km/s)/Mpc) and d is the distance
# d = vrec/H (Mpc)
# 1 parsec ~ 3.262 light years
# d = vrec/H * 3.262 Million light years

def findDistance(vrec):
    
    distance = (vrec/71.0)*10**6 * u.parsec
    x = distance.to('lyr')
    return x.value


    


