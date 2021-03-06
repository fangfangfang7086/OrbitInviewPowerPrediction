#!/usr/bin/env python

from satellite_tle import SatelliteTle
from datetime import datetime
from pytz import timezone

###############################################################################
# Script to use the satellite_tle module to compute
# a table of ephemeris points for (local) today for ISS
###############################################################################

def main():
    """Main function... makes 'forward declarations' of helper functions unnecessary"""
    # Constants
    satnum = 25544 # ISS = 25544
    saturl="http://www.celestrak.com/NORAD/elements/stations.txt"
    our_tzname = 'US/Eastern'

    # Times we need
    now = datetime.now()
    our_tz = timezone(our_tzname)
    our_today_start = our_tz.localize(datetime(now.year, now.month, now.day, \
                                               0, 0, 0))
    our_today_end = our_tz.localize(datetime(now.year, now.month, now.day, \
                                             23, 59, 59))

    st = SatelliteTle(satnum, tle_url=saturl)
    table = st.compute_ephemeris_table(our_today_start, our_today_end, 60)
    print_ephemeris_table(st, table)

def print_ephemeris_table(st, table):
    print "Satellite Number: %s" % st.get_satellite_number()
    print "Current ISS TLE:"
    print st
    print "Time: X/Y/Z in km, VX/VY/VZ in km/s, ECI Coordinates"
    print ""
    for i in range(0, len(table)):
        print "%s: %16.8f/%16.8f/%16.8f %13.9f/%13.9f/%13.9f" % \
              (table[i][0], table[i][1][0], table[i][1][1], table[i][1][2], \
               table[i][2][0], table[i][2][1], table[i][2][2]) 

# Python idiom to eliminate the need for forward declarations
if __name__=="__main__":
   main()
