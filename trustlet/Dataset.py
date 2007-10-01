
__doc__ = """Abstraction class for Network dataset."""

import os
import urllib
from networkx import component
from networkx.xdigraph import XDiGraph

from numpy import *


def _dataset_dir():
    '''Create datasets/ directory if needed'''
    if os.environ.has_key('HOME'):
        home = os.environ['HOME']
    dataset_path = os.path.join(home, 'datasets')
    if not os.path.exists(dataset_path):
        os.mkdir(dataset_path)
    return dataset_path
        

class Network(XDiGraph):
    """
    Network dataset, extending networkx.xdigraph.XDiGraph
    see https://networkx.lanl.gov/reference/networkx/networkx.xgraph.XDiGraph-class.html
    """
    
    def __init__(self, make_base_path = True):
        '''Create directory for class name if needed'''

        XDiGraph.__init__(self)
        if make_base_path:
            self.path = os.path.join(_dataset_dir(), self.__class__.__name__)
            if not os.path.exists(self.path):
                os.mkdir(self.path)

    def download_file(self, url, file):
        '''Download url to filename into the right path '''
        filepath = os.path.join(self.path, file)
        print "Downloading %s to %s " % (url, filepath)
        p = urllib.urlretrieve(url, filepath)

    def _read_dot(self, filepath):
        import networkx
        graph = networkx.read_dot(filepath)
        for node in graph.nodes():
            self.add_node(node)
        for edge in graph.edges():
            self.add_edge(edge)


    def ditch_components(self, threshold = 3):
        """Ditch components with less than [threshold] nodes"""
        UG = self.to_undirected()
        if len(UG):
            concom_subgraphs = component.connected_component_subgraphs(UG)[1:]
            n_remove = 0
            for sg in concom_subgraphs:
                if len(sg) <= threshold:
                    for n in sg:
                        n_remove += 1
                        self.delete_node(n)
            print "Thrown out", n_remove, "nodes, fraction: ", 1.0 * n_remove / len(UG)
        else:
            print "Empty graph, no components to ditch"

    def _sorted_edges(self):
        e = self.edges()
        e.sort()
        return e

    def _edge_array(self, fieldname = 'trust'):
        e = self._sorted_edges()
        a = array(map(lambda x: float(x[2][fieldname]), e))
        return a

class PredGraph(Network):
    def __init__(self, dataset, tm):
        jpath = os.path.join
        Network.__init__(self, make_base_path = False)
        
        filepath = reduce(jpath, [_dataset_dir(), dataset, tm, 'pred_graph.dot'])
        self._read_dot(filepath)
        

if __name__ == "__main__":
    scale = (0.4, 1)
    pg = PredGraph("Kaitiaki", "PageRankTM")
    pr = pg._edge_array('predtrust')
    pr_normalized = (pr - min(pr)) / (max(pr) - min(pr))
    pr_scaled = scale[0] + pr_normalized * (scale[1] - scale[0])



