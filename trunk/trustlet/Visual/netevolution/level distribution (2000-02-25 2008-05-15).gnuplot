#!/usr/bin/env gnuplot
# Title: Level distribution
# Date: Sat Aug 16 01:13:24 2008
# Network: Advogato
# >>> plot_level_distribution(level_distribution(...))

set title "Level distribution"
set data style linespoint
set xlabel "dates (from 2000-02-25 to 2008-05-15)"
set ylabel "percentage of edges"
set xdata time
set timefmt "%Y-%m-%d"
set terminal png
set output "level distribution (2000-02-25 2008-05-15).png"
plot "-" using 1:2 title "Master", "-" using 1:2 title "Journeyer", "-" using 1:2 title "Apprentice", "-" using 1:2 title "Observer"
2000-02-25 0.332385016596
2000-07-18 0.320220105125
2000-08-11 0.312956010484
2000-09-28 0.304931391935
2000-11-07 0.309403657279
2001-02-13 0.302347977621
2001-03-06 0.301743306947
2001-05-07 0.298808655483
2001-06-15 0.29817169804
2001-07-04 0.297667726791
2001-07-16 0.295481658217
2001-08-04 0.294498967877
2001-08-22 0.292763273173
2001-09-04 0.291323666173
2001-09-22 0.290736550606
2001-10-03 0.290830897423
2001-10-09 0.291532905297
2001-10-29 0.292865589279
2001-11-15 0.295037738879
2001-11-28 0.295911560088
2001-12-10 0.297061409017
2001-12-26 0.296437422553
2002-01-14 0.296185444217
2002-01-23 0.29549943781
2002-02-02 0.295055676592
2002-02-12 0.295232071323
2002-02-27 0.295289801032
2002-03-18 0.29571099427
2002-03-28 0.295880589998
2002-04-08 0.29587162655
2002-04-18 0.296524582574
2002-05-01 0.297571314011
2002-05-13 0.298710886479
2002-05-30 0.298962696427
2002-06-13 0.299005168677
2003-03-04 0.302144862981
2003-03-24 0.302885308969
2003-04-10 0.303428626155
2004-07-05 0.306434576873
2006-10-01 0.383096324121
2006-11-07 0.317659227434
2006-12-01 0.316594231529
2007-01-01 0.316587565726
2007-02-01 0.317492814678
2007-03-01 0.316289374819
2007-04-01 0.317649344342
2007-05-01 0.317874246273
2007-06-06 0.320155945419
2007-07-01 0.320377557189
2007-08-01 0.321397991749
2007-08-27 0.333923271206
2007-09-01 0.321229213265
2007-11-01 0.3222875261
2008-01-01 0.322582519758
2008-01-15 0.323147322294
2008-02-01 0.323551061522
2008-02-15 0.323585197801
2008-03-01 0.323730846618
2008-03-15 0.324139397337
2008-04-01 0.324212111849
2008-04-15 0.324214225037
2008-05-01 0.324507662872
2008-05-12 0.324534791598
2008-05-15 0.324529031011
e
2000-02-25 0.499288762447
2000-07-18 0.485298948752
2000-08-11 0.471842459446
2000-09-28 0.466175325064
2000-11-07 0.455694828802
2001-02-13 0.447537375034
2001-03-06 0.44774526372
2001-05-07 0.442661479861
2001-06-15 0.4410343628
2001-07-04 0.440405876117
2001-07-16 0.438748881599
2001-08-04 0.438308043313
2001-08-22 0.438023479937
2001-09-04 0.437708814108
2001-09-22 0.437371247172
2001-10-03 0.437388704096
2001-10-09 0.436964954521
2001-10-29 0.436407830771
2001-11-15 0.432599967882
2001-11-28 0.432701165857
2001-12-10 0.432343337938
2001-12-26 0.433333333333
2002-01-14 0.433588858687
2002-01-23 0.431731850366
2002-02-02 0.432007988381
2002-02-12 0.432005060089
2002-02-27 0.432747665782
2002-03-18 0.432917823595
2002-03-28 0.433066933067
2002-04-08 0.432093362509
2002-04-18 0.432039818271
2002-05-01 0.431750486883
2002-05-13 0.431029587143
2002-05-30 0.43119781857
2002-06-13 0.430750847552
2003-03-04 0.422896291275
2003-03-24 0.423034383265
2003-04-10 0.422353110185
2004-07-05 0.415902657484
2006-10-01 0.379205795546
2006-11-07 0.41045073
2006-12-01 0.412998814698
2007-01-01 0.413655251187
2007-02-01 0.413106815229
2007-03-01 0.413312782969
2007-04-01 0.413423992229
2007-05-01 0.413692149602
2007-06-06 0.415497076023
2007-07-01 0.416229498606
2007-08-01 0.415680703666
2007-08-27 0.416791106687
2007-09-01 0.416084800156
2007-11-01 0.416479777279
2008-01-01 0.416550441655
2008-01-15 0.416333811611
2008-02-01 0.41616302495
2008-02-15 0.416253774096
2008-03-01 0.416170097508
2008-03-15 0.415988557512
2008-04-01 0.416093774139
2008-04-15 0.416074600355
2008-05-01 0.416288193572
2008-05-12 0.416281810979
2008-05-15 0.416288281325
e
2000-02-25 0.141299193931
2000-07-18 0.133377135348
2000-08-11 0.157328044202
2000-09-28 0.173707232309
2000-11-07 0.180910521461
2001-02-13 0.188892965239
2001-03-06 0.189762518901
2001-05-07 0.188426938974
2001-06-15 0.18719802095
2001-07-04 0.188058458277
2001-07-16 0.186213838354
2001-08-04 0.187773874624
2001-08-22 0.188995969862
2001-09-04 0.189956256673
2001-09-22 0.190537300328
2001-10-03 0.190706581998
2001-10-09 0.190643392188
2001-10-29 0.19094074366
2001-11-15 0.189914886783
2001-11-28 0.18945963976
2001-12-10 0.189564234585
2001-12-26 0.189498141264
2002-01-14 0.18941453135
2002-01-23 0.18837937217
2002-02-02 0.188846526265
2002-02-12 0.188909972591
2002-02-27 0.188944903499
2002-03-18 0.188663082649
2002-03-28 0.188311688312
2002-04-08 0.187600291758
2002-04-18 0.187718841335
2002-05-01 0.186762515752
2002-05-13 0.186580725765
2002-05-30 0.186461642257
2002-06-13 0.187156116267
2003-03-04 0.182385978503
2003-03-24 0.181894686223
2003-04-10 0.181607048796
2004-07-05 0.178461278466
2006-10-01 0.171022269922
2006-11-07 0.174265027648
2006-12-01 0.173528249704
2007-01-01 0.173181827133
2007-02-01 0.17288082208
2007-03-01 0.173663423562
2007-04-01 0.171384167071
2007-05-01 0.171103398802
2007-06-06 0.172124756335
2007-07-01 0.171733915791
2007-08-01 0.171479722893
2007-08-27 0.16267536825
2007-09-01 0.171311873967
2007-11-01 0.170443121182
2008-01-01 0.170037192004
2008-01-15 0.169717299414
2008-02-01 0.169572291957
2008-02-15 0.169544011767
2008-03-01 0.169517102616
2008-03-15 0.169395210391
2008-04-01 0.169299397497
2008-04-15 0.169337400571
2008-05-01 0.168950389425
2008-05-12 0.168943595293
2008-05-15 0.168949859917
e
2000-02-25 0.027027027027
2000-07-18 0.0611038107753
2000-08-11 0.0578734858681
2000-09-28 0.0551860506921
2000-11-07 0.0539909924575
2001-02-13 0.0612216821058
2001-03-06 0.0607489104332
2001-05-07 0.0701029256828
2001-06-15 0.0735959182096
2001-07-04 0.0738679388157
2001-07-16 0.0795556218312
2001-08-04 0.0794191141853
2001-08-22 0.0802172770282
2001-09-04 0.0810112630455
2001-09-22 0.0813549018946
2001-10-03 0.0810738164836
2001-10-09 0.0808587479936
2001-10-29 0.0797858362896
2001-11-15 0.0824474064558
2001-11-28 0.0819276342959
2001-12-10 0.0810310184604
2001-12-26 0.0807311028501
2002-01-14 0.0808111657454
2002-01-23 0.0843893396542
2002-02-02 0.084089808763
2002-02-12 0.0838528959971
2002-02-27 0.0830176296871
2002-03-18 0.082708099486
2002-03-28 0.0827407886231
2002-04-08 0.0844347191831
2002-04-18 0.0837167578204
2002-05-01 0.0839156833543
2002-05-13 0.0836788006133
2002-05-30 0.0833778427459
2002-06-13 0.083087867504
2003-03-04 0.0925728672412
2003-03-24 0.0921856215436
2003-04-10 0.0926112148638
2004-07-05 0.0992014871773
2006-10-01 0.0666756104105
2006-11-07 0.0976250149182
2006-12-01 0.0968787040695
2007-01-01 0.0965753559542
2007-02-01 0.0965195480137
2007-03-01 0.0967344186495
2007-04-01 0.0975424963575
2007-05-01 0.0973302053241
2007-06-06 0.0922222222222
2007-07-01 0.0916590284143
2007-08-01 0.0914415816922
2007-08-27 0.0866102538576
2007-09-01 0.0913741126131
2007-11-01 0.0907895754389
2008-01-01 0.090829846583
2008-01-15 0.0908015666809
2008-02-01 0.0907136215714
2008-02-15 0.0906170163351
2008-03-01 0.090581953258
2008-03-15 0.0904768347604
2008-04-01 0.0903947165148
2008-04-15 0.0903737740366
2008-05-01 0.090253754131
2008-05-12 0.0902398021294
2008-05-15 0.0902328277461
e
