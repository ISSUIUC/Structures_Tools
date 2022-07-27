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
        self.sims = []
        sim_list = []
        try:
            sim_list = xml_dict["openrocket"]["simulations"]["simulation"]
        except:
            print('no sims')

        for sim in sim_list:
            try:
                self.sims.append(Simulation(sim["flightdata"]["@maxaltitude"],
                                            sim["flightdata"]["@maxvelocity"],
                                            sim["flightdata"]["@maxacceleration"],
                                            sim["flightdata"]["@flighttime"]))
            except:
                print("unparsable sim")
                pass

        tube_collection = xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"]["subcomponents"]["bodytube"]
        self.tubes = []
        if isinstance(tube_collection, list):
            for tube in tube_collection:
                self.tubes.append(BodyTube(tube['name'],float(tube['length']), tube['material']['#text'], float(tube['thickness'])))
                try:
                    fin_dict = tube['subcomponents']['trapezoidfinset']
                    self.finset = Finset('trapezoid', fin_dict["fincount"], fin_dict["material"]["#text"], float(fin_dict["height"]), float(fin_dict["rootchord"]), float(fin_dict["tipchord"]))
                except:
                    print("this tube has no trapezoid fins")

                try:
                    fin_dict = tube['subcomponents']['freeformfinset']
                    self.finset = Finset("freeform", fin_dict['fincount'],fin_dict['material']['#text'])
                except:
                    print('this tube has no freeform fins')
        else:
            self.tubes.append(BodyTube(tube_collection['name'],float(tube_collection['length']), tube_collection['material']['#text'], float(tube_collection['thickness'])))
            try:
                fin_dict = tube_collection['subcomponents']['trapezoidfinset']
                self.finset = Finset('trapezoid', fin_dict["fincount"], fin_dict["material"]["#text"], float(fin_dict["height"]), float(fin_dict["rootchord"]), float(fin_dict["tipchord"]))
            except:
                print("this tube has no trapezoid fins")

            try:
                fin_dict = tube_collection['subcomponents']['freeformfinset']
                self.finset = Finset("freeform", fin_dict['fincount'],fin_dict['material']['#text'])
            except:
                print('this tube has no freeform fins')




class Nosecone:
    def __init__(self, length, geometry, material):
        self.length = length
        self.geometry = geometry
        self.material = material
    def __str__(self):
        return f"Nosecone - Length:{self.length},Geometry:{self.geometry},Material:{self.material}"

class Finset:
    def __init__(self, type, fin_count, material, height=None, root_chord=None, tip_chord=None):
        self.type = type
        self.fin_count = fin_count
        self.height = height
        self.root_chord = root_chord
        self.tip_chord = tip_chord
        self.material = material
    def __str__(self):
        return f"Finset - Fin Count:{self.fin_count},Type:{self.type},Material:{self.material}"

class Simulation:
    def __init__(self, apogee, max_velocity, max_acceleration, flight_time):
        self.apogee = apogee
        self.max_velocity = max_velocity
        self.max_acceleration = max_acceleration
        self.flight_time = flight_time
    def __str__(self):
        return f"Simulation - Apogee:{self.apogee},Max Velocity:{self.max_velocity},Max Acceleration:{self.max_acceleration}"

class BodyTube:
    def __init__(self, name, length, material, thickness):
        self.name = name
        self.length = length
        self.material = material
        self.thickness = thickness
    def __str__(self):
        return f"{self.name} - Length:{self.length},Material:{self.material},Thickness:{self.thickness}"

class RecoverySystem:
    def __init__(self, shockcord_length, chute_material):
        self.shockcord_length = shockcord_length
        self.chute_material = chute_material
    def __str__(self):
        return f"RecoverySystem - Shockcord Length:{self.shockcord_length},Chute Material:{self.chute_material}"
