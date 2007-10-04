"""
Constantly evolving test stuff.

It will often reflect what guaka was working on in a specific
revision.  It might be removed in the future if trustlet ever reaches
a beta stage.

"""


from __init__ import *

from pylab import *
from networkx import *
from analysis import *

from pprint import pprint


def ev(G):
    return map(lambda tm: PredGraph(G, tm),
               [IntersectionTM,
                GuakaMoleTM,
                GuakaMoleFullTM,
                PaoloMoleTM])

G = Kaitiaki()
pga = ev(G)

for p in pga:
    pprint (p.evaluate())
