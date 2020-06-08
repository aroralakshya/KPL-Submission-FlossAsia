 # all imports below
from datetime import datetime
from datetime import timedelta
from astropy.coordinates import EarthLocation, SkyCoord, solar_system_ephemeris, get_body, get_body_barycentric
import astropy.units as u
from astropy.coordinates import AltAz
from astropy.time import Time

#setting the reference location
observing_location = EarthLocation(lat="31.781216",lon="76.994217", height=1000*u.m)


#finding the AltAz positoin of saturn at time t
def position_of_saturn(t,Earth_wise_location):
    reference = AltAz(location=Earth_wise_location)
    with solar_system_ephemeris.set('builtin'):
        saturn = get_body('saturn', Time(t), Earth_wise_location)
    return saturn.transform_to(reference)
        
#finding the startobs
#---t is initial time---
def start_time(t, minimum_alt, earth_wise_location):
    coord = position_of_saturn(t, earth_wise_location)
    while(coord.alt.deg<minimum_alt):
        t = t+timedelta(seconds=1)
        coord=position_of_saturn(t, earth_wise_location)
        print(coord.alt.deg)
    return t

def end_time(t, minimum_alt, earth_wise_location):
    coord = position_of_saturn(t, earth_wise_location)
    while(coord.alt.deg>minimum_alt):
        t = t+timedelta(seconds=1)
        coord=position_of_saturn(t, earth_wise_location)
        print(coord.alt.deg)
    return t-timedelta(seconds=1)
    
#to find use startobs = start_time(datetime(2020, 6, 8, 18, 35, 0), 20, observing_location)
startobs = datetime(2020, 6, 8, 18, 39, 21)#time when saturn will become first visible

# to find run endobs = end_time(datetime(2020,6,9,1,0,0),20,observing_location)
endobs = datetime(2020, 6, 9, 1, 11, 25) #time when Saturn is no longer visible from SAC terrace

def findSaturn(obstime):
    '''
    Parameters
    ----------
    obstime : A `~datetime.datetime` instance.
    
    Returns
    -------
    A `tuple` of two floats.
    '''
    
    coord = position_of_saturn(obstime,observing_location)
    return tuple((coord.alt.deg, coord.az.deg))
