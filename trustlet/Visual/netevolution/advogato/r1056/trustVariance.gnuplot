#!/usr/bin/env gnuplot
# Title: Trust Variance on time
# Date: Wed Dec  3 09:08:50 2008
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
2000-02-25 0.022520584521
2000-07-18 0.0277533902134
2000-09-28 0.0279579207471
2001-02-13 0.0294418752326
2001-05-07 0.0306703127267
2001-07-16 0.03189734468
2001-09-15 0.0320323379248
2001-11-23 0.0324013695657
2002-02-02 0.0326568439641
2002-04-08 0.0327015465953
2002-06-21 0.0327810118344
2003-03-04 0.0340218748118
2004-07-05 0.0350696585917
2004-10-28 0.0351113107882
2005-11-11 0.0347992350277
2006-02-11 0.0328936840646
2006-05-20 0.0327673421913
2006-10-01 0.03257060179
2006-12-01 0.0349875788793
2007-02-01 0.0349491083883
2007-05-01 0.0350207482134
2007-07-01 0.0342860354421
2007-10-13 0.0342400095862
2007-12-12 0.0341976116827
2008-02-10 0.0341973228871
2008-04-10 0.0341747980982
2008-06-09 0.0341704073239
2008-08-08 0.0341293904579
2008-10-07 0.0340586343716
e
