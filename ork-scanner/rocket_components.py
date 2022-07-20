"""
Rocket Component Objects

A few objects that should make the parsing cleaner than reading out of a
dictionary every time. Also makes dealing with multiple ork files at a time
way nicer.
"""

class Rocket:
    def __init__(self, nosecone, finset, simulations, tube, recovery):
        self.nosecone = nosecone
        self.finset = finset
        self.simulations = simulations
        self.tube = tube
        self.recovery = recovery

class Nosecone:
    def __init__(self, length, geometry, material):
        self.length = length
        self.geometry = geometry
        self.material = material

class Finset:
    def __init__(self, fin_count, height, root_chord, tip_chord, material):
        self.fin_count = fin_count
        self.height = height
        self.root_chord = root_chord
        self.tip_chord = tip_chord
        self.material = material

class Simulation:
    def __init__(self, apogee, max_velocity, max_acceleration, flight_time):
        self.apogee = apogee
        self.max_velocity = max_velocity
        self.max_acceleration = max_acceleration
        self.flight_time = flight_time

class BodyTube:
    pass

class RecoverySystem:
    pass
