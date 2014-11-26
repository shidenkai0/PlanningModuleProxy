__author__ = 'Mohamed Messaad'

import geopy
import time
import csv

K=1
GPS_REFERENCE = 36.370373, 127.36136910000005

class UavInstruction(object):

    def __init__(self, uav_id=0, start=geopy.Point(GPS_REFERENCE[0], GPS_REFERENCE[1]), dest = geopy.Point(GPS_REFERENCE[0], GPS_REFERENCE[1]), timestamp=time.localtime(time.time())):
        if (uav_id>=0)&(type(uav_id) == type(0)):
            self._uav_id=uav_id
        else:
            raise RuntimeError('Invalid UAV Id')

        self.start=start
        self.dest=dest
        self.timestamp=timestamp

    @property
    def uav_id(self):
        return self._uav_id

    @uav_id.setter
    def uav_id(self, uav_id):
        if (uav_id>=0)&(type(uav_id) == type(0)):
            self._uav_id=uav_id
        else:
            raise RuntimeError('Invalid UAV Id')


# Convert WGS84 to cartesian coordinates
def gps_to_cartesian_ref(lat, long):
    y = (lat-GPS_REFERENCE[0])/K
    x = (long-GPS_REFERENCE[1])/K
    return x, y

# Convert cartesian to WGS84 coordinates
def cartesian_to_gps_ref(x, y):
    long_gps=GPS_REFERENCE[1]+K*x
    lat_gps=GPS_REFERENCE[0]+K*y
    return lat_gps, long_gps




def read_csv(name):

    with open(name, 'r') as csvfile:
        actionreader=csv.DictReader(csvfile, delimiter=',')

        for row in actionreader:
            print row
            t = cartesian_to_gps_ref(float(row['start_x']), float(row['start_y']))
            print t
            print gps_to_cartesian_ref(t[0], t[1])

        csvfile.close()
    return 1


def main():
    uavinst1 = UavInstruction(3, geopy.Point(36.370373, 127.36136910000005), geopy.Point(1,0), time.localtime(time.time()))
    print read_csv('input.csv')

main()




