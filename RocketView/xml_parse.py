"""
XML Parsing Functionality

OpenRocket (.ork) files are internally stored as xml files. We use the xmltodict
library to read the xml file into a Python dict, which are far easier to work with.
"""

import xmltodict
import pprint
import unit_convert

inf = open("test_rockets/endurance.ork", 'r')
print("\nOpened ork file...")

xml_string = inf.read()
inf.close()
print("Parsed xml file to a string...")

xml_dict = xmltodict.parse(xml_string)
print("Parsed string into a dictionary...")

pp = pprint.PrettyPrinter(indent=0)
pp.pprint(xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"])
print("\n BODY TOOBS \n")
toobdict = xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"]["subcomponents"]["bodytube"]

for toob in toobdict:
    print(toob)
    print('\n')

print('\n')
print("--- ORK SCAN READY, MY LIEGE --- ")
print('\n')
nosecone_dict = xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"]["subcomponents"]["nosecone"]
print('\tNosecone data:')
nosecone_len = float(nosecone_dict["length"])
print("\t\tLength: " + str(nosecone_len * 100) + "cm")
print("\t\tGeometry: " + nosecone_dict["shape"])
print("\t\tMaterial: " + nosecone_dict["material"]["#text"])

fin_dict = xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"]["subcomponents"]["bodytube"][2]['subcomponents']['trapezoidfinset']
print('\tFinset data:')
print('\t\tFin count: ' + str(fin_dict["fincount"]))
print('\t\tHeight: ' + str(float(fin_dict["height"]) * 100) + 'cm')
print('\t\tRoot Chord: ' + str(float(fin_dict["rootchord"]) * 100) + 'cm')
print('\t\tTip Chord: ' + str(float(fin_dict["tipchord"]) * 100) + 'cm')
# print('\t\t')
print("\t\tMaterial: " + fin_dict["material"]["#text"])

print("\tSimulation Summary: ")
for sim in xml_dict["openrocket"]["simulations"]["simulation"]:
    try:
        print("\t\tApogee: " + sim["flightdata"]["@maxaltitude"])
        print("\t\tMax Velocity: " + sim["flightdata"]["@maxvelocity"])
        print("\t\tMax Acceleration: " + sim["flightdata"]["@maxacceleration"])
        print("\t\tFlight Time: " + sim["flightdata"]["@flighttime"])
        print("\n")
    except:
        pass
