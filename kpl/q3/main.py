# all imports below

import math
"""
Any extra lines of code (if required)
as helper for this function.
"""

M = 5.974e24

C = 2.998e8

G = 6.674 * 10 ** (-11)
R = 6357000

# time dilation = sqrt(1- 2*G*M/r*c*c ) * T - Where T is the time taken for light to reach the satellite 

def calcTime(dist):
	return (R-dist)/C

def findDelay(dist):
    T = calcTime(dist)
    dT1 = math.sqrt(1- (2*G*M)/(R*C*C)) * T
    dT2 = math.sqrt(1- (2*G*M)/(dist*C*C)) * T
    return abs(dT1 - dT2)*10**9			#the nanoseconds gained by the satellite
