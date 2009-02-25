#!/usr/bin/env gnuplot
# Title: betweenness_centrality_yes-normalized_yes-weighted_edges
# Date: Wed Feb 25 19:01:14 2009
# eval = avg(nx.betweenness_centrality(G,normalized=True,weighted_edges=True).values())

set title "betweenness_centrality_yes-normalized_yes-weighted_edges"
set data style linespoint
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "betweenness_centrality_yes-normalized_yes-weighted_edges_(2000-02-25_2004-10-28).png"
plot "-" using 1:2 title ""
2000-02-25 0.00404601359853
2000-07-18 0.000988278814506
2000-08-11 0.000713216217039
2000-09-28 0.000597100894012
2000-11-07 0.000538007745221
2001-02-13 0.000420980505039
2001-03-06 0.00040476514065
2001-03-23 0.000391401635711
2001-05-07 0.000371766087127
2001-06-08 0.000357176384147
2001-06-15 0.000353039671618
2001-06-21 0.000350390289298
2001-06-26 0.000349923382052
2001-07-04 0.000349465331315
2001-07-10 0.000346677627121
2001-07-16 0.000341005529958
2001-07-22 0.000339201463178
2001-08-04 0.000332017133984
2001-08-13 0.000329021791443
2001-08-22 0.00032471331792
2001-08-30 0.000321353979916
2001-09-04 0.00031947197513
2001-09-15 0.000316736246202
2001-09-22 0.000313932542146
2001-09-28 0.000312088401212
2001-10-03 0.000311141316759
2001-10-06 0.000310881199514
2001-10-09 0.000311204296789
2001-10-18 0.00030730421196
2001-10-29 0.000303816316063
2001-11-12 0.000300683588574
2001-11-15 0.000298952364957
2001-11-23 0.000295175035766
2001-11-28 0.000293061751098
2001-12-02 0.000292981612797
2001-12-10 0.000291265703039
2001-12-17 0.000288193768673
2001-12-26 0.000286816840159
2002-01-05 0.000283238248788
2002-01-14 0.000281408129722
2002-01-19 0.00028037554066
2002-01-23 0.000278880977593
2002-01-28 0.00027911042278
2002-02-02 0.000277569645854
2002-02-06 0.000276412990241
2002-02-12 0.000273876327399
2002-02-20 0.000273656781192
2002-02-27 0.000272280138101
2002-03-02 0.000271773265824
2002-03-18 0.000268775289623
2002-03-22 0.000267403390006
2002-03-28 0.000265830510666
2002-04-02 0.000265305969976
2002-04-08 0.00026321255033
2002-04-13 0.000261577176003
2002-04-18 0.000260311408034
2002-04-25 0.00025842938669
2002-05-01 0.00025664885247
2002-05-06 0.000256132098192
2002-05-13 0.000255336798585
2002-05-24 0.000252486394013
2002-05-30 0.000251713414863
2002-06-06 0.000250928259812
2002-06-13 0.000249327732784
2002-06-21 0.000248587090372
2003-03-04 0.000209672178335
2003-03-24 0.000207511487486
2003-04-10 0.000205881069365
2004-07-05 0.0001615880524
2004-10-28 3.10495563276e-05
e
