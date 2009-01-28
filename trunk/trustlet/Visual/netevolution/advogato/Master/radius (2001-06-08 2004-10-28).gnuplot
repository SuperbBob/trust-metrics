#!/usr/bin/env gnuplot
# Title: radius
# Date: Tue Jan 27 16:04:06 2009
# eval = nx.radius(networkx.connected_component_subgraphs(G.to_undirected())[0])

set title "radius"
set data style linespoint
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "radius (2001-06-08 2004-10-28).png"
plot "-" using 1:2 title ""
2001-06-08 4
2001-06-15 4
2001-06-21 4
2001-06-26 4
2001-07-04 4
2001-07-10 4
2001-07-16 4
2001-07-22 4
2001-08-04 4
2001-08-13 4
2001-08-22 4
2001-08-30 4
2001-09-04 4
2001-09-15 4
2001-09-22 4
2001-09-28 4
2001-10-03 4
2001-10-06 4
2001-10-09 4
2001-10-18 5
2001-10-29 4
2001-11-12 4
2001-11-15 4
2001-11-23 4
2001-11-28 4
2001-12-02 4
2001-12-10 4
2001-12-17 4
2001-12-26 4
2002-01-05 4
2002-01-14 4
2002-01-19 5
2002-01-23 5
2002-01-28 5
2002-02-02 5
2002-02-06 5
2002-02-12 5
2002-02-20 5
2002-02-27 5
2002-03-02 5
2002-03-18 5
2002-03-22 5
2002-03-28 5
2002-04-02 5
2002-04-08 5
2002-04-13 5
2002-04-18 5
2002-04-25 5
2002-05-01 5
2002-05-06 5
2002-05-13 5
2002-05-24 5
2002-05-30 5
2002-06-06 5
2002-06-13 5
2002-06-21 5
2003-03-04 5
2003-03-24 5
2003-04-10 5
2004-07-05 5
2004-10-28 0
e