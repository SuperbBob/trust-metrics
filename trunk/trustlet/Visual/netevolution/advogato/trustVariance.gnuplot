#!/usr/bin/env gnuplot
# Title: Trust Variance on time
# Date: Mon Jan 26 17:24:46 2009
# Network: Advogato
# >>> trustAverage( fromdate, todate, dpath, noObserver=False )

set title "Trust Variance on time"
set data style linespoint
set xlabel "date"
set ylabel "trust variance"
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "trustVariance.png"
plot "-" using 1:2 title ""
2000-07-18         
2000-08-11         
2002-05-13         
2008-11-16         
2008-12-31         
e
