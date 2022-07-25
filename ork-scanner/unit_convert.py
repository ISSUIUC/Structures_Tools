"""
Unit Conversion Functions

OpenRocket stores all values in S.I units under the hood. In ITR and ISS
in general, we often speak in imperial units (massive L tbh), so these
conversions should come in handy.
"""

import math

def metersToFeet(meter_val):
    return round(meter_val * 3.28, 3)

def metersToCm(meter_val):
    return round(meter_val * 100, 3)

def kgsToLbs(kg_val):
    return round(kg_val * 2.20462, 3)

def radToDeg(rad_val):
    pass

def mpsToMach(mps_val):
    return round(mps_val/343, 3)


# Add more as required
