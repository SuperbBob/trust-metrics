#!/usr/bin/env gnuplot
# Title: betweenness_centrality yes-normalized yes-weighted_edges
# Date: Wed Dec  3 09:08:51 2008
# eval = avg(nx.betweenness_centrality(G,normalized=True,weighted_edges=True).values())

set title "betweenness_centrality yes-normalized yes-weighted_edges"
set data style linespoint
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "betweenness_centrality yes-normalized yes-weighted_edges (2000-02-25 2008-10-07).png"
plot "-" using 1:2 title ""
2000-02-25 0.00404541752761
2000-07-18 0.00098731194151
2000-09-28 0.000595838193053
2001-02-13 0.00042094210878
2001-05-07 0.000371727327919
2001-07-16 0.000341005529958
2001-09-15 0.000316704659239
2001-11-23 0.000295153857109
2002-02-02 0.000277569645854
2002-04-08 0.00026321255033
2002-06-21 0.000248587090372
2003-03-04 0.000209709713073
2004-07-05 0.000161685668483
2004-10-28 7.76234997032e-06
2005-11-11 6.60277591242e-06
2006-02-11 6.14434176949e-06
2006-05-20 5.79941040372e-06
2006-10-01 2.05217591435e-05
2006-12-01 2.23480397776e-05
2007-02-01 2.2051634926e-05
2007-05-01 2.17344033969e-05
2007-07-01 2.1392418873e-05
2007-10-13 2.09440452426e-05
2007-12-12 2.06474051814e-05
2008-02-10 2.019051809e-05
2008-04-10 2.00026444672e-05
2008-06-09 1.97208533742e-05
2008-08-08 1.96842725736e-05
2008-10-07 1.96217174669e-05
e
