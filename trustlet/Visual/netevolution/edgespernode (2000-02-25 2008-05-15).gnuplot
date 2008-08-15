#!/usr/bin/env gnuplot
# Title: Average Edges per Node
# Date: Sat Aug 16 00:19:36 2008
# Network: Advogato
# >>> plot_edgespernode(edgespernode(...))

set title "Average Edges per Node"
set data style linespoint
set xlabel "nodes"
set ylabel "number of edges per node"
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "edgespernode (2000-02-25 2008-05-15).png"
plot "-" using 1:2 title ""
2000-02-25 7.03
2000-07-18 8.37414030261
2000-08-11 7.50904255319
2000-09-28 7.62054794521
2000-11-07 7.65641877856
2001-02-13 7.48575351871
2001-03-06 7.48535286285
2001-05-07 7.60493066256
2001-06-15 7.67685459941
2001-07-04 7.74545454545
2001-07-16 7.72803226736
2001-08-04 7.8223796034
2001-08-22 7.96177455357
2001-09-04 8.01352470328
2001-09-22 8.02683654107
2001-10-03 8.01589011581
2001-10-09 8.01500938086
2001-10-29 8.01579778831
2001-11-15 8.01828483132
2001-11-28 7.98554033486
2001-12-10 7.99497991968
2001-12-26 7.99207724684
2002-01-14 7.98220380302
2002-01-23 7.96008708273
2002-02-02 7.95379061372
2002-02-12 7.93333333333
2002-02-27 7.93819559555
2002-03-18 7.91166160318
2002-03-28 7.90201996749
2002-04-08 7.89564616448
2002-04-18 7.89874285714
2002-05-01 7.89418946416
2002-05-13 7.90704984284
2002-05-30 7.89458499778
2002-06-13 7.90206411946
2003-03-04 7.78808446456
2003-03-24 7.76802390736
2003-04-10 7.75310933729
2004-07-05 7.51396825397
2006-10-01 5.37496394577
2006-11-07 3.90599021055
2006-12-01 3.94820996802
2007-01-01 3.94645216445
2007-02-01 3.93935633967
2007-03-01 4.01120556414
2007-04-01 3.96663327425
2007-05-01 3.95680859225
2007-06-06 3.91244661379
2007-07-01 3.91278138115
2007-08-01 3.90130580018
2007-08-27 7.41024590164
2007-09-01 3.89065455921
2007-11-01 3.88580872962
2008-01-01 3.85397536394
2008-01-15 7.05333698031
2008-02-01 7.05824446267
2008-02-15 7.06039901612
2008-03-01 7.05734571273
2008-03-15 7.05729095621
2008-04-01 7.05792558266
2008-04-15 7.05667574932
2008-05-01 7.04945504087
2008-05-12 7.04862435304
2008-05-15 7.04628999319
e
