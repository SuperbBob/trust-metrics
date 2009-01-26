#!/usr/bin/env gnuplot
# Title: Trust Variance on time
# Date: Mon Jan 26 19:16:06 2009
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
2001-06-08 0.0311792533017
2001-06-15 0.0311376654705
2001-06-21 0.0311055767666
2001-06-26 0.0311166101955
2001-07-04 0.0311897720803
2001-07-10 0.0311815825784
2001-07-16 0.03189734468
2001-07-22 0.032007501574
2001-08-04 0.0318893408156
2001-08-13 0.0319441887629
2001-08-22 0.0319766869536
2001-08-30 0.0320021156615
2001-09-04 0.0320658372744
2001-09-15 0.0320323379248
2001-09-22 0.0321114355685
2001-09-28 0.0320818379337
2001-10-03 0.0320794341374
2001-10-06 0.0320432372866
2001-10-09 0.0320764498383
2001-10-18 0.0320216006712
2001-10-29 0.0319850608576
2001-11-12 0.0324594775882
2001-11-15 0.0324467825674
2001-11-23 0.0324013695657
2001-11-28 0.0323914637056
2001-12-02 0.0323233755852
2001-12-10 0.032310895729
2001-12-17 0.0322082035359
2001-12-26 0.0322354890372
2002-01-05 0.0322052621979
2002-01-14 0.032233438417
2002-01-19 0.0327146264041
2002-01-23 0.0326806344633
2002-01-28 0.0326833885119
2002-02-02 0.0326568439641
2002-02-06 0.0326264253284
2002-02-12 0.0326314268042
2002-02-20 0.0325758479438
2002-02-27 0.0325096913593
2002-03-02 0.032500923658
2002-03-18 0.0324719847158
2002-03-22 0.0324434109203
2002-03-28 0.0324720621925
2002-04-02 0.0324339712324
2002-04-08 0.0327015465953
2002-04-13 0.0326671070238
2002-04-18 0.0326269295703
2002-04-25 0.0326596851361
2002-05-01 0.0326697995947
2002-05-06 0.0326899798343
2002-05-13 0.0326782697805
2002-05-24 0.0326509210238
2002-05-30 0.0326396857859
2002-06-06 0.0325930160088
2002-06-13 0.0326224546607
2002-06-21 0.0327810118344
2003-03-04 0.0340218748118
2003-03-24 0.0339802151332
2003-04-10 0.034058434653
2004-07-05 0.0350696585917
2004-10-28 0.0351113107882
e