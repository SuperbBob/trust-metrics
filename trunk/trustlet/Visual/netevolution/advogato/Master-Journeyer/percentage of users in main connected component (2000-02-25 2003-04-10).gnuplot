#!/usr/bin/env gnuplot
# Title: percentage of users in main connected component
# Date: Wed Jan 28 00:26:13 2009
# eval = len(G.connected_components()[0]) / G.number_of_nodes()

set title "percentage of users in main connected component"
set data style linespoint
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "percentage of users in main connected component (2000-02-25 2003-04-10).png"
plot "-" using 1:2 title ""
2000-02-25 0.93
2000-07-18 0.858912594632
2000-08-11 0.827384123601
2000-09-28 0.819844535894
2000-11-07 0.822037422037
2001-02-13 0.80316042597
2001-03-06 0.803131245836
2001-03-23 0.800518134715
2001-05-07 0.799259944496
2001-06-08 0.797846889952
2001-06-15 0.796735905045
2001-06-21 0.79627439385
2001-06-26 0.795990566038
2001-07-04 0.797241784038
2001-07-10 0.796323314853
2001-07-16 0.794753531277
2001-07-22 0.795128939828
2001-08-04 0.793650793651
2001-08-13 0.793811533052
2001-08-22 0.792853154662
2001-08-30 0.793179927918
2001-09-04 0.793151063242
2001-09-15 0.792566274939
2001-09-22 0.792084575766
2001-09-28 0.791193949217
2001-10-03 0.791273902505
2001-10-06 0.791946308725
2001-10-09 0.792705819254
2001-10-18 0.791600212653
2001-10-29 0.791359325606
2001-11-12 0.790998448008
2001-11-15 0.791398403296
2001-11-23 0.790816326531
2001-11-28 0.790208016235
2001-12-02 0.791150442478
2001-12-10 0.792315419387
2001-12-17 0.79112662014
2001-12-26 0.790686153084
2002-01-05 0.79008102136
2002-01-14 0.790102389078
2002-01-19 0.789460903351
2002-01-23 0.789308176101
2002-01-28 0.789028516191
2002-02-02 0.78882735372
2002-02-06 0.78828612578
2002-02-12 0.78699497968
2002-02-20 0.786869647954
2002-02-27 0.787491115849
2002-03-02 0.787957497048
2002-03-18 0.786766425064
2002-03-22 0.785964094194
2002-03-28 0.785598141696
2002-04-02 0.78539976825
2002-04-08 0.784051624798
2002-04-13 0.783207157605
2002-04-18 0.782529156186
2002-04-25 0.782124175574
2002-05-01 0.781723591948
2002-05-06 0.782109058134
2002-05-13 0.782345013477
2002-05-24 0.782434239857
2002-05-30 0.782068353307
2002-06-06 0.781436464088
2002-06-13 0.781071585419
2002-06-21 0.781010719755
2003-03-04 0.771784232365
2003-03-24 0.770926756353
2003-04-10 0.76991643454
e
