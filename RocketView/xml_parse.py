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
