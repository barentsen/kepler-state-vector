# kepler-state-vector 
***Prints the state vector of the Kepler spacecraft using SpiceyPy (SPICE).***

A little tool intended to demonstrate the use of SPICE, through the [SpiceyPy Python wrapper](http://spiceypy.readthedocs.org), to print the state vector of the Kepler spacecraft.

### Example use
```
$ python kepler-state-vector.py "2016 01 12.94106"
```

Output:
```
Input time = 2016 01 12.94106

# Position of Kepler in the geocentric J2000 frame
X = 0.8071066542355017 AU
Y = -0.04303078307468914 AU
Z = -0.026958957670645378 AU

# Velocity of Kepler in the geocentric J2000 frame
dX = 6.801563010842106e-09 AU/s
dY = 1.5067559509333052e-07 AU/s
dZ = 6.52888679400489e-08 AU/s

# Orbital speed [sqrt(dX^2 + dY^2 + dZ^2)]
Speed = 1.6435337688350942e-07 AU/s
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
