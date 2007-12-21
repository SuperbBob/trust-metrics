"""
Generate some tables on the console.

For http://trustlet.org/wiki/A_comparison_of_trust_metrics_on_Advogato_social_network

For a certain dataset we want to have a table in which the rows are
the different trust metrics and the columns the evaluation techniques.

Rows:
* PageRank
* Advogato
* some moletrusts
* ebay
* always 1

Columns:
* coverage
* mean_abs_error
* root_mean_squared_error
* mean_abs_error on [0.4, 0.6, 0.8, 1.0]

for datasets: Kaitiaki, SqueakFoundation, Advogato

""" 

from helpers import get_name


def display(eval_measure, methods, evals):
    """Display evaluations in table."""
    from Table import Table
    tbl = Table([32] + [20] * len(methods))
    tbl.printHdr([eval_measure] + methods)
    tbl.printSep()

    def display_what(thing):
        if type(thing) == float:
            return "%f" % thing
        if thing == 0:
            return 0
        else:
            return "%f %i" % (thing[1], thing[0])

    for trust_metric in evals:
        tbl.printRow([trust_metric] + map(display_what, evals[trust_metric]))


def evals_with_conds(pred_graphs, eval_measure, conds_on_edges):
    """Evaluation with conditions."""
    evals = {}
    for pred_graph in pred_graphs:
        evals[get_name(pred_graph.TM)] = [getattr(pred_graph, eval_measure)(cond)
                                          for cond in conds_on_edges]
    return conds_on_edges, evals

if __name__ == "__main__":
    from Dataset.Advogato import AdvogatoNetwork, SqueakFoundationNetwork, KaitiakiNetwork
    from PredGraph import PredGraph
    from TrustMetric import EbayTM, OutA_TM
    G = SqueakFoundation() # Advogato()

    evaluated_trust_metrics = [EbayTM, OutA_TM]
    #evaluated_trust_metrics = [AlwaysMaster, AlwaysJourneyer,
    #AlwaysApprentice, AlwaysObserver, RandomTM, EbayTM, OutA_TM,
    #OutB_TM, EdgesB_TM, EdgesA_TM, MoletrustTM_horizon1_threshold0,
    #MoletrustTM_horizon2_threshold0, MoletrustTM_horizon3_threshold0,
    #MoletrustTM_horizon4_threshold0,
    #MoletrustTM_horizon1_threshold05,
    #MoletrustTM_horizon2_threshold05,
    #MoletrustTM_horizon3_threshold05,
    #MoletrustTM_horizon4_threshold05, AdvogatoGlobalTM, AdvogatoTM,
    #PageRankGlobalTM, PageRankTM0, GuakaMoleFullTM, GuakaMoleTM,
    #PaoloMoleTM, IntersectionTM, ]
    
    eval_measures = ['coverage_cond', 'abs_error_cond']
    conds_on_edges = ['and_cond(master, edge_to_connected_node(5))',
                      'and_cond(master, not_cond(edge_to_connected_node(5)))',
                      'and_cond(not_cond(master), edge_to_connected_node(5))']

    pred_graphs = map(lambda tm: PredGraph(G, tm), evaluated_trust_metrics)

    for eval_measure in eval_measures:
        conds, evals = evals_with_conds(pred_graphs,
                                        eval_measure, conds_on_edges)
        display(eval_measure, conds, evals)
        


