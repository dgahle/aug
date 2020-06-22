import matplotlib.pyplot as plt
import math
import numpy as np
from cherab.mastu.machine import *

radians = 3.14159265 / 180.0


class fibres:
    """
    Geometry data for fibre bundles
    """

    def __init__(self):
        self.loaded = -1
        self.set_bundle(group=1)
        
    def set_bundle(self, group=None, fibre=12):
        if group == 1:
            self.group = 1
            self.load_ROV(fibre)
            self.numfibres = 14
            self.loaded = 1

    def set_fibre(self, number=1):
        self.set_bundle(group = self.group, fibre=number) 
                   
    def load_ROV(self,fibre):
        if fibre == 1:
            self.origin = self.machine_coordinates(1.438,-1.194,112.541)
            self.term = self.machine_coordinates(1.581,-1.202,112.592)
        if fibre == 2:
            self.origin = self.machine_coordinates(1.438,-1.194,112.541)
            self.term = self.machine_coordinates(1.584,-1.191,112.556)
        if fibre == 3:
            self.origin = self.machine_coordinates(1.438,-1.194,112.541)
            self.term = self.machine_coordinates(1.587,-1.178,112.544)
        if fibre == 4:
            self.origin = self.machine_coordinates(1.438,-1.194,112.541)
            self.term = self.machine_coordinates(1.591,-1.165,112.532)
        if fibre == 5:
            self.origin = self.machine_coordinates(1.438,-1.194,112.541)
            self.term = self.machine_coordinates(1.595,-1.150,112.517)
        if fibre == 6:
            self.origin = self.machine_coordinates(1.438,-1.194,112.541)
            self.term = self.machine_coordinates(1.598,-1.136,112.508)
        if fibre == 7:
            self.origin = self.machine_coordinates(1.438,-1.194,112.541)
            self.term = self.machine_coordinates(1.603,-1.118,112.507)
        if fibre == 8:
            self.origin = self.machine_coordinates(1.409,-1.147,112.665)
            self.term = self.machine_coordinates(1.602,-1.123,112.543)
        if fibre == 9:
            self.origin = self.machine_coordinates(1.409,-1.147,112.665)
            self.term = self.machine_coordinates(1.607,-1.105,112.551)
        if fibre == 10:
            self.origin = self.machine_coordinates(1.409,-1.147,112.665)
            self.term = self.machine_coordinates(1.612,-1.086,112.546)
        if fibre == 11:
            self.origin = self.machine_coordinates(1.409,-1.147,112.665)
            self.term = self.machine_coordinates(1.617,-1.065,112.529)
        if fibre == 12:
            self.origin = self.machine_coordinates(1.409,-1.147,112.665)
            self.term = self.machine_coordinates(1.624,-1.041,112.538)
        if fibre == 13:
            self.origin = self.machine_coordinates(1.409,-1.147,112.665)
            self.term = self.machine_coordinates(1.631,-1.013,112.537)
        if fibre == 14:
            self.origin = self.machine_coordinates(1.409,-1.147,112.665)
            self.term = self.machine_coordinates(1.641,-0.980,112.554)
        self.distance = self.fibre_distance_world(-1)
        
    def machine_coordinates(self,R,Z,phi):
        return ( R * math.cos(phi * radians), R * math.sin(phi * radians), Z )

    def xhat(self):
        return (self.term[0]-self.origin[0]) / self.distance

    def yhat(self):
        return (self.term[1]-self.origin[1]) / self.distance

    def zhat(self):
        return (self.term[2]-self.origin[2]) / self.distance

    def fibre_distance_world(self,world):
        return np.sqrt( (self.origin[0]-self.term[0])**2 + (self.origin[1]-self.term[1])**2 + (self.origin[2]-self.term[2])**2)

    
