#!/usr/bin/env gnuplot
# Title: Level distribution
# Date: Tue Aug  5 20:48:30 2008

set title "Level distribution"
set data style linespoint
set xlabel "dates (from 2001-02-13 to 2007-11-01)"
set ylabel "percentage of edges"
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "netevolution/level distribution (2001-02-13 2007-11-01).png"
plot "-" using 1:2 title "Master", "-" using 1:2 title "Journeyer", "-" using 1:2 title "Apprentice", "-" using 1:2 title "Observer"
2000-02-25 33.2385016596
2000-07-18 32.0220105125
2000-08-11 31.2956010484
2000-09-28 30.4931391935
2000-11-07 30.9403657279
2001-02-13 30.2347977621
2001-03-06 30.1743306947
2001-05-07 29.8808655483
2001-06-15 29.817169804
2001-07-04 29.7667726791
2001-07-16 29.5481658217
2001-08-04 29.4498967877
2001-08-22 29.2763273173
2001-09-04 29.1323666173
2001-09-22 29.0736550606
2001-10-03 29.0830897423
2001-10-09 29.1532905297
2001-10-29 29.2865589279
2001-11-15 29.5037738879
2001-11-28 29.5911560088
2001-12-10 29.7061409017
2001-12-26 29.6437422553
2002-01-14 29.6185444217
2002-01-23 29.549943781
2002-02-02 29.5055676592
2002-02-12 29.5232071323
2002-02-27 29.5289801032
2002-03-18 29.571099427
2002-03-28 29.5880589998
2002-04-08 29.587162655
2002-04-18 29.6524582574
2002-05-01 29.7571314011
2002-05-13 29.8710886479
2002-05-30 29.8962696427
2002-06-13 29.9005168677
2003-03-04 30.2144862981
2003-03-24 30.2885308969
2003-04-10 30.3428626155
2004-07-05 30.6434576873
2006-10-01 38.3096324121
2006-11-07 31.7659227434
2006-12-01 31.6594231529
2007-01-01 31.6587565726
2007-02-01 31.7492814678
2007-03-01 31.6289374819
2007-04-01 31.7649344342
2007-05-01 31.7874246273
2007-06-06 32.0155945419
2007-07-01 32.0377557189
2007-08-01 32.1397991749
2007-08-27 33.3923271206
2007-09-01 32.1229213265
2007-11-01 32.22875261
2008-01-01 32.2582519758
2008-01-15 32.3147322294
2008-02-01 32.3551061522
2008-02-15 32.3585197801
2008-03-01 32.3730846618
2008-03-15 32.4139397337
2008-04-01 32.4212111849
2008-04-15 32.4214225037
2008-05-01 32.4507662872
2008-05-12 32.4534791598
2008-05-15 32.4529031011
e
2000-02-25 49.9288762447
2000-07-18 48.5298948752
2000-08-11 47.1842459446
2000-09-28 46.6175325064
2000-11-07 45.5694828802
2001-02-13 44.7537375034
2001-03-06 44.774526372
2001-05-07 44.2661479861
2001-06-15 44.10343628
2001-07-04 44.0405876117
2001-07-16 43.8748881599
2001-08-04 43.8308043313
2001-08-22 43.8023479937
2001-09-04 43.7708814108
2001-09-22 43.7371247172
2001-10-03 43.7388704096
2001-10-09 43.6964954521
2001-10-29 43.6407830771
2001-11-15 43.2599967882
2001-11-28 43.2701165857
2001-12-10 43.2343337938
2001-12-26 43.3333333333
2002-01-14 43.3588858687
2002-01-23 43.1731850366
2002-02-02 43.2007988381
2002-02-12 43.2005060089
2002-02-27 43.2747665782
2002-03-18 43.2917823595
2002-03-28 43.3066933067
2002-04-08 43.2093362509
2002-04-18 43.2039818271
2002-05-01 43.1750486883
2002-05-13 43.1029587143
2002-05-30 43.119781857
2002-06-13 43.0750847552
2003-03-04 42.2896291275
2003-03-24 42.3034383265
2003-04-10 42.2353110185
2004-07-05 41.5902657484
2006-10-01 37.9205795546
2006-11-07 41.045073
2006-12-01 41.2998814698
2007-01-01 41.3655251187
2007-02-01 41.3106815229
2007-03-01 41.3312782969
2007-04-01 41.3423992229
2007-05-01 41.3692149602
2007-06-06 41.5497076023
2007-07-01 41.6229498606
2007-08-01 41.5680703666
2007-08-27 41.6791106687
2007-09-01 41.6084800156
2007-11-01 41.6479777279
2008-01-01 41.6550441655
2008-01-15 41.6333811611
2008-02-01 41.616302495
2008-02-15 41.6253774096
2008-03-01 41.6170097508
2008-03-15 41.5988557512
2008-04-01 41.6093774139
2008-04-15 41.6074600355
2008-05-01 41.6288193572
2008-05-12 41.6281810979
2008-05-15 41.6288281325
e
2000-02-25 14.1299193931
2000-07-18 13.3377135348
2000-08-11 15.7328044202
2000-09-28 17.3707232309
2000-11-07 18.0910521461
2001-02-13 18.8892965239
2001-03-06 18.9762518901
2001-05-07 18.8426938974
2001-06-15 18.719802095
2001-07-04 18.8058458277
2001-07-16 18.6213838354
2001-08-04 18.7773874624
2001-08-22 18.8995969862
2001-09-04 18.9956256673
2001-09-22 19.0537300328
2001-10-03 19.0706581998
2001-10-09 19.0643392188
2001-10-29 19.094074366
2001-11-15 18.9914886783
2001-11-28 18.945963976
2001-12-10 18.9564234585
2001-12-26 18.9498141264
2002-01-14 18.941453135
2002-01-23 18.837937217
2002-02-02 18.8846526265
2002-02-12 18.8909972591
2002-02-27 18.8944903499
2002-03-18 18.8663082649
2002-03-28 18.8311688312
2002-04-08 18.7600291758
2002-04-18 18.7718841335
2002-05-01 18.6762515752
2002-05-13 18.6580725765
2002-05-30 18.6461642257
2002-06-13 18.7156116267
2003-03-04 18.2385978503
2003-03-24 18.1894686223
2003-04-10 18.1607048796
2004-07-05 17.8461278466
2006-10-01 17.1022269922
2006-11-07 17.4265027648
2006-12-01 17.3528249704
2007-01-01 17.3181827133
2007-02-01 17.288082208
2007-03-01 17.3663423562
2007-04-01 17.1384167071
2007-05-01 17.1103398802
2007-06-06 17.2124756335
2007-07-01 17.1733915791
2007-08-01 17.1479722893
2007-08-27 16.267536825
2007-09-01 17.1311873967
2007-11-01 17.0443121182
2008-01-01 17.0037192004
2008-01-15 16.9717299414
2008-02-01 16.9572291957
2008-02-15 16.9544011767
2008-03-01 16.9517102616
2008-03-15 16.9395210391
2008-04-01 16.9299397497
2008-04-15 16.9337400571
2008-05-01 16.8950389425
2008-05-12 16.8943595293
2008-05-15 16.8949859917
e
2000-02-25 2.7027027027
2000-07-18 6.11038107753
2000-08-11 5.78734858681
2000-09-28 5.51860506921
2000-11-07 5.39909924575
2001-02-13 6.12216821058
2001-03-06 6.07489104332
2001-05-07 7.01029256828
2001-06-15 7.35959182096
2001-07-04 7.38679388157
2001-07-16 7.95556218312
2001-08-04 7.94191141853
2001-08-22 8.02172770282
2001-09-04 8.10112630455
2001-09-22 8.13549018946
2001-10-03 8.10738164836
2001-10-09 8.08587479936
2001-10-29 7.97858362896
2001-11-15 8.24474064558
2001-11-28 8.19276342959
2001-12-10 8.10310184604
2001-12-26 8.07311028501
2002-01-14 8.08111657454
2002-01-23 8.43893396542
2002-02-02 8.4089808763
2002-02-12 8.38528959971
2002-02-27 8.30176296871
2002-03-18 8.2708099486
2002-03-28 8.27407886231
2002-04-08 8.44347191831
2002-04-18 8.37167578204
2002-05-01 8.39156833543
2002-05-13 8.36788006133
2002-05-30 8.33778427459
2002-06-13 8.3087867504
2003-03-04 9.25728672412
2003-03-24 9.21856215436
2003-04-10 9.26112148638
2004-07-05 9.92014871773
2006-10-01 6.66756104105
2006-11-07 9.76250149182
2006-12-01 9.68787040695
2007-01-01 9.65753559542
2007-02-01 9.65195480137
2007-03-01 9.67344186495
2007-04-01 9.75424963575
2007-05-01 9.73302053241
2007-06-06 9.22222222222
2007-07-01 9.16590284143
2007-08-01 9.14415816922
2007-08-27 8.66102538576
2007-09-01 9.13741126131
2007-11-01 9.07895754389
2008-01-01 9.0829846583
2008-01-15 9.08015666809
2008-02-01 9.07136215714
2008-02-15 9.06170163351
2008-03-01 9.0581953258
2008-03-15 9.04768347604
2008-04-01 9.03947165148
2008-04-15 9.03737740366
2008-05-01 9.0253754131
2008-05-12 9.02398021294
2008-05-15 9.02328277461
e
