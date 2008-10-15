"""
Network classes

In this file, was stored all the class that
wrap the network in DOT format.
Each network supported has it's own class to wrap it.
"""


from trustlet.Table import Table
from trustlet.powerlaw import power_exp_cum_deg_hist
import trustlet

import networkx

import os
from networkx.xdigraph import XDiGraph
from networkx import cluster, path, component

import numpy

average = lambda x: x and float(sum(x)) / len(x)


def dataset_dir(path=None):
    """Create datasets/ directory if needed."""
    
    if not path:
        path = ''
        if os.environ.has_key('HOME'):
            path = os.environ['HOME']
    dataset_path = os.path.join(path, 'datasets')
    
    trustlet.helpers.mkpath(dataset_path)
    
    return dataset_path
        

class Network(XDiGraph):
    """
    Network dataset, extending networkx.xdigraph.XDiGraph
    see https://networkx.lanl.gov/reference/networkx/networkx.xgraph.XDiGraph-class.html
    """
    
    def __init__(self, from_graph = None, make_base_path = True, base_path = None, savememory = False):
        '''
        Create directory for class name if needed
        base_path: the path to put dataset directory
        savememory:
           decrease of ~9% time to load graph, and it saves some memory
           (50MB (on 300MB) in Italian Wiki graph)
           *but* we can't modify edges after graph creation.
        '''

        XDiGraph.__init__(self, multiedges = False)
        if make_base_path:
            self.path = os.path.join(dataset_dir(base_path), self.__class__.__name__)
            if not os.path.exists(self.path):
                os.mkdir(self.path)
                
        self.savememory = savememory

        if from_graph:
            self.paste_graph(from_graph)

    
        
    def download_file(self, url, filename):
        '''Download url to filename into the right path '''
        filepath = os.path.join(self.path, filename)
        print "Downloading %s to %s " % (url, filepath)

        import urllib2
        try:
            asock = urllib2.urlopen(url)
            f = open(filepath, 'w')
            f.write(asock.read())
            f.close()
            asock.close()
        except urllib2.HTTPError, e:
            try:
                asock = urllib2.urlopen(url+'.bz2')
                f = open(filepath+'.bz2', 'w')
                f.write(asock.read())
                f.close()
                asock.close()
            except urllib2.HTTPError, e:
                print e.code
                print "Cannot download dataset, for a complete list of it, go to ", os.path.split( os.path.split( url )[0] )[0]


    def connected_components(self):
        G = self
        if self.is_directed():
            G = G.to_undirected()
        return component.connected_components(G)

    def number_of_connected_components(self):
        return len(self.connected_components())

    def connected_components_size(self):
        return map(len, self.connected_components())

    def connected_components_size2(self,n=2):
        '''n = number of cc to keep'''
        return map(len, self.connected_components()[:n])

    def strongly_connected_components(self):
        G = self
        if self.is_directed():
            G = G.to_undirected()
        return component.connected_components(G)

    def strongly_connected_components_size(self):
        return map(len, self.connected_components())

    def avg_degree(self):
        return average(self.degree())

    def std_in_degree(self):
        return numpy.std(self.in_degree())

    def std_out_degree(self):
        return numpy.std(self.out_degree())

    def degree_histogram(self):
        from networkx import degree_histogram
        return degree_histogram(self)

    def _show_method(self, method, desc = ""):
        if not desc:
            desc = method
        print desc, getattr(self, method)()
        
    def info(self):
        """Show information."""
        XDiGraph.info(self)
        
        for method, desc in [("std_in_degree", "Std deviation of in-degree:"),
                             ("std_out_degree", "Std deviation of out-degree:"),
                             ("average_clustering", "Average clustering coefficient:"),
                             ("link_reciprocity", "Ratio of edges reciprocated:"),
                             ("powerlaw_exponent", "Power exponent of cumulative degree distribution:"),
                             ("number_of_connected_components","Number of connected components:"),
                             ("connected_components_size2","Connected component size:"),
                             ]:
            self._show_method(method, desc)
        
    def powerlaw_exponent(self):
        return power_exp_cum_deg_hist(self)

    def is_connected(self):
        if self.is_directed():
            G = self.to_undirected()
            return component.is_connected(G)
        else:
            return component.is_connected(self)

    def is_strongly_connected(self):
        if self.is_directed():
            return component.is_strongly_connected(self)

    def link_reciprocity(self):
        """Calculate the reciprocity of the edges (without paying attention 
        to the value on the edges."""
        return 1.0 * sum([self.has_successor(e[1], e[0]) 
                          for e in self.edges_iter()]) / self.number_of_edges()

    def in_degree_hist(self):
        """in-degree histogram, minor adaptation from 
        networkx.function.degree_histogram"""
        degseq = self.in_degree()
        dmax = max(degseq)+1
        freq = [0 for d in xrange(dmax)]
        for d in degseq:
            freq[d] += 1
        return freq

    def out_degree_hist(self):
        """out-degree histogram, minor adaptation from 
        networkx.function.degree_histogram"""
        degseq = self.out_degree()
        dmax = max(degseq)+1
        freq = [0 for d in xrange(dmax)]
        for d in degseq:
            freq[d] += 1
        return freq

    
    def download_dataset(self, url, filepath ):
        """
        download a dataset from a url to a filepath, if it not exist
        NB: automatically add filename to url
        """
        
        filename = os.path.split( filepath )[1] 

        if not os.path.exists(filepath) and not os.path.exists(filepath+'.bz2'):
            self.download_file( os.path.join(url,filename) , filename )


    def _read_dot(self, filepath,force=False):
        """Read file."""
        print "Reading", filepath
        #import networkx
        #graph = networkx.read_dot(filepath)
        graph = trustlet.helpers.cached_read_dot(filepath,force)
        self.paste_graph(graph)
        
    def paste_graph(self, graph, avoidset=None):
        """
        Paste graph into object.
        Parameter:
           graph: the graph
           avoidset: the set object that contains all the nodes leaved out from the copying
        """
    
        if self.savememory:
            add_edge = lambda e: self.add_edge((e[0],e[1],trustlet.helpers.pool(e[2])))
        else:
            add_edge = lambda e: self.add_edge(e)

        if avoidset:
            for node in [x for x in graph.nodes_iter() if x not in avoidset]:
                self.add_node(node)

            for edge in [x for x in graph.edges_iter() if x[0] not in avoidset and x[1] not in avoidset]:
                add_edge(edge)
        else:
            for node in graph.nodes_iter():
                self.add_node(node)

            for edge in graph.edges_iter():
                add_edge(edge)
    
    def _paste_graph(self, graph, avoidset=None):
        """Deprecated."""
        self.paste_graph(graph, avoidset)

    def ditch_components(self, threshold = 3):
        """Ditch components with less than [threshold] nodes"""

        undir_graph = self.to_undirected()
        if len(undir_graph):
            concom_subgraphs = component.connected_component_subgraphs(undir_graph)[1:]
            n_remove = 0
            for subgraph in concom_subgraphs:
                if len(subgraph) <= threshold:
                    for node in subgraph:
                        n_remove += 1
                        self.delete_node(node)
            print "Thrown out", n_remove,
            print "nodes, fraction: ", 1.0 * n_remove / len(undir_graph)
        else:
            print "Empty graph, no components to ditch"

    def _sorted_edges(self):
        """sorted edges"""
        edges = self.edges()
        edges.sort()
        return edges

    def _edge_array(self, mapper = None):
        """numpy array of sorted edges, mapper is an optional function
        that will be applied to the edges"""
        return numpy.array(map(mapper, self._sorted_edges()))

    def average_clustering(self):
        """Average clustering coefficient."""
        return average(cluster.clustering(self))

    def transitivity(self):
        """Clustering transitivity coefficient."""
        return cluster.transitivity(self)

    def avg_shortest_distance(self):
        """Average shortest distance between nodes."""
        # TODO: pay attention to the fact there are 2 or more connected component
        pair_distances = path.all_pairs_shortest_path_length(self)
        return average([average(x.values()) for x in pair_distances.values()])

    def min_in_edges(self, num):
        """Nodes with minimum of num incoming edges."""
        return [n for n in self if len(self.in_edges(n)) > num]
    

class WeightedNetwork(Network):
    """A weighted network.

    Things to arrange:
    * weights can be discrete or continuous
    """
    
    def __init__(self, weights = None, has_discrete_weights = True, base_path = None,savememory = False):
        Network.__init__(self, base_path=base_path,savememory=savememory)
        self.has_discrete_weights = has_discrete_weights
        self.is_weighted = True
        self._weights = weights

    def trust_on_edge(self, edge):
        """
        SHOULD BE: weight_on_edge
        """
        return edge[2]

    def weights(self):
        """
        Return a list with the weights of all edges
        """
        if hasattr(self, "_weights") and self._weights:
            ws = self._weights
        else:
            ws = []
            for n in self.edges_iter():
                x = n[2]
                ws.append( x )
            
            self._weights = ws
        
        return ws
    
    def weights_dictionary(self):
        """
        Return a dictionary with the weights of all edges
        Work only in advogato-like function
        """
        if trustlet.helpers.get_name( self ) == 'WikiNetwork':
            return None

        if hasattr(self, "_weights_dictionary") and self._weights_dictionary:
            ws = self._weights_dictionary
        else:
            ws = {}
            for n in self.edges_iter():
                x = n[2]
                if type(x) is float or type(x) is int:
                    ws[str(x)] = x
                else:
                    if hasattr( x, 'keys' ) and hasattr( self, 'level_map' ):
                        ws[x.values()[0]] = self.level_map[ x.values()[0] ]
                    elif type(x) is tuple:
                        ws[x[0]] = x[1]
            
            self._weights_dictionary = ws
        
        return ws
    

    def info(self):

        Network.info(self)

    def min_weight(self):
        """Minimum weight."""
        return min(self.weights())

    def max_weight(self):
        """Maximum weight."""
        return max(self.weights())

    def node_controversiality(self, node):
        """Controversiality of node: the standard deviation of incoming weights."""
        return numpy.std(map(self.trust_on_edge,
                             self.in_edges_iter(node)))


    def controversiality(self):
        """Controversiality of nodes."""
        return dict([(n, self.node_controversiality(n))
                     for n in self])
        
    def avg_controversiality(self, min_num_edges = 3):
        """Average controversiality of nodes with at least min_num_edges incoming edges."""
        
        return average([self.node_controversiality(n)
                        for n in self.min_in_edges(min_num_edges)])

    def controversial_nodes(self, min_std = 0.1, min_num_edges = 3):
        """Nodes with at least min_num_edges incoming edges and controversiality > min_std."""
        node_controversy_list = [(n, c)
                                 for (n, c) in self.controversiality().items()
                                 if c >= min_std and len(self.in_edges(n)) >= min_num_edges]
        node_controversy_list.sort(lambda x, y: cmp(x[1], y[1]))
        node_controversy_list.reverse()
        return node_controversy_list
        
    def show_reciprocity_matrix(self):
        if self.has_discrete_weights:
            recp_mtx = self.reciprocity_matrix()
            tbl = Table([12] + [12] * len(self.weights_dictionary()))
            tbl.printHdr(['reciprocity'] + self.weights_dictionary().keys())
            tbl.printSep()
            for k, v in recp_mtx.items():
                tbl.printRow([k] + v)

    def reciprocity_matrix(self):
        """Generate a reciprocity table (which is actually a dict)."""
        def value_on_edge(e):
            if type(e) in (int, float):
                return e
            else:
                return e.values()[0]
        
        if self.has_discrete_weights:
            table = {}
            for v in self.weights_dictionary().keys():
                line = []
                for w in self.weights_dictionary().keys():
                    line.append(sum([value_on_edge(self.get_edge(e[1], e[0])) == w
                                     for e in self.edges_iter()
                                     if (self.has_edge(e[1], e[0]) and 
                                         value_on_edge(e[2]) == v)]))
                table[v] = line
            return table
        else:
            raise Exception( "Not implemented" )



class MovieLensNetwork(WeightedNetwork):
    """
    MovieLens dataset network
    """
    def __init__(self, base_path = None):
        WeightedNetwork.__init__(self, base_path = base_path)
        
        try:
            #print os.path.join(self.path,"graph.dot")
            self._read_dot( os.path.join(self.path,"graph.dot") )
        except IOError:
            raise IOError("There aren't a dot file on this path:\n "+
                          self.path+"\nplease specify another path or create dot file with movielens.py" )
        

class WikiNetwork(WeightedNetwork):
    """
    Wikipedia Network Handler.
    You must pass to it a string with lang of wikipedia, and a string with the date of dataset. 
    Optionally:
    dataset: path to a dot file that it will load and save in the dataset folder
    upthreshold: number of vote to consider edges max trusted
    current: Default True (download graphCurrent), if False use the dataset generated by History xml (named graphHistory).
    bots: default False, indicate if you would or not the bots in the network.
    threshold: the minimum weights on edges (1..n)

    NB: if you would know what kind of network are hosted on www.trustlet.org invoke getNetworkList() from trustlet.helpers
    """
        
    def __init__(self, lang, date, current=False, bots=True, blockedusers=True, base_path = None,
                 dataset = None, force = False,
                 savememory = False, threshold=1, output=False ):
        WeightedNetwork.__init__(self,base_path=base_path,savememory=savememory)
        
        assert trustlet.helpers.isdate(date),'date: aaaa-mm-dd'

        self.url = 'http://www.trustlet.org/trustlet_dataset_svn/'
        self.lang = lang; self.date = date; self.current = current; self.bots = bots; self.botset = None; self._weights_dictionary = None
        self.threshold = threshold; self.__upbound = None; self.blockedusers=blockedusers

        if savememory:
            add_edge = lambda e: self.add_edge((e[0],e[1],trustlet.helpers.pool(e[2])))
        else:
            add_edge = lambda e: self.add_edge(e)

        if current:
            filename = "graphCurrent"
        else:
            filename = "graphHistory"

        #if not bots:
        #    filename += '-nobots'

        self.path = os.path.join( self.path, lang, date )
        trustlet.helpers.mkpath(self.path)
        
        self.filepath = os.path.join( self.path, filename )

        path,relpath = trustlet.helpers.relative_path( self.filepath, 'datasets' )
        #                                  the first value is the name of the file
        self.url = os.path.join( self.url, os.path.split(relpath)[0])

        #load from cache
        if output:
            print "Reading ", self.filepath+'.c2'
        
        cachedict = {'network':'Wiki','lang':str(lang),'date':str(date)}
        if threshold > 1:
            cachedict['threshold'] = threshold

        #if not bots:
        #    cachedict['users'] = 'nobots'

        
        pydataset = trustlet.helpers.load(cachedict, self.filepath+'.c2')
        
        if pydataset == None:
            # retry without thresold
            cachedict = {'network':'Wiki','lang':str(lang),'date':str(date)}
            pydataset = trustlet.helpers.load(cachedict, self.filepath+'.c2')
            
            #generate dataset with the requested threshold
            if pydataset and threshold > 1:
                edges = pydataset[1]
                edges = filter( lambda x: x[2] >= threshold, edges )
                pydataset = (pydataset[0],edges)
                
            
        if pydataset:
            #now I'm sure that this network is in a c2 file
            self.filepath += '.c2' ; self.filename = filename + '.c2'
        
            nodes,edges = pydataset
            toU = lambda x: unicode(x) #to unicode
            
            #implement here the nobots control
            cachedict = {'lang':lang}
            if not bots:
                cachedict['list'] = 'bots'
                botset = trustlet.helpers.load(cachedict, self.filepath )
                if type(botset) is list:
                    botset = set(botset)
                else:
                    botset = set()
                self.botset = botset #save botset for future use
            else:
                self.botset = set()

            if not blockedusers:
                cachedict['list'] = 'blockedusers'
                blockedset = trustlet.helpers.load(cachedict, self.filepath )
                if type(blockedset) is list:
                    blockedset = set(blockedset)
                else:
                    blockedset = set()
                self.blockedset = blockedset #save blockset for future use
            else:
                self.blockedset = set()
                
            if not self.botset:
                botset = set()

                    #if bots false x not in botset is always true!
            for u in [x for x in nodes if (toU(x) not in botset) and (toU(x) not in blockedset)]:
                self.add_node(u)
            for u,v,e in [x for x in edges if toU(x[0]) not in botset and toU(x[1]) not in botset and toU(x[0]) not in blockedset and toU(x[1]) not in blockedset]:
                self.add_node(u)
                self.add_node(v)
                add_edge( ( u,v,{'value':e} ) )
       
        else:
            if os.path.exists( self.filepath+'.c2' ):
                print "Warning! the c2 file does not contain the dataset.."
                print "the key used was: ", cachedict

            self.filepath += '.dot'; self.filename = filename + '.dot'

            try:

                if dataset == None:
                    self._read_dot( self.filepath, force )
                else:
                    if os.path.isfile( dataset ):
                        self._read_dot( dataset, force )
                        data = dataset
                    else:
                        data = os.path.join( dataset, filename+'.dot' )
                        self._read_dot( data, force )
                                    
                    #save graph.dot in right folder
                    os.rename( data, os.path.join(self.path,filename+'.dot') )
                
                #end else

            except IOError:
                                        
                raise IOError("There isn't a dot file on this path:\n "+
                              self.path+"\nplease specify another path with dataset parameter "+
                              "or create dot file with [wikixml2dot.py|wikixml2graph.py]" )

        self.__rescale()


    def weights(self):
        """
        Return a list with the weights of all edges
        """
        if hasattr(self, "_weights_dictionary") and self._weights_dictionary:
            ws_dict = self._weights_dictionary
        else:
            ws_dict = {}
                    
        lendict = len(ws_dict)

        if hasattr(self, "_weights") and self._weights:
            ws = self._weights
        else:
            ws = []
            for n in self.edges_iter():
                        
                try:
                    x = self.map( float(n[2]['value']) )
                    
                    if lendict == 0:
                        ws_dict[int(n[2]['value'])] = x
                    
                    ws.append( x )
                except:
                    raise "Cannot read dataset. The edges was malformed.\nThis is a malformed edge:", n
                                
            self._weights_dictionary = ws_dict
            self._weights = ws
        
        return ws

    def weights_dictionary(self):
        """
        return a dictionary with all the weights in the network
        and it's rescaled value
        """
        return self._weights_dictionary

    def map(self, value):
        """
        take a value to rescale in range 0..1
        """
        from math import log

        if type(value) is str:
            value = int(value)

        #logarithm in base 3 of the value

        if value > self.__upbound:
            return 1.
        else:
            return log( value , 3 ) / log( self.__upbound , 3 )

    def __rescale(self):
        """
        take the _weights field and rescale the value
        """

        upbound = trustlet.helpers.load({'network':'Wiki','lang':str(self.lang),'date':str(self.date),'%':95})
        
        if upbound:
            self.__upbound = upbound
        else:
            s = sorted( map( lambda x: x[2]['value'] , self.edges() ) )
            wslen = self.number_of_edges()
            maximum = float(wslen) * 5 / 100
            self.__upbound = s[wslen - int(maximum)]
            
        return self.weights()



    def trust_on_edge(self,edge):
        """
        return trust on edge passed
        """
        if type(edge[2]) is int:
            return self.map( edge[2] )

        return self.map( edge[2].values()[0] )

    def ignored_users(self):
        '''
        Users with in_degree and out_degree both equal to 0 aren't returned.
        '''
        return [x for x in self.nodes_iter() if self.out_degree(x) and not self.in_degree(x)]

    def passive_users(self):
        '''
        Users with in_degree and out_degree both equal to 0 aren't returned.
        '''
        return [x for x in self.nodes_iter() if not self.out_degree(x) and self.in_degree(x)]

    
    def plot_weight_edges_histogram(self):
        '''
        Plot the network frequency weights histogram.
        '''
        
        data = {}

        for w in self.edges_iter():
            w = w[2]['value']
            if w in data:
                data[w] += 1
            else:
                data[w] = 1
            
        trustlet.helpers.prettyplot(data.items(),os.path.join(self.path,'weights histogram nolog'),
                                    xlabel='weights',
                                    ylabel='frequency',
                                    title='Frequency weights histogram',
                                    #log='xy',
                                    histogram=True)
        print 'Graph saved in',self.path

    def load_distrust(self):
        filepath = os.path.join(self.path,'graphDistrust.c2')

        pynet = trustlet.helpers.load({'network':'DistrustWiki','lang':self.lang,'date':self.date}, filepath)
        if not pynet:
            print "Distrust graph doesn't exist"
            return

        nodes,edges = pynet

        for n in nodes:
            self.add_node(n)

        for e in edges:
            self.add_node(e[0])
            self.add_node(e[1])
            
            try:
                weight = self.get_edge(e[0],e[1])
            except networkx.NetworkXError:
                weight = {}

            weight['distrust'] = e[2]

            self.add_edge(e[0],e[1],weight)

if __name__ == "__main__":
    from trustlet import *
    W = WikiNetwork('fur','2008-06-14',savememory=1)
    W.load_distrust()
