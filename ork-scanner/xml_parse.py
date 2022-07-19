import xmltodict
import pprint


inf = open("rocket.ork", 'r')
print("\nOpened ork file...")

xml_string = inf.read()
inf.close()
print("Parsed xml file to a string...")

xml_dict = xmltodict.parse(xml_string)
print("Parsed string into a dictionary...")

# pp = pprint.PrettyPrinter(indent=0)
# pp.pprint(output["openrocket"]["rocket"]["subcomponents"]["stage"])
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

print("/tSimulation Summary: ")
