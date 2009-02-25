#!/usr/bin/env gnuplot
# Title: number_connected_components (direct graph)
# Date: Wed Jan 28 00:26:13 2009
# eval = len(networkx.kosaraju_strongly_connected_components(G))

set title "number_connected_components (direct graph)"
set data style linespoint
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "number_connected_components (direct graph) (2000-02-25 2003-04-10).png"
plot "-" using 1:2 title ""
2000-02-25 114
2000-07-18 555
2000-08-11 799
2000-09-28 941
2000-11-07 1054
2001-02-13 1321
2001-03-06 1369
2001-03-23 1413
2001-05-07 1483
2001-06-08 1546
2001-06-15 1563
2001-06-21 1574
2001-06-26 1573
2001-07-04 1577
2001-07-10 1589
2001-07-16 1615
2001-07-22 1622
2001-08-04 1646
2001-08-13 1652
2001-08-22 1671
2001-08-30 1688
2001-09-04 1697
2001-09-15 1711
2001-09-22 1726
2001-09-28 1735
2001-10-03 1742
2001-10-06 1747
2001-10-09 1745
2001-10-18 1765
2001-10-29 1785
2001-11-12 1818
2001-11-15 1827
2001-11-23 1854
2001-11-28 1868
2001-12-02 1870
2001-12-10 1887
2001-12-17 1905
2001-12-26 1913
2002-01-05 1939
2002-01-14 1953
2002-01-19 1963
2002-01-23 1971
2002-01-28 1969
2002-02-02 1980
2002-02-06 1986
2002-02-12 2003
2002-02-20 2002
2002-02-27 2012
2002-03-02 2016
2002-03-18 2042
2002-03-22 2050
2002-03-28 2063
2002-04-02 2066
2002-04-08 2086
2002-04-13 2098
2002-04-18 2107
2002-04-25 2119
2002-05-01 2136
2002-05-06 2142
2002-05-13 2151
2002-05-24 2174
2002-05-30 2181
2002-06-06 2185
2002-06-13 2198
2002-06-21 2206
2003-03-04 2611
2003-03-24 2642
2003-04-10 2666
e
