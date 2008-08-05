#!/usr/bin/env gnuplot
# Title: Number of edges
# Date: Tue Aug  5 20:48:30 2008

set title "Number of edges"
set data style linespoint
set xlabel "date [s] (from 2001-02-13 to 2007-11-01)"
set ylabel "n. of edges"
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "netevolution/numedges (2001-02-13 2007-11-01).png"
plot "-" using 1:2 title ""
2000-02-25 2109
2000-07-18 12176
2000-08-11 14117
2000-09-28 16689
2000-11-07 18429
2001-02-13 21806
2001-03-06 22486
2001-05-07 24678
2001-06-15 25871
2001-07-04 26412
2001-07-16 26824
2001-08-04 27613
2001-08-22 28535
2001-09-04 29033
2001-09-22 29611
2001-10-03 29763
2001-10-09 29904
2001-10-29 30444
2001-11-15 31135
2001-11-28 31479
2001-12-10 31852
2001-12-26 32280
2002-01-14 32743
2002-01-23 32907
2002-02-02 33048
2002-02-12 33201
2002-02-27 33523
2002-03-18 33854
2002-03-28 34034
2002-04-08 34275
2002-04-18 34557
2002-05-01 34916
2002-05-13 35218
2002-05-30 35573
2002-06-13 35986
2003-03-04 41308
2003-03-24 41590
2003-04-10 41766
2004-07-05 47338
2006-10-01 74540
2006-11-07 50274
2006-12-01 50620
2007-01-01 50779
2007-02-01 50798
2007-03-01 51905
2007-04-01 51475
2007-05-01 51577
2007-06-06 51300
2007-07-01 51277
2007-08-01 51388
2007-08-27 54243
2007-09-01 51415
2007-11-01 51724
2008-01-01 51624
2008-01-15 51574
2008-02-01 51624
2008-02-15 51668
2008-03-01 51688
2008-03-15 51737
2008-04-01 51784
2008-04-15 51796
2008-05-01 51743
2008-05-12 51751
2008-05-15 51755
e