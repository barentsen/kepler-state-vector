# kepler-state-vector 
***Prints the state vector of the Kepler spacecraft using SpiceyPy (SPICE).***

A little tool intended to demonstrate the use of SPICE, through the [SpiceyPy Python wrapper](http://spiceypy.readthedocs.org), to print the state vector of the Kepler spacecraft.

### Example use
```
$ python kepler-state-vector.py "2016-01-12T22:35:07.584"
```

Output:
```
Input time = 2016-01-12T22:35:07.584

# Position of Kepler in the geocentric J2000 frame
X = 0.80754723 AU
Y = -0.03077504 AU
Z = -0.02164734 AU

# Velocity of Kepler in the geocentric J2000 frame
dX = 0.00000000 AU/s
dY = 0.00000015 AU/s
dZ = 0.00000007 AU/s

# Orbital speed [sqrt(dX^2 + dY^2 + dZ^2)]
Speed = 0.00000016 AU/s
```

### Installation

[SpiceyPy](http://spiceypy.readthedocs.org) must be installed.
For example:
```
$ conda install -c https://conda.anaconda.org/andrewannex spiceypy
```

Then simply download or clone this repository and run the Python script, e.g.
```
$ git clone git@github.com:barentsen/kepler-state-vector.git
$ cd kepler-state-vector
$ python kepler-state-vector.py 2015-11-13T09:43:00
```
