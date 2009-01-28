#!/usr/bin/env python
"""
This package contains all the function 
on the evolution of a network
"""
from trustlet.helpers import *
from trustlet.conversion import dot
from trustlet.Dataset import Network,Advogato
from networkx import read_dot
from pprint import pprint
import os,time,re
import os.path as path
import scipy

re_alphabetic = re.compile("[A-Za-z]+")

# functions list
fl = []
al = lambda f,pf: fl.append((f,pf)) #function, print function

def evolutionmap(networkname,functions,cond_on_edge=None,range=None,cacheonly=False,debug=None,prefix='_'):
    '''
    apply functions to each network in range range.
    If you want use cache `function` cannot be lambda functions.

    Parameters:
    networkname = the name of the network (case sensitive)
                  ex. AdvogatoNetwork
    functions = list of functions to apply to each dataset
                the functions must take two argument:
                1) graph g (as trustlet.Network or subclasses)
                2) date in wich the dataset of the graph g, was calculated 
                #e.g. [trustvariance,trustaverage...]
    range = tuple with at first the initial date, and at end the
                final date #ex. ('2000-01-01','2008-01-01')
    
    return a list of list of values where each list of the first
                list represent a function 'i', and the values in
                this i-list are the i-function returned values for each network in
                range
    '''
    #we load network from datasets
    lpath = os.path.join(os.environ['HOME'],'datasets',networkname)
    #and cache/predgraph from shared_dataset (an svn on trustlet.org)
    cachepath = os.path.join( os.environ['HOME'],'shared_datasets',networkname,'netevolution.c2') 
    
    #make sure the path exists
    mkpath(lpath)
            #avoid c2 file..
    mkpath( os.path.split(cachepath)[0] )

    if debug:
        deb = file( debug, 'w' ) #in debug file was stored the last function to be evaluated and on which network
        deb.close()


    dates = sorted(
        [date for date in os.listdir(lpath)
         if isdate(date) and ( path.exists(path.join(lpath,date,'graph.dot')) or
                               path.exists(path.join(lpath,date,'graph.c2')) or
                               path.exists(path.join(lpath,date,'graphHistory.c2')) ) ]
        )
    
    if not dates:
        print "There isn't any network in this path"
        return

    if range:
        assert isdate(range[0]) and  isdate(range[1]) and (len(range)<3 or type(range[2]) is int),range
        #dates = [x for x in dates if x>=range[0] and x<=range[1]]
        new = []
        prec = '1970-01-01'
        for date in dates:
            #range check
            if date<range[0]:
                continue
            elif date>range[1]:
                break

            #step check
            if len(range)==3 and mktimefromdate(date) - mktimefromdate(prec) < 3600*24*range[2]:
                continue
            new.append(date)
            prec = date
        dates = new

    if len(dates)==1:
        print 'There is a network'
    else:
        print 'There are %d networks' % len(dates)

    def task(date):
        resdict = {} #dict of result
        calcfunctions = []
        recompute = set(['level_distribution'])

        #try to find the functions cached
        for i in xrange(len(functions)):
            assert functions[i].__name__!='<lambda>','Lambda functions aren\'t supported'

            cachekey = {'function':functions[i].__name__,'date':date}
            if cond_on_edge:
                assert cond_on_edge.__name__!='<lambda>','Lambda function is not suppoeted for condition on edges'
                cachekey['cond']=str(cond_on_edge.__name__)

            cache = load(cachekey,path.join(lpath,cachepath))
            #cache = None # debug
            if cache and type(cache) is tuple and isdate(cache[0]):
                #check on type of data in cache

                #sys.stderr.write('cache hit\n')
                if functions[i].__name__ in recompute:
                    calcfunctions.append(functions[i])
                else:
                    resdict[functions[i].__name__] = cache
                #do not calculate for functions cached
            elif not cacheonly:
                #eprint(cachekey)
                #eprint(str(cache)[:50]) #debug
                #sys.stderr.write('cache fault\n')
                calcfunctions.append(functions[i])

        if not calcfunctions:
            #if is empty
            return resdict

        # Type Of Network
        ton = networkname

        alphabetic = re_alphabetic.search( ton ) #search alphabetic character (delete non A-Za-z prefix)
        ton = ton[alphabetic.start():] #delete first non alphabetic character
        
        try:
            ton = re_alphabetic.findall( ton )[0] # _ added to support robots_net network
        except IndexError:
            if debug:
                deb = file( debug, 'a' )
                deb.write( "ERROR!: problem in path! is this path correct? "+lpath+"\n" )
                deb.close()
            else:
                print "ERROR!: problem in path! is this path correct? "+lpath
            return None
                
        print ton
        
        if debug:
            deb = file( debug, 'a' )
            deb.write( "evaluating functions "+str(calcfunctions)+"\non "+ton+" at date "+date+"\n" )
            deb.close()

        if ton != 'WikiNetwork':
            dotpath = path.join(lpath,date,'graph.dot')
            c2path = dotpath[:-3]+'c2'
    
            #test what type of network I had to use
            try:
                Networkclass = getattr( Advogato , ton )
            except AttributeError:
                try:
                    Networkclass = getattr( Network , ton )
                except AttributeError:
                    if debug:
                        deb = file( debug, 'a' )
                        deb.write( "ERROR!: this type of network("+ton+") is not defined in trustlet.Dataset module\n" )
                        deb.close()
                    return None

            #load network
            try:
                K = Networkclass(date=date,cond_on_edge=cond_on_edge)
            except IOError:
                print "Warning! in default path date does not exist! try to use a prefix"
                K = Networkclass(date=date,prefix=prefix)
                #try with _ if there isn't in normal path
                #(because sync does not upload folder with _ prefix)
            
            print 'K is a %s' % K.__class__.__name__
    
            if not K:
                if debug:
                    deb = file( debug, 'a' )
                    deb.write( "ERROR!: cannot be able to load c2 on "+ton+" at date "+date+"\n" )
                    deb.close()
                else:
                    print "Error! can't load network",ton,"on date",date
                
                return None
            
            if K.number_of_nodes() == 0 or K.number_of_edges() == 0:
                if debug:
                    deb = file( debug, 'a' )
                    deb.write( "WARNING!: the network "+ton+" at date "+date+" may be wrong! check it\n" )
                    deb.close()

        elif path.exists( path.join(lpath,date,'graphHistory.c2') ):
            #load network
            try:
                lang = path.split( lpath )[1]

            except IndexError:
                if debug:
                    deb = file( debug, 'a' )
                    deb.write( "ERROR: Cannot find lang of this wikinetwork ("+date+")\n" )
                    deb.close()
                return None

            if not lang:
                print "Lang value is not usable, this is the path "+lpath+" exiting"
                return None

            if cond_on_edge:
                print "Warning! condition on edge, not implemented in wikinetwork"

            K = Network.WikiNetwork( lang=lang, date=date, current=False, output=False )
            #netevolution only with history
        else:
            if debug:
                deb = file( debug, 'a' )
                deb.write( "ERROR!: Cannot be able to load network! (date="+date+") on network "+ton+"\n" )
                deb.close()
            else:
                print "Cannot be able to load network! (date="+date+") on network "+ton
            return None

        for function in calcfunctions: #foreach functions that must be calculated on this network
            if debug:
                deb = file( debug, 'a' )
                deb.write( "processing "+date+"\non function "+function.__name__+"\n" )
                deb.close()

            if function.__name__!='<lambda>':
                print 'Task:',function.__name__,"on date:",date

            res = function(K,date)
            try:
                pass
                #res = function(K,date)
            except Exception,e:
                if debug:
                    deb = file( debug, 'a' )
                    deb.write( "ERROR!: Error applying "+function.__name__+" to the network "+date+"! Exiting\n" )
                    deb.write(str(e)+'\n')
                    deb.close()
                else:
                    print "Error applying "+function.__name__+" to the network "+date+"! Exiting"
                    print e
                continue

            assert type(res) is tuple,'name: %s res %s' % (function.__name__,str(res))

            if function.__name__!='<lambda>':
                cachekey = {'function':function.__name__,'date':date}
                if cond_on_edge:
                    assert cond_on_edge.__name__!='<lambda>','Lambda function is not suppoeted for condition on edges'
                    cachekey['cond']=str(cond_on_edge.__name__)

                if not safe_save(cachekey,res,path.join(lpath,cachepath)):
                    print "Warning! I cannot be able to save cache for function",function.__name__,"on date",date
            
            resdict[function.__name__] = res

        return resdict

    #map list of result for each dataset in list of result for each function
    safe_merge(path.join(lpath,cachepath))
    if cacheonly:
        np = 1
    else:
        np = None
    data_ordered = splittask(task,dates,notasksout=True,np = np )
    safe_merge(path.join(lpath,cachepath))
    nd = len( dates )
    nf = len( functions )

    #print 'DEBUG',data_ordered
    
    func_ordered = []
    #prepare return value set to empty
    for fi in xrange( nf ):
        func_ordered.append( [] )

    if debug:
        deb = file( debug, 'a' )
        deb.write( "computation of functions finished! filling the return value\n" )
        deb.write( "data_ordered:\n"+str(data_ordered)+"\n" )
        deb.close()

    #fill the return value
    for fi in xrange( nf ):
        for di in xrange( nd ):
            if data_ordered[di]:
                if data_ordered[di].has_key( functions[fi].__name__ ):
                    func_ordered[fi].append( data_ordered[di][ functions[fi].__name__ ] )
            else:
                if debug:
                    deb = file(debug,'a')
                    deb.write('Warning: data_ordered[di] not defined\n')
                    deb.close()

    return func_ordered


def trustaverage( K, d ):
    """
    This function evaluate the trust average on more than one datasets.
    If you evaluate twice the same thing, the evaluate 
    function be able to remember it.(if you call it with evolutionmap)
    
    Parameters:
    K = network
    d = date
    """

    weight = K.weights_list()
    #try to use some dictionary, because
    #sometimes the key is 'value' and sometimes is 'level'
    if not weight:
        averagetrust = 0
    else:
        averagetrust = avg(weight)

    return (d,averagetrust)

def ta_plot(ta, dpath, filename="trustAverage"):
    prettyplot( ta, path.join(dpath,filename),
                title="Trust Average on time", showlines=True,
                xlabel='date',ylabel='trust average',
                comment=['Network: Advogato',
                         '>>> trustAverage( fromdate, todate, dpath, noObserver=False )'
            ]
                )
al(trustaverage,ta_plot)#0

    
def trustvariance( K, d ):
    """
    This function evaluate the trust variance on more than one datasets.
    If you evaluate twice the same thing, the evaluate 
    function be able to remember it (if you call it with evolutionmap).
    
    Parameters:
    K = network
    d = date
    """
    return (d,scipy.var(K.weights_list()))

def var_plot(var, dpath, filename="trustVariance"):
    
    prettyplot( var, path.join(dpath,filename),
                title="Trust Variance on time", showlines=True,
                xlabel='date',ylabel='trust variance',
                comment=['Network: Advogato',
                         '>>> trustAverage( fromdate, todate, dpath, noObserver=False )']
                )
al(trustvariance,var_plot)#1

def usersgrown(K,date):
        '''
        return the number of user for each network in date range
        '''
        return ( date,K.number_of_nodes() )

def plot_usersgrown(data,data_path='.'):
    '''
    data is the output of usersgrown
    >>> plot_usersgrown(usersgrown('trustlet/datasets/Advogato',range=('2000-01-01','2003-01-01')))
    '''
    fromdate = min(data,key=lambda x:x[0])[0]
    todate = max(data,key=lambda x:x[0])[0]
    prettyplot(data,path.join(data_path,'usersgrown (%s %s)'%(fromdate,todate)),
               title='Users Grown',
               xlabel='date [s] (from %s to %s)'%(fromdate,todate),
               ylabel='n. of users',
               showlines=True,
               comment='Network: Advogato'
               )
al(usersgrown,plot_usersgrown)#2

def numedges(K,date):
    '''
    return the number of user for each network in date range
    '''
    
    return ( date,K.number_of_edges() )

def plot_numedges(data,dpath='.'):
    '''
    >>> plot_*(*('trustlet/datasets/Advogato',range=('2000-01-01','2003-01-01')))
    '''
    fromdate = min(data,key=lambda x:x[0])[0]
    todate = max(data,key=lambda x:x[0])[0]
    prettyplot(data,path.join(dpath,'numedges (%s %s)'%(fromdate,todate)),
               title='Number of edges',
               xlabel='date [s] (from %s to %s)'%(fromdate,todate),
               ylabel='n. of edges',
               showlines=True,
               comment=['Network: Advogato','>>> plot_numedges(numedges(...))']
               )
al(numedges,plot_numedges)#3

def meandegree(K,date):
    return ( date,K.avg_degree() )


def plot_meandegree(data,data_path='.'):
    fromdate = min(data,key=lambda x:x[0])[0]
    todate = max(data,key=lambda x:x[0])[0]
    prettyplot(data, path.join( data_path,'meandegree (%s %s)'%(fromdate,todate) ),
               showlines=True,
               comment=['Network: Advogato','>>> plot_meandegree(meandegree(...))']
               )

al(meandegree,plot_meandegree)#4

def level_distribution(K,date):
    """
    see AdvogatoNetwork class
    this code (d = dict(...)) is copyed from there
    """
    
    # we use values()[0] instead of the key of dict because sometimes
    # the key is 'value' and sometimes it's 'level'
    # *need to fix this*
    d = dict(filter(lambda x:x[0],
                    map(lambda s: (s,
                                   len([e for e in K.edges_iter()
                                        if s in e[2].values()])),
                        K.level_map)))

    #order k from higher to lower values (Master to Observer)
    assert K.level_map,K.level_map

    l = [d[k] for k,v in sorted(K.level_map.items(),lambda x,y: cmp(y[1],x[1])) if k and d[k]]
    #temp: doesn't' work if: e.g. [0, a, b, c] -> becomes [a, b, c, 0]
    if len(l)<4:
        l += [0]*4
        l = l[:4]
    assert len(l)==4,l
    return ( date, map(lambda x:1.0*x/sum(l),l))

def plot_level_distribution(data,data_path='.'):

    # formatted data:
    # from: [(a,(b,c,d,e)), (a1,(b1,c1,d1,e1)), ...]
    # to:   [ [(a,b), (a1,b1), ...],[(a,c), (a1,c1), ...], [(a,d), ...], ... ]
    # lists of ['Master','Journeyer','Apprentice','Observer']

    if not data or not data[0] or not data[0][1]:
        return None

    f_data = [[],[],[],[]]
    for t in data:
        for i,l in enumerate(f_data):
            try:
                l.append((t[0],t[1][i]))
            except IndexError:
                print 'Warning: level_distribution skip',t[0]
                continue

    r = (min(data,key=lambda x:x[0])[0],max(data,key=lambda x:x[0])[0])
    prettyplot(f_data,path.join(data_path,'level distribution (%s %s)'%r),
               title='Level distribution',
               xlabel='dates (from %s to %s)'%r,
               ylabel='percentage of edges',
               legend=['Master','Journeyer','Apprentice','Observer'],
               showlines=True,
               comment=['Network: Advogato',
                        '>>> plot_level_distribution(level_distribution(...))']
               )
al(level_distribution,plot_level_distribution)#5

def avgcontroversiality(K,min_in_degree=10):
    '''
    generic function: not called directly
    '''

    cont = [] # controversiality array

    for n in K.nodes_iter():
        in_edges = K.in_edges(n)
        
        if len(in_edges)<min_in_degree:
            continue

        cont.append(
            numpy.std([K.level_map[x[2].values()[0]] for x in in_edges])
            # We get the first value because the key is sometimes
            # 'value' and sometimes 'level'
        )

    if not cont:
        return None
    else:
        return avg(cont)

def plot_generic(data,data_path='.',title='',comment=''):
    '''
    plot... ehm... generic output

    example:

    >>> plot_generic(
            genericevaluation('path/AdvogatoNetwork',networkx.average_clustering ,None),
            '.', title='Average clustering'
            )
    '''

    if not data or None in data:
        return None

    fromdate = min(data,key=lambda x:x[0])[0]
    todate = max(data,key=lambda x:x[0])[0]
    if not title:
        title = 'Untitled'
    prettyplot(
        data,
        path.join(data_path,'%s (%s %s)'%(title,fromdate,todate)),
        title=title,
        showlines=True,
        comment=comment,
        )



#generic evaluation
#avgcont10 = lambda G,d: (d,avgcontroversiality(G,10))
#avgcont10.__name__ = 'avgcontroversiality-min_in_degree-10'

avgcont20 = lambda G,d: (d,avgcontroversiality(G,20))
avgcont20.__name__ = 'avgcontroversiality-min_in_degree-20'
al(avgcont20,plot_generic)#6

al(lambda G,d:(d,networkx.average_clustering(G)),plot_generic)#7
fl[-1][0].__name__='average_clustering'

al(lambda G,d:(d,networkx.diameter(networkx.connected_component_subgraphs(G.to_undirected())[0])),plot_generic)#8
fl[-1][0].__name__='diameter-largest-connected-component'

al(lambda G,d:(d,networkx.radius(networkx.connected_component_subgraphs(G.to_undirected())[0])),plot_generic)#9
fl[-1][0].__name__='radius-largest-connected-component'

al(lambda G,d:(d,networkx.density(G)),plot_generic)#10
fl[-1][0].__name__='density'

al(lambda G,d:(d,avg(networkx.betweenness_centrality(G,normalized=True,weighted_edges=False).values())),plot_generic)#11
fl[-1][0].__name__ = 'betweenness_centrality-yes-normalized-no-weighted_edges'

def generate_eval(function):
    '''
    Return a function that calls function(Network)
    with get_edge method modified:
    it'll return values instead dictionaries on edges.
    '''
    def eval(G,date):
        assert hasattr(G,'level_map'),'I need level_map!'

        G.values_on_edges = True
        ret = function(G)
        G.values_on_edges = False
        return (date,ret)

    return eval

eval = generate_eval(lambda G:avg(networkx.betweenness_centrality(G,normalized=True,weighted_edges=True).values()))

al(eval,plot_generic)#12
fl[-1][0].__name__ = 'betweenness_centrality-yes-normalized-yes-weighted_edges'

al(lambda G,d: (d,avg(
    networkx.betweenness_centrality(G,normalized=False,weighted_edges=False).values()
    )),plot_generic)#13
fl[-1][0].__name__ = 'betweenness_centrality-no-normalized-no-weighted_edges'

eval = generate_eval(lambda G:avg(networkx.closeness_centrality(G,weighted_edges=False).values()))

al(eval,plot_generic)#14
fl[-1][0].__name__ = 'closeness_centrality-no-weighted_edges'

eval = generate_eval(lambda G:avg( networkx.closeness_centrality(G,weighted_edges=True).values() ) )

al(eval,plot_generic)#15
fl[-1][0].__name__ = 'closeness_centrality-yes-weighted_edges'

al(lambda G,d: (d,avg(
    networkx.newman_betweenness_centrality(G).values()
    )),plot_generic)#16
fl[-1][0].__name__ = 'newman_betweenness_centrality'


al(lambda G,d: (d,networkx.number_connected_components(G.to_undirected())),plot_generic)#17
fl[-1][0].__name__ = 'number_connected_components_undirect' 

al(lambda G,d: (d,1.0*len(G.connected_components()[0])/G.number_of_nodes()),plot_generic)#18
fl[-1][0].__name__ = 'percentage_of_users_in_main_cc'

def degrees_of_separation(G,d):
    nodes = set(networkx.kosaraju_strongly_connected_components(G)[0])
    pathsl = []

    for n in nodes:
        nodes.remove(n)
        for m in nodes:
            pathsl.append(len(networkx.shortest_path(G,n,m)))
        nodes.add(n)
    return (d,avg(pathsl))

al(degrees_of_separation,plot_generic)#19

al(lambda G,d: (d,len(networkx.kosaraju_strongly_connected_components(G))),plot_generic)#20
fl[-1][0].__name__ = 'number_connected_components_direct'

#function used for script.. do not use it if you use trustlet as library
def onlyMaster(e):
    return 'Master' in e[2].values()

def onlyMasterJourneyer(e):
    return 'Master' in e[2].values() or 'Journeyer' in e[2].values()

def noObserver(e):
    return 'Observer' in e[2].values()


if __name__ == "__main__":    
    import sys,os


    if sys.argv[1:] == ['list']:
        print 'Number of function:',len(fl)
        print 'List of functions:'
        for i,f in enumerate(fl):
            print '\t%2d'%i,f[0].__name__
        exit()

    if '--cacheonly' in sys.argv:
        sys.argv.remove('--cacheonly')
        cacheonly = True
    else:
        cacheonly = False

    if len(sys.argv) < 5:
        #prog startdate enddate path
        print "This script generate so many graphics with gnuplot (and generate .gnuplot file"
        print "useful to see the grown of the network in an interval of time"
        print "USAGE: netevolution.py startdate enddate networkname save_path [-s step] [--cacheonly] [-m|-mj|-mja] [-d debug_path]"
        print "    You can use '-' to skip {start,end}date"
        print "    step is the min numer of days between a computed network and the next one"
        print "    -m: only master edges (work only with advogato-like network)"
        print "    -mj: only master and journeyer edges (work only with advogato-like network)"
        print "    -mja: master and journeyer and apprentice edges (work only with advogato-like network)"
        print "    if you omit this command the computation will use all edges"
        print "    debug_path: path to a file filled with debug informations"
        print "OR netevolution.py list"
        print "   Show all function's names"
        sys.exit(1)


    startdate = sys.argv[1] == '-' and '1970-01-01' or sys.argv[1]
    enddate = sys.argv[2] == '-' and '9999-12-31' or sys.argv[2]
    netname = sys.argv[3]
    savepath = sys.argv[4]
    if '-s' in sys.argv[1:-1]:
        i = sys.argv.index('-s')
        step = int(sys.argv[i+1])
        del sys.argv[i+1]
        del sys.argv[i]
    else:
        step = 0

    cond_on_edge = None

    if '-m' in sys.argv:
        cond_on_edge = onlyMaster

    if '-mj' in sys.argv:
        cond_on_edge = onlyMasterJourneyer
    
    
    if '-mja' in sys.argv:
        cond_on_edge = noObserver

    
    range = (startdate,enddate,step)

    if '-d' in sys.argv:
        debugfile = sys.argv[sys.argv.index('-d')+1]
        mkpath(os.path.split(debugfile)[0])
    else:
        debugfile = None

    mkpath(savepath)

    data = evolutionmap( netname, [f[0] for f in fl], cond_on_edge, range, cacheonly, debugfile )
    
    if not data:
        sys.exit(1)

    #plot
    for (function,data_print),d in zip(fl,data):
        if data_print != plot_generic:
            data_print(d,savepath)

    plot_generic(
        data[7],
        savepath, title='adverage clustering',
        comment='networkx.average_clustering(G)'
        )

    plot_generic(
        data[8],
        savepath, title='diameter',
        comment='eval = nx.diameter(networkx.connected_component_subgraphs'
        '(G.to_undirected())[0])'
        )

    plot_generic(
        data[9],
        savepath, title='radius',
        comment='eval = nx.radius(networkx.connected_component_subgraphs'
                '(G.to_undirected())[0])'
        )

    plot_generic(
        data[10],
        savepath, title='density', comment='Function: nx.density'
        )

    plot_generic(
        data[11],
        savepath, title='betweenness_centrality yes-normalized no-weighted_edges',
        comment='eval = avg(nx.betweenness_centrality'
                '(G,normalized=True,weighted_edges=False).values())'
        )

    plot_generic(
        data[12],
        savepath, title='betweenness_centrality yes-normalized yes-weighted_edges',
        comment='eval = avg(nx.betweenness_centrality'
                '(G,normalized=True,weighted_edges=True).values())'
        ) 

    plot_generic(
        data[13],
        savepath, title='betweenness_centrality no-normalized no-weighted_edges',
        comment='eval = avg(nx.betweenness_centrality'
               '(G,normalized=False,weighted_edges=False).values())'
        )

    plot_generic(
        data[14],
        savepath, title='closeness_centrality no-weighted_edges',
        comment='eval = avg(nx.closeness_centrality'
                '(G,weighted_edges=False).values())'
        )

    plot_generic(
        data[15],
        savepath, title='closeness_centrality yes-weighted_edges',
        comment='eval = avg(nx.closeness_centrality'
                '(G,weighted_edges=True).values())'
        )

    plot_generic(
        data[16],
        savepath, title='newman betweenness centrality',
        comment='eval = avg(networkx.newman_betweenness_centrality(G).values())'
        )

    plot_generic(
        data[17],
        savepath, title='number_connected_components (undirect graph)',
        comment='eval = nx.number_connected_components(G.to_undirected())'
        )


    plot_generic(
        data[18],
        savepath, title='percentage of users in main connected component',
        comment='eval = len(G.connected_components()[0]) / G.number_of_nodes()'
        )

    plot_generic(
        data[19],
        savepath, title='mean degrees of separation',
        comment='''nodes = set(networkx.kosaraju_strongly_connected_components(G)[0])
pathsl = []

for n in nodes:
    nodes.remove(n)
    for m in nodes:
        pathsl.append(len(networkx.shortest_path(G,n,m)))
    nodes.add(n)
return (d,avg(pathsl))'''
        )

    plot_generic(
        data[20],
        savepath, title='number_connected_components (direct graph)',
        comment='eval = len(networkx.kosaraju_strongly_connected_components(G))'
        )


    plot_generic(
        data[6],
        savepath, title='avg of standard deviation in received trust (in degree=20)',
        comment='''\
cont = [] # controversiality array

for n in K.nodes_iter():
    in_edges = K.in_edges(n)

    # min_in_degree -> written in name of function
    if len(in_edges)<min_in_degree:
        continue

    cont.append(
        numpy.std([_obs_app_jour_mas_map[x[2]['level']] for x in in_edges])
    )

return avg(cont)'''
        )
