#!/usr/bin/env gnuplot
# Title: betweenness_centrality no-normalized no-weighted_edges
# Date: Sat Nov  8 10:06:35 2008
# eval = avg(nx.betweenness_centrality(G,normalized=False,weighted_edges=False).values())

set title "betweenness_centrality no-normalized no-weighted_edges"
set data style linespoint
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "betweenness_centrality no-normalized no-weighted_edges (2004-10-28 2008-10-27).png"
plot "-" using 1:2 title ""
#2004-10-28 6161.41514965
#2005-11-11 6419.89330692
#2006-02-11 6581.05691275
#2006-05-20 6673.63946454
2007-08-27 6398.48109215
2007-10-13 6418.14895076
2007-10-14 6418.61615469
2007-10-15 6419.79174664
2007-10-16 6420.35284441
2007-10-17 6420.27772447
2007-10-18 6420.48951624
2007-10-19 6420.38508976
2007-10-20 6421.13949027
2007-10-21 6421.03877775
2007-10-22 6422.60989312
2007-10-23 6422.59509455
2007-10-24 6422.08522883
2007-10-25 6423.66072897
2007-10-26 6425.17424658
2007-10-27 6424.86671233
2007-10-28 6424.83945205
2007-10-29 6425.34502123
2007-10-30 6425.34502123
2007-10-31 6430.98657902
2007-11-01 6435.65621577
2007-11-02 6435.65142388
2007-11-03 6435.07531152
2007-11-04 6434.78693688
2007-11-05 6435.49370208
2007-11-06 6436.85350493
2007-11-07 6437.66383794
2007-11-08 6437.66383794
2007-11-09 6434.94072553
2007-11-10 6435.30595483
2007-11-11 6435.30581793
2007-11-12 6437.16671229
2007-11-13 6436.92773063
2007-11-14 6435.95784287
2007-11-15 6436.32311482
2007-11-16 6436.32311482
2007-11-17 6444.05691613
2007-11-18 6443.61061705
2007-11-19 6443.59748256
2007-11-20 6445.8683167
2007-11-21 6448.07423103
2007-11-22 6448.06848941
2007-11-23 6447.71182502
2007-11-24 6447.71182502
2007-11-25 6447.71182502
2007-11-26 6447.64360902
2007-11-27 6447.53896637
2007-11-28 6451.98633133
2007-11-29 6447.52365327
2007-11-30 6447.52091879
2007-12-01 6448.7771702
2007-12-02 6448.7771702
2007-12-03 6446.47621001
2007-12-04 6444.03323304
2007-12-05 6443.97497265
2007-12-06 6445.23652531
2007-12-07 6445.23652531
2007-12-08 6447.41367989
2007-12-09 6447.41367989
2007-12-10 6448.30775544
2007-12-11 6447.4128591
2007-12-12 6447.4128591
2007-12-13 6448.20982082
2007-12-14 6447.79370725
2007-12-15 6449.60793434
2007-12-16 6449.60793434
2007-12-17 6449.64154814
2007-12-18 6449.64154814
2007-12-19 6447.67200109
2007-12-20 6447.67200109
2007-12-21 6446.79020788
2007-12-22 6446.79020788
2007-12-23 6446.79020788
2007-12-24 6446.79020788
2007-12-25 6448.31163681
2007-12-26 6448.31163681
2007-12-27 6448.05127855
2007-12-28 6448.05127855
2007-12-29 6448.05127855
2007-12-30 6448.92589554
2007-12-31 6448.92589554
2008-01-01 6448.53048947
2008-01-02 6448.53048947
2008-01-03 6448.53048947
2008-01-04 6448.53035275
2008-01-05 6442.66963064
2008-01-06 6442.66963064
2008-01-07 6444.87633379
2008-01-08 6444.8497948
2008-01-09 6444.8497948
2008-01-10 6445.89372179
2008-01-11 6438.72407661
2008-01-12 6439.60251676
2008-01-13 6443.42982096
2008-01-14 6445.43378434
2008-01-15 6445.43378434
2008-01-16 6444.93836272
2008-01-17 6444.88082547
2008-01-18 6444.62457291
2008-01-19 6444.62457291
2008-01-20 6444.62457291
2008-01-21 6445.68324679
2008-01-22 6447.11326684
2008-01-23 6447.11326684
2008-01-24 6447.11326684
2008-01-25 6448.91925126
2008-01-26 6448.89957644
2008-01-27 6448.89957644
2008-01-28 6448.83454024
2008-01-30 6448.83454024
2008-01-31 6448.83454024
2008-02-01 6449.22653368
2008-02-02 6449.22653368
2008-02-03 6449.22653368
2008-02-04 6449.22653368
2008-02-05 6449.01434622
2008-02-06 6451.05176181
2008-02-07 6452.45397432
2008-02-08 6451.00136556
2008-02-10 6448.3947009
2008-02-11 6451.73002868
2008-02-12 6451.73002868
2008-02-13 6451.62583641
2008-02-14 6451.0540762
2008-02-15 6451.0540762
2008-02-16 6451.0540762
2008-02-17 6451.04246893
2008-02-18 6451.04246893
2008-02-19 6451.82536865
2008-02-20 6451.82536865
2008-02-21 6452.77802048
2008-02-22 6454.22260134
2008-02-23 6454.22260134
2008-02-24 6454.91129913
2008-02-25 6454.91129913
2008-02-26 6455.67348888
2008-02-27 6455.66748533
2008-02-28 6455.66748533
2008-02-29 6455.66748533
2008-03-01 6455.66748533
2008-03-02 6455.66748533
2008-03-03 6455.66748533
2008-03-05 6456.91882674
2008-03-06 6456.50150068
2008-03-07 6456.50150068
2008-03-08 6458.60782976
2008-03-09 6458.60782976
2008-03-10 6459.51554828
2008-03-11 6459.49127114
2008-03-12 6459.40302782
2008-03-13 6458.25821404
2008-03-14 6458.45357873
2008-03-15 6458.73514177
2008-03-16 6458.91293092
2008-03-17 6458.90543671
2008-03-18 6458.92682927
2008-03-19 6458.92682927
2008-03-20 6458.92682927
2008-03-21 6457.94740428
2008-03-22 6457.94740428
2008-03-23 6460.62547684
2008-03-24 6460.62547684
2008-03-25 6462.32111717
2008-03-26 6462.1760218
2008-03-27 6462.1760218
2008-03-28 6462.14659401
2008-03-29 6461.81389646
2008-03-30 6461.79168937
2008-03-31 6461.79168937
2008-04-01 6468.76668483
2008-04-02 6468.76668483
2008-04-03 6466.84048495
2008-04-04 6466.84048495
2008-04-06 6466.84048495
2008-04-07 6467.87932443
2008-04-08 6467.96705242
2008-04-09 6474.11301743
2008-04-10 6474.11301743
2008-04-11 6474.1119281
2008-04-12 6474.1119281
2008-04-13 6474.1119281
2008-04-14 6475.75462963
2008-04-15 6476.51545269
2008-04-16 6477.11465142
2008-04-17 6474.53731953
2008-04-18 6476.05841503
2008-04-19 6476.04370915
2008-04-20 6476.04370915
2008-04-23 6474.13439542
2008-04-24 6474.13439542
2008-04-25 6474.04520697
2008-04-26 6474.632403
2008-04-27 6471.9208878
2008-04-28 6472.66072158
2008-04-29 6474.59869317
2008-04-30 6472.20367597
2008-05-01 6472.23294758
2008-05-02 6472.23294758
2008-05-03 6477.42621835
2008-05-04 6477.42621835
2008-05-05 6477.42621835
2008-05-06 6478.18565401
2008-05-07 6478.18565401
2008-05-08 6480.02082483
2008-05-09 6480.02082483
2008-05-10 6480.02082483
2008-05-11 6480.02082483
2008-05-12 6480.02082483
2008-05-13 6483.36771911
2008-05-14 6484.55292517
2008-05-15 6482.91142857
2008-05-16 6479.51952647
2008-05-17 6479.51952647
2008-05-18 6479.51952647
2008-05-19 6480.27904762
2008-05-20 6480.27904762
2008-05-21 6480.27904762
2008-05-22 6480.27904762
2008-05-23 6480.03673469
2008-05-24 6480.03673469
2008-05-25 6480.03673469
2008-05-26 6480.03673469
2008-05-27 6481.55522307
2008-05-28 6478.2414966
2008-05-29 6478.2414966
2008-05-30 6479.37001768
2008-05-31 6479.37001768
2008-06-01 6479.29179703
2008-06-02 6479.29152496
2008-06-03 6479.16038634
2008-06-04 6479.14691879
2008-06-05 6479.12515304
2008-06-06 6475.20843537
2008-06-07 6475.20829932
2008-06-08 6476.37994831
2008-06-09 6476.29723847
2008-06-10 6475.12557823
2008-06-11 6475.12557823
2008-06-12 6475.71840566
2008-06-13 6475.71840566
2008-06-14 6475.71840566
2008-06-15 6475.71840566
2008-06-16 6475.71840566
2008-06-17 6475.71840566
2008-06-18 6475.71840566
2008-06-19 6475.71840566
2008-06-20 6474.83759521
2008-06-22 6474.69001632
2008-06-24 6472.89091404
2008-06-25 6474.09302326
2008-06-26 6476.8840087
2008-06-27 6478.90875714
2008-06-28 6478.90875714
2008-06-29 6478.90875714
2008-06-30 6478.83573565
2008-07-01 6483.06701101
2008-07-02 6483.06701101
2008-07-03 6483.06701101
2008-07-04 6483.03574827
2008-07-05 6483.00666032
2008-07-06 6483.00666032
2008-07-07 6483.54294645
2008-07-08 6483.54294645
2008-07-09 6484.45169181
2008-07-10 6484.31526023
2008-07-11 6484.31485256
2008-07-12 6484.31485256
2008-07-13 6484.31485256
2008-07-14 6488.79440141
2008-07-15 6488.79440141
2008-07-16 6488.79440141
2008-07-17 6490.19410486
2008-07-18 6488.90574494
2008-07-19 6489.65716225
2008-07-20 6495.52483713
2008-07-21 6495.52483713
2008-07-22 6496.28565613
2008-07-23 6495.44206242
2008-07-24 6495.44206242
2008-07-25 6495.44206242
2008-07-26 6495.44206242
2008-07-27 6495.44179104
2008-07-28 6495.42930801
2008-07-29 6501.77207977
2008-07-30 6502.31253391
2008-07-31 6504.1261359
2008-08-01 6503.62810254
2008-08-02 6503.52610878
2008-08-03 6503.52610878
2008-08-04 6504.80946569
2008-08-05 6504.80946569
2008-08-06 6504.80946569
2008-08-07 6514.9625712
2008-08-08 6514.95145104
2008-08-09 6515.41090317
2008-08-10 6515.41090317
2008-08-11 6515.41090317
2008-08-12 6517.34879306
2008-08-13 6518.30318644
2008-08-14 6517.24477895
2008-08-15 6517.24477895
2008-08-16 6517.24477895
2008-08-17 6516.36122034
2008-08-18 6516.36122034
2008-08-19 6516.3240678
2008-08-20 6516.3240678
2008-08-21 6516.3240678
2008-08-22 6516.3240678
2008-08-23 6516.3240678
2008-08-24 6516.3240678
2008-08-25 6516.3240678
2008-08-26 6516.21477966
2008-08-27 6516.07173854
2008-08-28 6513.8765767
2008-08-29 6513.8765767
2008-08-30 6513.68452462
2008-08-31 6513.68452462
2008-09-01 6513.24752475
2008-09-02 6515.2306128
2008-09-03 6521.3895664
2008-09-04 6520.57168022
2008-09-05 6520.57113821
2008-09-06 6520.57113821
2008-09-07 6521.86885246
2008-09-08 6521.86885246
2008-09-09 6521.86885246
2008-09-10 6521.81493023
2008-09-11 6521.81493023
2008-09-12 6521.80910446
2008-09-13 6521.80910446
2008-09-14 6521.72266631
2008-09-15 6521.71575667
2008-09-16 6520.61739602
2008-09-17 6520.61739602
2008-09-18 6520.61739602
2008-09-19 6520.61739602
2008-09-20 6520.61739602
2008-09-21 6520.61739602
2008-09-22 6521.49986454
2008-09-23 6530.52986591
2008-09-24 6530.52986591
2008-09-25 6537.12120802
2008-09-26 6537.12120802
2008-09-27 6537.12120802
2008-09-28 6536.40108328
2008-09-29 6535.46675694
2008-09-30 6535.44901828
2008-10-01 6535.44861205
2008-10-02 6535.44861205
2008-10-03 6535.44861205
2008-10-04 6535.16357481
2008-10-05 6537.26364252
2008-10-06 6537.23425863
2008-10-07 6537.99471974
2008-10-08 6537.92905497
2008-10-09 6537.92905497
2008-10-10 6538.76824151
2008-10-11 6539.82796427
2008-10-12 6538.65073778
2008-10-13 6538.65073778
2008-10-14 6537.7220417
2008-10-15 6537.7220417
2008-10-16 6538.79017192
2008-10-17 6538.79017192
2008-10-18 6538.77893597
2008-10-19 6538.76918912
2008-10-20 6537.17939345
2008-10-21 6538.68832927
2008-10-22 6541.09029376
2008-10-23 6538.65204441
2008-10-24 6538.54075278
2008-10-25 6538.54075278
2008-10-26 6538.54075278
2008-10-27 6538.61264555
e
