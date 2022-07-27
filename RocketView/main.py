"""
Main sequence

This is the file that should actually be run. Edit filepaths to specify
which orks you want scanned
"""

from rocket_components import *

rkt = Rocket('bruh', 'test_rockets/Navya_L1.ork')
print("nosecone len " + str(rkt.nosecone.length))
print("nosecone material " + rkt.nosecone.material)
print("nosecone geometry: " + rkt.nosecone.geometry)
print("fin material " + rkt.finset.material)
print("fin type: " + rkt.finset.type)
print("fin count: " + str(rkt.finset.fin_count))

for tube in rkt.tubes:
    print(tube)

for sim in rkt.sims:
    print(sim)
    print('\n')
