"""
Rocket Component Objects

A few objects that should make the parsing cleaner than reading out of a
dictionary every time. Also makes dealing with multiple ork files at a time
way nicer.
"""

import xmltodict

class Rocket:
    def __init__(self, name):
        self.name = name
    def populateData(self, xml_filename):
        in_file = open(xml_filename, 'r')
        xml_string = in_file.read()
        in_file.close()
        xml_dict = xmltodict.parse(xml_string)

        # Populating nosecone data
        nosecone_dict = xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"]["subcomponents"]["nosecone"]
        self.nosecone.length = float(nosecone_dict["length"])
        self.nosecone.geometry = nosecone_dict["shape"]
        self.nosecone.material = nosecone_dict["material"]["#text"]
    def setNosecone():
        pass
    def

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
    def __init__(self, length, material, thickness):
        self.length = length
        self.material = material
        self.thickness = thickness

class RecoverySystem:
    def __init__(self, shockcord_length, chute_material):
        self.shockcord_length = shockcord_length
        self.chute_material = chute_material
