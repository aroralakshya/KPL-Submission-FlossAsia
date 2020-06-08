# all imports below
from astropy import units as u

"""
Any extra lines of code (if required)
as helper for this function.
"""
# vrec = H*d - v is recessional velocity(Km/s), H is the hubble's constant(Km/s/Mpc) and d is the distance
# d = vrec/H (Mpc)
# 1ps = 3.262 light years
# d = vrec/H * 3.262 Million light years
def findDistance(vrec):
	return (vrec/71.0)*3.262