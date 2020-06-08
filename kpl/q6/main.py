# all imports below

import math
import astropy.coordinates
from astropy.coordinates import cartesian_to_spherical

"""
Any extra lines of code (if required)
as helper for this function.
"""

def findstrike(velocity, alt, az):
	V = [velocity*math.cos(math.pi/180*alt)*math.cos(math.pi/180*az),velocity*math.sin(math.pi/180*alt),v*math.cos(math.pi/180*alt)*math.sin(math.pi/180*az)]
	#m/s #projectile velocity in three directions xyz

	time = 2*V[1]/9.8  #(t=2Vy/g)

	#all in meter
	sx = V[0]*time
	sy = -8848
	sz = V[2]*time


	xyz = [302768.03439095,5636038.60539686,2979468.58862902]  #coordinates of top of mt everest in meters calculated from its lat,long and elev

	new_coord = [sx-xyz[0],sy-xyz[1],sz-xyz[2]]

	qw = astropy.coordinates.cartesian_to_spherical(new_coord[0],new_coord[1],new_coord[2])

	answer = (qw[1],qw[2])
	return (answer)
