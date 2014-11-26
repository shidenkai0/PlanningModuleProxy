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



# Reads a CSV File and Outputs a List containing Uav Instructions as objects
def read_csv(name):

    instructions_list = []

    with open(name, 'r') as csvfile:
        actionreader=csv.DictReader(csvfile, delimiter=',')

        for row in actionreader:
            start = cartesian_to_gps_ref(float(row['start_x']), float(row['start_y']))
            dest = cartesian_to_gps_ref(float(row['dest_x']), float(row['dest_y']))
            start_point = geopy.Point(start[0], start[1])
            dest_point = geopy.Point(dest[0], dest[1])
            timestamp = time.strptime(row['time'], '%H:%M')
            inst = UavInstruction(int(row['uav_id']), start_point, dest_point, timestamp)
            instructions_list.append(inst)

    return instructions_list


def main():
    for instruct in read_csv('input.csv'):
        print instruct.start

main()




