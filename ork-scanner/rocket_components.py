"""
Rocket Component Objects

A few objects that should make the parsing cleaner than reading out of a
dictionary every time.
"""

class Nosecone(object):
    def __init__(self, length, geometry, material):
        self.length = length
        self.geometry = geometry
        self.material = material

class Finset(object):
    def __init__(self, fin_count, height, root_chord, tip_chord, material):
        self.fin_count = fin_count
        self.height = height
        self.root_chord = root_chord
        self.tip_chord = tip_chord
        self.material = material

class Simulation(object):
    def __init__(self, apogee, max_velocity, max_acceleration, flight_time):
        self.apogee = apogee
        self.max_velocity = max_velocity
        self.max_acceleration = max_acceleration
        self.flight_time = flight_time

class BodyTube(object):
    pass

class RecoverySystem(object):
    pass
