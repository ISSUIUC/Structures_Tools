"""
Main sequence

This is the file that should actually be run. Edit filepaths to specify
which orks you want scanned
"""

from rocket_components import *

rkt = Rocket('bruh', 'test_rockets/endurance.ork')
print(rkt.nosecone.length)
print(rkt.finset.material)
