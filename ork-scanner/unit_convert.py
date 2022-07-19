"""
Unit Conversion Functions

OpenRocket stores all values in S.I units under the hood. In ITR and ISS
in general, we often speak in imperial units, so these conversions should
come in handy.
"""

import math

def metersToFeet(meter_val):
    return round(meter_val * 3.28, 3)

def metersToCm(meter_val):
    return round(meter_val * 100, 3)

def kgsToLbs(kg_val):
    pass

def radToDeg(rad_val):
    pass

def mpsToMach(mps_val):
    pass


# Add more as required
