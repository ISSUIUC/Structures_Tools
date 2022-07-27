"""
Main sequence

This is the file that should actually be run. Edit filepaths to specify
which orks you want scanned
"""

from rocket_components import *

rkt = Rocket('bruh', 'test_rockets/Gautam_L1_June.ork')
print("nosecone len " + str(rkt.nosecone.length))
print("fin material " + str(rkt.finset.material))
print("fin root chord: " + str(rkt.finset.root_chord))
print("fin tip chord: "+ str(rkt.finset.tip_chord))
for sim in rkt.sims:
    print(sim)
