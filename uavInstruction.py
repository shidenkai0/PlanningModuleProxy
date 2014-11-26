__author__ = 'Mohamed Messaad'

import geopy
import time
import csv

class UavInstruction(object):

    def __init__(self, uav_id=0, start=geopy.Point(36.370373, 127.36136910000005), dest=geopy.Point(36.370373, 127.36136910000005), timestamp=time.localtime(time.time())):
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


def read_csv(name):

    with open(name, 'r') as csvfile:
        actionreader=csv.DictReader(csvfile, delimiter=',')

        for row in actionreader:
            print row

        csvfile.close()
    return 1


def main():
    uavinst1 = UavInstruction(3, geopy.Point(36.370373, 127.36136910000005), geopy.Point(1,0), time.localtime(time.time()))
    print read_csv('input.csv')

main()




