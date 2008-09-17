#!/usr/bin/env gnuplot
# Title: newman betweenness centrality
# Date: Sat Aug 16 00:23:10 2008
# eval = avg(networkx.newman_betweenness_centrality(G).values())

set title "newman betweenness centrality"
set data style linespoint
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "newman betweenness centrality (2000-02-25 2008-05-15).png"
plot "-" using 1:2 title ""
2000-02-25 0.0040950446305
2000-07-18 0.000938964295911
2000-08-11 0.000678372592295
2000-09-28 0.000571390799884
2000-11-07 0.000516159643373
2001-02-13 0.000405559562994
2001-03-06 0.000390478473221
2001-05-07 0.000359042305303
2001-06-15 0.000341133556811
2001-07-04 0.000337600779153
2001-07-16 0.000329019086596
2001-08-04 0.000320060627735
2001-08-22 0.000313179946436
2001-09-04 0.000307872402016
2001-09-22 0.000302596382643
2001-10-03 0.00030002041305
2001-10-09 0.000300125349355
2001-10-29 0.000292999001475
2001-11-15 0.000286438157572
2001-11-28 0.00028095350215
2001-12-10 0.00027940343306
2001-12-26 0.000274916493557
2002-01-14 0.000269789821492
2002-01-23 0.000267121905979
2002-02-02 0.000265978573324
2002-02-12 0.000262504730096
2002-02-27 0.000261081094003
2002-03-18 0.000257716330841
2002-03-28 0.000254830555717
2002-04-08 0.000251381381288
2002-04-18 0.000248666879165
2002-05-01 0.000245260489178
2002-05-13 0.000243994880754
2002-05-30 0.000240567817695
2002-06-13 0.000238401067012
2003-03-04 0.000201011644122
2003-03-24 0.000198965797819
2003-04-10 0.000197410297767
2004-07-05 0.000155054555312
2006-10-01 1.97689660676e-05
2006-11-07 2.12985121312e-05
2006-12-01 2.14536203889e-05
2007-01-01 2.12893550792e-05
2007-02-01 2.1171368594e-05
2007-03-01 2.12329985105e-05
2007-04-01 2.10583438497e-05
2007-05-01 2.08518625219e-05
2007-06-06 2.04112567411e-05
2007-07-01 2.05102974501e-05
2007-08-01 2.03331106267e-05
2007-08-27 0.000119642168593
2007-09-01 2.01395567279e-05
2007-11-01 1.9951416414e-05
2008-01-01 1.96443915488e-05
2008-01-15 0.00012078378814
2008-02-01 0.000120788708939
2008-02-15 0.000120690759752
2008-03-01 0.000120579097947
2008-03-15 0.000120405980476
2008-04-01 0.000120395609676
2008-04-15 0.000120441174964
2008-05-01 0.000120361602056
2008-05-12 0.000120440684471
2008-05-15 0.0001203959069
e