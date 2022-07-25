"""
Rocket Component Objects

A few objects that should make the parsing cleaner than reading out of a
dictionary every time. Also makes dealing with multiple ork files at a time
way nicer.
"""

import xmltodict

class Rocket:
    def __init__(self, name, xml_filename):
        self.name = name
        self.xml_filename = xml_filename
        in_file = open(xml_filename, 'r')
        xml_string = in_file.read()
        in_file.close()
        xml_dict = xmltodict.parse(xml_string)

        # Populating data
        nosecone_dict = xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"]["subcomponents"]["nosecone"]
        self.nosecone = Nosecone(float(nosecone_dict["length"]),
                                       nosecone_dict["shape"],
                                       nosecone_dict["material"]["#text"])
        fin_dict = xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"]["subcomponents"]["bodytube"][1]['subcomponents']['trapezoidfinset']
        self.finset = Finset(fin_dict["fincount"], float(fin_dict["height"]), float(fin_dict["rootchord"]), float(fin_dict["tipchord"]), fin_dict["material"]["#text"])

        sim_list = xml_dict["openrocket"]["simulations"]["simulation"]
        self.sims = []
        for sim in sim_list:
            try:
                self.sims.append(Simulation(sim["flightdata"]["@maxaltitude"],
                                            sim["flightdata"]["@maxvelocity"],
                                            sim["flightdata"]["@maxacceleration"],
                                            sim["flightdata"]["@flighttime"]))
            except:
                pass

class Nosecone:
    def __init__(self, length, geometry, material):
        self.length = length
        self.geometry = geometry
        self.material = material
    def __str__(self):
        return f"Length:{self.length},Geometry:{self.geometry},Material:{self.material}"

class Finset:
    def __init__(self, fin_count, height, root_chord, tip_chord, material):
        self.fin_count = fin_count
        self.height = height
        self.root_chord = root_chord
        self.tip_chord = tip_chord
        self.material = material
    def __str__(self):
        return f"Fin Count:{self.fin_count},Height:{self.height},Root Chord:{self.root_chord},"

class Simulation:
    def __init__(self, apogee, max_velocity, max_acceleration, flight_time):
        self.apogee = apogee
        self.max_velocity = max_velocity
        self.max_acceleration = max_acceleration
        self.flight_time = flight_time
    def __str__(self):
        return f"Apogee:{self.apogee},Max Velocity:{self.max_velocity},Max Acceleration:{self.max_acceleration}"

class BodyTube:
    def __init__(self, length, material, thickness):
        self.length = length
        self.material = material
        self.thickness = thickness
    def __str__(self):
        return f"Length:{self.length},Material:{self.material},Thickness:{self.thickness}"

class RecoverySystem:
    def __init__(self, shockcord_length, chute_material):
        self.shockcord_length = shockcord_length
        self.chute_material = chute_material
    def __str__(self):
        return f"Shockcord Length:{self.shockcord_length},Chute Material:{self.chute_material}"
