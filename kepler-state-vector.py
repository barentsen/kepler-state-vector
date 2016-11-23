"""Prints the geocentric J2000 state vector of the Kepler spacecraft using SpiceyPy (SPICE).
"""
import sys
import spiceypy as sp

KERNELS = ['data/naif0011.tls',
           'data/de432s.bsp',
           'data/spk_2016313000000_2016314193308_kplr.bsp']


if __name__ == "__main__":
    # Script expects first argument to be a UTC timestamp
    if len(sys.argv) > 1:
        input_utc = sys.argv[1]
    else:
        input_utc = '2016-01-12T22:35:07.584'  # default for testing
    # Load the necessary data files
    sp.furnsh(KERNELS)
    # Convert input time to ephemeris time
    epoch = sp.str2et(input_utc)
    # State (position and velocity in cartesian coordinates)
    # of Kepler (-227) as seen from EARTH in the J2000 coordinate frame.
    state, lt, = sp.spkezr("-227", epoch, "J2000", "NONE", "EARTH")
    # Show the output
    print("Input time = {}".format(input_utc))
    print("")
    print("# Position of Kepler in the geocentric J2000 frame")
    print("X = {:.8f} AU".format(sp.convrt(state[0], 'km', 'AU')))
    print("Y = {:.8f} AU".format(sp.convrt(state[1], 'km', 'AU')))
    print("Z = {:.8f} AU".format(sp.convrt(state[2], 'km', 'AU')))
    print("")
    print("# Velocity of Kepler in the geocentric J2000 frame")
    print("dX = {:.8f} AU/s".format(sp.convrt(state[3], 'km', 'AU')))
    print("dY = {:.8f} AU/s".format(sp.convrt(state[4], 'km', 'AU')))
    print("dZ = {:.8f} AU/s".format(sp.convrt(state[5], 'km', 'AU')))
    # As a sanity check, print the speed
    speed = (state[3]**2 + state[4]**2 + state[5]**2)**.5
    print("")
    print("# Orbital speed [sqrt(dX^2 + dY^2 + dZ^2)]")
    print("Speed = {:.8f} AU/s".format(sp.convrt(speed, 'km', 'AU')))
