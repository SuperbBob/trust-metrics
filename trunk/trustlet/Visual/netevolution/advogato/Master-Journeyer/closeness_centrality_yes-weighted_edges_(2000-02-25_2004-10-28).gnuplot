#!/usr/bin/env gnuplot
# Title: closeness_centrality_yes-weighted_edges
# Date: Wed Feb 25 19:01:22 2009
# eval = avg(nx.closeness_centrality(G,weighted_edges=True).values())

set title "closeness_centrality_yes-weighted_edges"
set data style linespoint
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "closeness_centrality_yes-weighted_edges_(2000-02-25_2004-10-28).png"
plot "-" using 1:2 title ""
2000-02-25 0.31139632623
2000-07-18 0.308219199971
2000-08-11 0.289843590105
2000-09-28 0.287749244374
2000-11-07 0.286655002763
2001-02-13 0.283983819333
2001-03-06 0.281955593436
2001-03-23 0.281294092935
2001-05-07 0.281553859595
2001-06-08 0.28245930256
2001-06-15 0.283174467169
2001-06-21 0.284140072756
2001-06-26 0.283639213896
2001-07-04 0.284242324642
2001-07-10 0.283357872013
2001-07-16 0.285105426203
2001-07-22 0.284325236352
2001-08-04 0.285507726379
2001-08-13 0.285968587569
2001-08-22 0.286451800462
2001-08-30 0.28549268769
2001-09-04 0.285984321233
2001-09-15 0.285535596466
2001-09-22 0.285393588689
2001-09-28 0.285550610762
2001-10-03 0.284475800602
2001-10-06 0.284805411589
2001-10-09 0.285489416305
2001-10-18 0.284336270116
2001-10-29 0.284597081896
2001-11-12 0.286192754398
2001-11-15 0.285863567214
2001-11-23 0.285958257133
2001-11-28 0.285063520134
2001-12-02 0.285192899357
2001-12-10 0.283725090154
2001-12-17 0.282928789541
2001-12-26 0.282749878309
2002-01-05 0.28180184772
2002-01-14 0.281823004091
2002-01-19 0.282425802708
2002-01-23 0.282294536089
2002-01-28 0.28161459174
2002-02-02 0.281504069775
2002-02-06 0.281004271558
2002-02-12 0.281153626755
2002-02-20 0.281650874459
2002-02-27 0.281760239429
2002-03-02 0.281832672925
2002-03-18 0.281281360001
2002-03-22 0.280933975244
2002-03-28 0.280702648225
2002-04-02 0.280299444506
2002-04-08 0.281443320086
2002-04-13 0.280346461294
2002-04-18 0.280029855249
2002-04-25 0.280331507079
2002-05-01 0.279958398452
2002-05-06 0.279779248691
2002-05-13 0.279329822281
2002-05-24 0.279099261132
2002-05-30 0.278600200435
2002-06-06 0.279364502387
2002-06-13 0.278591090381
2002-06-21 0.278928361679
2003-03-04 0.274523743624
2003-03-24 0.273209785576
2003-04-10 0.272855962942
2004-07-05 0.26609712186
2004-10-28 0.154877234456
e
