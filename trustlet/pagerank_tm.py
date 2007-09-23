
from networkx import *
from Advogato import *
import page_rank
import numpy

from pprint import pprint

# http://localhost/src/networkx/reference/public/networkx.generators.classic-module.html


def exactPR(G):
    M = page_rank.google_matrix(G, alpha=0.9)
    e, ev = numpy.linalg.eig(M.T)
    p = numpy.array(ev[:,0] / ev[:,0].sum())[:,0]
    return p

def NXPR(G):
    pr = page_rank.page_rank(G,alpha=0.9,tol=1.0e-8)
    return pr.values()

def numpyPR(G):
    np = page_rank.page_rank_numpy(G,alpha=0.9)
    return np

def scipyPR(G):
    try:
        ns = page_rank.page_rank_scipy(G,alpha=0.9)
        return ns
    except "bad scipy":
        print "scipy not working"



def randomgraph():
    G = XDiGraph()
    edges = [(1,2), (1,3),
             (3,1), (3,2), (3,5),
             (4,5), (4,6),
             (5,4), (5,6),
             (6,4)]
    G.add_edges_from(edges)
    return G

def test():
    G = Advogato("tiny")
    for e in G.edges():
        G.delete_edge(e)
        G.add_edge(e[0], e[1], G.trust_on_edge(e))
    # pprint (G.edges())

    print "networkx", NXPR(G)
    print "numpy   ", numpyPR(G)
    print "scipy   ", scipyPR(G)
    print "exact   ", exactPR(G)

if __name__ == '__main__':
    test()





def pagerank_tm(G, a, b):
    pr = page_rank.page_rank(G, alpha=0.9, tol=1.0e-8)
    print pr.values()
    
