#!/usr/bin/env gnuplot
# Title: Level distribution
# Date: Tue Jan 27 16:04:06 2009
# Network: Advogato
# >>> plot_level_distribution(level_distribution(...))

set title "Level distribution"
set data style linespoint
set xlabel "dates (from 2001-06-08 to 2004-10-28)"
set ylabel "percentage of edges"
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "level distribution (2001-06-08 2004-10-28).png"
plot "-" using 1:2 title "Master", "-" using 1:2 title "Journeyer", "-" using 1:2 title "Apprentice", "-" using 1:2 title "Observer"
2001-06-08 1.0
2001-06-15 1.0
2001-06-21 1.0
2001-06-26 1.0
2001-07-04 1.0
2001-07-10 1.0
2001-07-16 1.0
2001-07-22 1.0
2001-08-04 1.0
2001-08-13 1.0
2001-08-22 1.0
2001-08-30 1.0
2001-09-04 1.0
2001-09-15 1.0
2001-09-22 1.0
2001-09-28 1.0
2001-10-03 1.0
2001-10-06 1.0
2001-10-09 1.0
2001-10-18 1.0
2001-10-29 1.0
2001-11-12 1.0
2001-11-15 1.0
2001-11-23 1.0
2001-11-28 1.0
2001-12-02 1.0
2001-12-10 1.0
2001-12-17 1.0
2001-12-26 1.0
2002-01-05 1.0
2002-01-14 1.0
2002-01-19 1.0
2002-01-23 1.0
2002-01-28 1.0
2002-02-02 1.0
2002-02-06 1.0
2002-02-12 1.0
2002-02-20 1.0
2002-02-27 1.0
2002-03-02 1.0
2002-03-18 1.0
2002-03-22 1.0
2002-03-28 1.0
2002-04-02 1.0
2002-04-08 1.0
2002-04-13 1.0
2002-04-18 1.0
2002-04-25 1.0
2002-05-01 1.0
2002-05-06 1.0
2002-05-13 1.0
2002-05-24 1.0
2002-05-30 1.0
2002-06-06 1.0
2002-06-13 1.0
2002-06-21 1.0
2003-03-04 1.0
2003-03-24 1.0
2003-04-10 1.0
2004-07-05 1.0
e
e
e
e
