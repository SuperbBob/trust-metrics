#!/usr/bin/env gnuplot
# Title: Number of edges
# Date: Tue Jan 27 16:04:06 2009
# Network: Advogato
# >>> plot_numedges(numedges(...))

set title "Number of edges"
set data style linespoint
set xlabel "date [s] (from 2001-06-08 to 2004-10-28)"
set ylabel "n. of edges"
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "numedges (2001-06-08 2004-10-28).png"
plot "-" using 1:2 title ""
2001-06-08 7651
2001-06-15 7714
2001-06-21 7770
2001-06-26 7785
2001-07-04 7862
2001-07-10 7908
2001-07-16 7926
2001-07-22 7966
2001-08-04 8132
2001-08-13 8267
2001-08-22 8354
2001-08-30 8424
2001-09-04 8458
2001-09-15 8555
2001-09-22 8609
2001-09-28 8634
2001-10-03 8656
2001-10-06 8677
2001-10-09 8718
2001-10-18 8795
2001-10-29 8916
2001-11-12 9111
2001-11-15 9186
2001-11-23 9271
2001-11-28 9315
2001-12-02 9346
2001-12-10 9462
2001-12-17 9512
2001-12-26 9569
2002-01-05 9643
2002-01-14 9698
2002-01-19 9704
2002-01-23 9724
2002-01-28 9730
2002-02-02 9751
2002-02-06 9766
2002-02-12 9802
2002-02-20 9882
2002-02-27 9899
2002-03-02 9936
2002-03-18 10011
2002-03-22 10036
2002-03-28 10070
2002-04-02 10102
2002-04-08 10141
2002-04-13 10204
2002-04-18 10247
2002-04-25 10329
2002-05-01 10390
2002-05-06 10451
2002-05-13 10520
2002-05-24 10572
2002-05-30 10635
2002-06-06 10686
2002-06-13 10760
2002-06-21 10824
2003-03-04 12477
2003-03-24 12593
2003-04-10 12669
2004-07-05 14502
2004-10-28 0
e
