#!/usr/bin/env gnuplot
# Title: betweenness_centrality yes-normalized yes-weighted_edges
# Date: Tue Jan 27 16:04:06 2009
# eval = avg(nx.betweenness_centrality(G,normalized=True,weighted_edges=True).values())

set title "betweenness_centrality yes-normalized yes-weighted_edges"
set data style linespoint
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "betweenness_centrality yes-normalized yes-weighted_edges (2001-06-08 2004-10-28).png"
plot "-" using 1:2 title ""
2001-06-08 4.79791708595e-05
2001-06-15 4.77172651268e-05
2001-06-21 4.80738421236e-05
2001-06-26 4.77059128375e-05
2001-07-04 4.99381287856e-05
2001-07-10 4.95602563502e-05
2001-07-16 4.80340122991e-05
2001-07-22 4.85917848463e-05
2001-08-04 4.60154222461e-05
2001-08-13 4.71117970996e-05
2001-08-22 4.77802520789e-05
2001-08-30 4.8297402545e-05
2001-09-04 4.77696701451e-05
2001-09-15 4.74678793799e-05
2001-09-22 4.81831446724e-05
2001-09-28 4.78607585824e-05
2001-10-03 4.78133401373e-05
2001-10-06 4.75134174993e-05
2001-10-09 4.75537170446e-05
2001-10-18 4.66813586902e-05
2001-10-29 4.58701812961e-05
2001-11-12 4.4233780855e-05
2001-11-15 4.43688171337e-05
2001-11-23 4.34184658945e-05
2001-11-28 4.37813758187e-05
2001-12-02 4.36020080075e-05
2001-12-10 4.34218768565e-05
2001-12-17 4.28970766815e-05
2001-12-26 4.23405050498e-05
2002-01-05 4.17245611183e-05
2002-01-14 4.09163836525e-05
2002-01-19 4.07342506509e-05
2002-01-23 4.0454336156e-05
2002-01-28 4.04392679279e-05
2002-02-02 4.02491279969e-05
2002-02-06 4.01670033518e-05
2002-02-12 3.96647298479e-05
2002-02-20 3.9599652491e-05
2002-02-27 3.89223926098e-05
2002-03-02 3.86446376404e-05
2002-03-18 3.84725312419e-05
2002-03-22 3.81501433547e-05
2002-03-28 3.79878322683e-05
2002-04-02 3.85924351551e-05
2002-04-08 3.84102548006e-05
2002-04-13 3.88589313475e-05
2002-04-18 3.86680883928e-05
2002-04-25 3.88151888968e-05
2002-05-01 3.89151663618e-05
2002-05-06 3.86500254926e-05
2002-05-13 3.88142336869e-05
2002-05-24 3.83318936211e-05
2002-05-30 3.84032977216e-05
2002-06-06 3.86428842612e-05
2002-06-13 3.82349318223e-05
2002-06-21 3.82555995413e-05
2003-03-04 3.70000511395e-05
2003-03-24 3.63363995903e-05
2003-04-10 3.58964270029e-05
2004-07-05 2.77909819561e-05
2004-10-28 0.0
e
