#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:04:47 2021
Modified on Mon Oct 24 13:13:01 2022

@author: adeyem01
"""

import glob
import pandas as pd
from itertools import chain

import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from collections import Counter
from itertools import chain

hookers = pd.read_csv("all_hookersList.csv")
h_id = list(hookers['id'])

# Read all patterns from all fixtures player, and append the unique patterns to a placeholder
Analysed_h = []
Analysed_w = []
LCCpatterns = []
sensorFolders =  sorted([i for i in glob.glob('/home/adeyem01/Documents/Study3/Game_PlayerLevel_patternbased/GameLevel_sResultMatrix_LCCspm_Mpatterns/*')])
sensorFoldersLCC = sensorFolders[3:]

for folder in sensorFoldersLCC:
    fname = folder+'/*'
    sensorFiles =  sorted(glob.glob(fname))
    
    for file in sensorFiles:
        ath_id = file[150:len(file)-4]
        d = pd.read_csv(file)
        if (ath_id in h_id):
            Analysed_h.append(d)
        else:
            Analysed_w.append(d)
        LCCpatterns.append(list(d['Sequences']))
        
LCCpatterns_unique = list(set(list(chain.from_iterable(LCCpatterns))))

PatternsFrequency_h = dict.fromkeys(LCCpatterns_unique,0)
for i in range(len(Analysed_h)):
    diction = dict(zip(Analysed_h[i]['Sequences'], Analysed_h[i]['AbsoluteSupport']))
    
    for key, value in diction.items():
        PatternsFrequency_h[key] +=value

PatternsFrequency_h_LCC = pd.DataFrame(PatternsFrequency_h.items(), columns = ['Sequences', 'AbsoluteSupport'] ) 
PatternsFrequency_h_LCC = PatternsFrequency_h_LCC.sort_values('AbsoluteSupport', ascending=False)
PatternsFrequency_h_LCC = PatternsFrequency_h_LCC[PatternsFrequency_h_LCC['AbsoluteSupport'] != 0 ]

PatternsFrequency_w = dict.fromkeys(LCCpatterns_unique,0)
for i in range(len(Analysed_w)):
    diction = dict(zip(Analysed_w[i]['Sequences'], Analysed_w[i]['AbsoluteSupport']))
    
    for key, value in diction.items():
        PatternsFrequency_w[key] +=value

PatternsFrequency_w_LCC = pd.DataFrame(PatternsFrequency_w.items(), columns = ['Sequences', 'AbsoluteSupport'] ) 
PatternsFrequency_w_LCC = PatternsFrequency_w_LCC.sort_values('AbsoluteSupport', ascending=False)
PatternsFrequency_w_LCC = PatternsFrequency_w_LCC[PatternsFrequency_w_LCC['AbsoluteSupport'] != 0 ]
#PatternsFrequencyDF.to_csv("patterns_LCC", index = False)

# SMP
Analysed_h = []
Analysed_w = []
SMPpatterns = []
sensorFolders =  sorted([i for i in glob.glob('/home/adeyem01/Documents/Study3/Game_PlayerLevel_patternbased/GameLevel_sResultMatrix_SMP_Mpatterns/*')])
sensorFoldersSMP = sensorFolders[3:]

for folder in sensorFoldersSMP:
    fname = folder+'/*'
    sensorFiles =  sorted(glob.glob(fname))
    
    for file in sensorFiles:
        ath_id = file[139:len(file)-4]
        d = pd.read_csv(file)
        if (ath_id in h_id):
            Analysed_h.append(d)
        else:
            Analysed_w.append(d)
        SMPpatterns.append(list(d['Sequences']))
SMPpatterns_unique = list(set(list(chain.from_iterable(SMPpatterns))))

PatternsFrequency_h = dict.fromkeys(SMPpatterns_unique,0)
for i in range(len(Analysed_h)):
    diction = dict(zip(Analysed_h[i]['Sequences'], Analysed_h[i]['AbsoluteSupport']))
    
    for key, value in diction.items():
        PatternsFrequency_h[key] +=value

PatternsFrequency_h_SMP = pd.DataFrame(PatternsFrequency_h.items(), columns = ['Sequences', 'AbsoluteSupport'] ) 
PatternsFrequency_h_SMP = PatternsFrequency_h_SMP.sort_values('AbsoluteSupport', ascending=False)
PatternsFrequency_h_SMP = PatternsFrequency_h_SMP[PatternsFrequency_h_SMP['AbsoluteSupport'] != 0 ]
#PatternsFrequencyDF.to_csv("patterns_LCC", index = False)

PatternsFrequency_w = dict.fromkeys(SMPpatterns_unique,0)
for i in range(len(Analysed_w)):
    diction = dict(zip(Analysed_w[i]['Sequences'], Analysed_w[i]['AbsoluteSupport']))
    
    for key, value in diction.items():
        PatternsFrequency_w[key] +=value

PatternsFrequency_w_SMP = pd.DataFrame(PatternsFrequency_w.items(), columns = ['Sequences', 'AbsoluteSupport'] ) 
PatternsFrequency_w_SMP = PatternsFrequency_w_SMP.sort_values('AbsoluteSupport', ascending=False)
PatternsFrequency_w_SMP = PatternsFrequency_w_SMP[PatternsFrequency_w_SMP['AbsoluteSupport'] != 0 ]

# Apriori Close
Analysed_h = []
Analysed_w = []
APRpatterns = []
sensorFolders =  sorted([i for i in glob.glob('/home/adeyem01/Documents/Study3/Game_PlayerLevel_patternbased/GameLevel_sResultMatrix_APR_Mpatterns/*')])
sensorFoldersAPR = sensorFolders[3:]

for folder in sensorFoldersAPR:
    fname = folder+'/*'
    sensorFiles =  sorted(glob.glob(fname))
    
    for file in sensorFiles:
        ath_id = file[139:len(file)-4]
        d = pd.read_csv(file)
        if (ath_id in h_id):
            Analysed_h.append(d)
        else:
            Analysed_w.append(d)
        APRpatterns.append(list(d['Sequences']))      
APRpatterns_unique = list(set(list(chain.from_iterable(APRpatterns))))

PatternsFrequency_h = dict.fromkeys(APRpatterns_unique,0)
for i in range(len(Analysed_h)):
    diction = dict(zip(Analysed_h[i]['Sequences'], Analysed_h[i]['AbsoluteSupport']))
    
    for key, value in diction.items():
        PatternsFrequency_h[key] +=value

PatternsFrequency_h_APR = pd.DataFrame(PatternsFrequency_h.items(), columns = ['Sequences', 'AbsoluteSupport'] ) 
PatternsFrequency_h_APR = PatternsFrequency_h_APR.sort_values('AbsoluteSupport', ascending=False)
PatternsFrequency_h_APR = PatternsFrequency_h_APR[PatternsFrequency_h_APR['AbsoluteSupport'] != 0 ]
#PatternsFrequencyDF.to_csv("patterns_LCC", index = False)

PatternsFrequency_w = dict.fromkeys(APRpatterns_unique,0)
for i in range(len(Analysed_w)):
    diction = dict(zip(Analysed_w[i]['Sequences'], Analysed_w[i]['AbsoluteSupport']))
    
    for key, value in diction.items():
        PatternsFrequency_w[key] +=value

PatternsFrequency_w_APR = pd.DataFrame(PatternsFrequency_w.items(), columns = ['Sequences', 'AbsoluteSupport'] ) 
PatternsFrequency_w_APR = PatternsFrequency_w_APR.sort_values('AbsoluteSupport', ascending=False)
PatternsFrequency_w_APR = PatternsFrequency_w_APR[PatternsFrequency_w_APR['AbsoluteSupport'] != 0 ]


def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(set(list1)) + len(set(list2))) - intersection
    return float(intersection)/ union

# Calculate Jaccard Similarity
LCC_SMP = jaccard(LCCpatterns_unique, SMPpatterns_unique)
LCC_APR = jaccard(LCCpatterns_unique, APRpatterns_unique)
SMP_APR = jaccard(SMPpatterns_unique, APRpatterns_unique)

# Calculate Jaccard Difference and collate results into csv
JaccardScores =[]
LCC__SMP = ('LCC_SMP',LCC_SMP, 1-LCC_SMP)
LCC__APR = ('LCC_APR',LCC_APR, 1-LCC_APR)
SMP__APR = ('SMP_APR',SMP_APR, 1- SMP_APR)

JaccardScores.append(LCC__SMP)
JaccardScores.append(LCC__APR)
JaccardScores.append(SMP__APR)

ResultFrame = pd.DataFrame(JaccardScores, columns = ['Method', 'Jaccard_Sim', 'Jaccard_Diff'])

ResultFrame.to_csv('JaccardScoresforPatternsPerAlgo.csv', index = False)

# Overlap pattern Framework_level

lcc_glbDF = pd.concat([PatternsFrequency_h_LCC,PatternsFrequency_w_LCC], axis=0).sort_values('AbsoluteSupport', ascending=False).reset_index().drop('index',axis=1)
PatternsFrequencyDF_lcc_ = dict.fromkeys(LCCpatterns_unique,0)
for i in range(len(lcc_glbDF)):
    diction = lcc_glbDF.iloc[[i]].set_index('Sequences')['AbsoluteSupport'].to_dict()
    
    for key, value in diction.items():
        PatternsFrequencyDF_lcc_[key] +=value
PatternsFrequencyDF_lcc = pd.DataFrame(PatternsFrequencyDF_lcc_.items(), columns = ['Sequences', 'AbsoluteSupport'] ) 
PatternsFrequencyDF_lcc = PatternsFrequencyDF_lcc.sort_values('AbsoluteSupport', ascending=False).reset_index().drop('index',axis=1)
PatternsFrequencyDF_lcc = PatternsFrequencyDF_lcc[PatternsFrequencyDF_lcc['AbsoluteSupport'] != 0 ]

lcc_glbDF_top50= list(PatternsFrequencyDF_lcc['Sequences'][:50])
lcc_glbDF_bot50 = list(PatternsFrequencyDF_lcc['Sequences'][len(PatternsFrequencyDF_lcc)-50:])


smp_glbDF = pd.concat([PatternsFrequency_h_SMP,PatternsFrequency_w_SMP], axis=0).sort_values('AbsoluteSupport', ascending=False)
PatternsFrequencyDF_smp_ = dict.fromkeys(SMPpatterns_unique,0)
for i in range(len(smp_glbDF)):
    diction = smp_glbDF.iloc[[i]].set_index('Sequences')['AbsoluteSupport'].to_dict()
    
    for key, value in diction.items():
        PatternsFrequencyDF_smp_[key] +=value
PatternsFrequencyDF_smp = pd.DataFrame(PatternsFrequencyDF_smp_.items(), columns = ['Sequences', 'AbsoluteSupport'] ) 
PatternsFrequencyDF_smp = PatternsFrequencyDF_smp.sort_values('AbsoluteSupport', ascending=False).reset_index().drop('index',axis=1)
PatternsFrequencyDF_smp = PatternsFrequencyDF_smp[PatternsFrequencyDF_smp['AbsoluteSupport'] != 0 ]

smp_glbDF_top50= list(PatternsFrequencyDF_smp['Sequences'][:50])
smp_glbDF_bot50 = list(PatternsFrequencyDF_smp['Sequences'][len(PatternsFrequencyDF_smp)-50:])


apr_glbDF = pd.concat([PatternsFrequency_h_APR,PatternsFrequency_w_APR], axis=0).sort_values('AbsoluteSupport', ascending=False)
PatternsFrequencyDF_apr_ = dict.fromkeys(APRpatterns_unique,0)
for i in range(len(apr_glbDF)):
    diction = apr_glbDF.iloc[[i]].set_index('Sequences')['AbsoluteSupport'].to_dict()
    
    for key, value in diction.items():
        PatternsFrequencyDF_apr_[key] +=value
PatternsFrequencyDF_apr = pd.DataFrame(PatternsFrequencyDF_apr_.items(), columns = ['Sequences', 'AbsoluteSupport'] ) 
PatternsFrequencyDF_apr = PatternsFrequencyDF_apr.sort_values('AbsoluteSupport', ascending=False).reset_index().drop('index',axis=1)
PatternsFrequencyDF_apr = PatternsFrequencyDF_apr[PatternsFrequencyDF_apr['AbsoluteSupport'] != 0 ]

apr_glbDF_top50= list(PatternsFrequencyDF_apr['Sequences'][:50])
apr_glbDF_bot50 = list(PatternsFrequencyDF_apr['Sequences'][len(PatternsFrequencyDF_apr)-50:])

#                   IDENTIFICATION  of OVERLAPPED pattern across FRAMEWORKS
#               LCC      vs.      SMP
ov_glb_lccsmp_top = list(set(lcc_glbDF_top50).intersection(set(smp_glbDF_top50)))
ov_glb_lccsmp_bot = list(set(lcc_glbDF_bot50).intersection(set(smp_glbDF_bot50)))

ov_glb_lccsmp_top_DF1 = PatternsFrequencyDF_lcc[PatternsFrequencyDF_lcc['Sequences' ].isin(ov_glb_lccsmp_top)]
ov_glb_lccsmp_top_DF2 = PatternsFrequencyDF_smp[PatternsFrequencyDF_smp['Sequences' ].isin(ov_glb_lccsmp_top)]
ov_glb_lccsmp_merged = ov_glb_lccsmp_top_DF1.copy().sort_values('Sequences', ascending = True).reset_index().drop('index', axis = 1)
ov_glb_lccsmp_merged['SMP_support'] = ov_glb_lccsmp_top_DF2.sort_values('Sequences', ascending = True).reset_index().drop('index', axis = 1)['AbsoluteSupport']
ov_glb_lccsmp_merged = ov_glb_lccsmp_merged.sort_values('AbsoluteSupport', ascending = False).reset_index().drop('index', axis = 1)
 
word_cloud_dict1= ov_glb_lccsmp_top_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= ov_glb_lccsmp_top_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
plt.close()

#               LCC      vs.      APR
ov_glb_lccapr_top = list(set(lcc_glbDF_top50).intersection(set(apr_glbDF_top50)))
ov_glb_lccapr_bot = list(set(lcc_glbDF_bot50).intersection(set(apr_glbDF_bot50)))

ov_glb_lccapr_top_DF1 = PatternsFrequencyDF_lcc[PatternsFrequencyDF_lcc['Sequences' ].isin(ov_glb_lccapr_top)]
ov_glb_lccapr_top_DF2 = PatternsFrequencyDF_apr[PatternsFrequencyDF_apr['Sequences' ].isin(ov_glb_lccapr_top)]
ov_glb_lccapr_merged = ov_glb_lccapr_top_DF1.copy().sort_values('Sequences', ascending = True).reset_index().drop('index', axis = 1)
ov_glb_lccapr_merged['APR_support'] = ov_glb_lccapr_top_DF2.sort_values('Sequences', ascending = True).reset_index().drop('index', axis = 1)['AbsoluteSupport']
ov_glb_lccapr_merged = ov_glb_lccapr_merged.sort_values('AbsoluteSupport', ascending = False).reset_index().drop('index', axis = 1)

#               SMP      vs.      APR
ov_glb_smpapr_top = list(set(smp_glbDF_top50).intersection(set(apr_glbDF_top50)))
ov_glb_smpapr_bot = list(set(smp_glbDF_bot50).intersection(set(apr_glbDF_bot50)))

ov_glb_smpapr_top_DF1 = PatternsFrequencyDF_smp[PatternsFrequencyDF_smp['Sequences' ].isin(ov_glb_smpapr_top)]
ov_glb_smpapr_top_DF2 = PatternsFrequencyDF_apr[PatternsFrequencyDF_apr['Sequences' ].isin(ov_glb_smpapr_top)]
ov_glb_smpapr_merged = ov_glb_smpapr_top_DF1.copy().sort_values('Sequences', ascending = True).reset_index().drop('index', axis = 1)
ov_glb_smpapr_merged['APR_support'] = ov_glb_smpapr_top_DF2.sort_values('Sequences', ascending = True).reset_index().drop('index', axis = 1)['AbsoluteSupport']
ov_glb_smpapr_merged = ov_glb_smpapr_merged.sort_values('AbsoluteSupport', ascending = False).reset_index().drop('index', axis = 1)



# Overlapping Patterns and Visualization
                                                        #Hookers
LCCpatterns_hk = list(PatternsFrequency_h_LCC['Sequences'])
LCCpatterns_hk_top50 = LCCpatterns_hk[:50]
LCCpatterns_hk_bot50 = LCCpatterns_hk[len(LCCpatterns_hk)-50:]

SMPpatterns_hk = list(PatternsFrequency_h_SMP['Sequences'])
SMPpatterns_hk_top50 = SMPpatterns_hk[:50]
SMPpatterns_hk_bot50 = SMPpatterns_hk[len(SMPpatterns_hk)-50:]

APRpatterns_hk = list(PatternsFrequency_h_APR['Sequences'])
APRpatterns_hk_top50 = APRpatterns_hk[:50]
APRpatterns_hk_bot50 = APRpatterns_hk[len(APRpatterns_hk)-50:]


#Visualization LCC vs. SMP
#TOP 50
Overlap = list(set(LCCpatterns_hk_top50).intersection(set(SMPpatterns_hk_top50)))
Overlap_DF1 = PatternsFrequency_h_LCC[PatternsFrequency_h_LCC['Sequences' ].isin(Overlap)]
Overlap_DF2 = PatternsFrequency_h_SMP[PatternsFrequency_h_SMP['Sequences' ].isin(Overlap)]

word_cloud_dict1= Overlap_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= Overlap_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

#BOTTOM 50
Overlap = list(set(LCCpatterns_hk_bot50).intersection(set(SMPpatterns_hk_bot50)))


#Visualization LCC vs. APR
#TOP 50
Overlap = list(set(LCCpatterns_hk_top50).intersection(set(APRpatterns_hk_top50)))
Overlap_DF1 = PatternsFrequency_h_LCC[PatternsFrequency_h_LCC['Sequences' ].isin(Overlap)]
Overlap_DF2 = PatternsFrequency_h_APR[PatternsFrequency_h_APR['Sequences' ].isin(Overlap)]

word_cloud_dict1= Overlap_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= Overlap_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

#BOTTOM 50
Overlap = list(set(LCCpatterns_hk_bot50).intersection(set(APRpatterns_hk_bot50)))


#Visualization SMP vs. APR
#TOP 50
Overlap = list(set(SMPpatterns_hk_top50).intersection(set(APRpatterns_hk_top50)))
Overlap_DF1 = PatternsFrequency_h_APR[PatternsFrequency_h_APR['Sequences' ].isin(Overlap)]
Overlap_DF2 = PatternsFrequency_h_SMP[PatternsFrequency_h_SMP['Sequences' ].isin(Overlap)]

word_cloud_dict1= Overlap_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= Overlap_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

#BOTTOM 50
Overlap = list(set(SMPpatterns_hk_bot50).intersection(set(APRpatterns_hk_bot50)))


                        #   Wingers
LCCpatterns_wg = list(PatternsFrequency_w_LCC['Sequences'])
LCCpatterns_wg_top50 = LCCpatterns_wg[:50]
LCCpatterns_wg_bot50 = LCCpatterns_wg[len(LCCpatterns_wg)-50:]

SMPpatterns_wg = list(PatternsFrequency_w_SMP['Sequences'])
SMPpatterns_wg_top50 = SMPpatterns_wg[:50]
SMPpatterns_wg_bot50 = SMPpatterns_wg[len(SMPpatterns_wg)-50:]

APRpatterns_wg = list(PatternsFrequency_w_APR['Sequences'])
APRpatterns_wg_top50 = APRpatterns_wg[:50]
APRpatterns_wg_bot50 = APRpatterns_wg[len(APRpatterns_wg)-50:]

#Visualization LCC vs. SMP
#TOP 50
Overlap = list(set(LCCpatterns_wg_top50).intersection(set(SMPpatterns_wg_top50)))
Overlap_DF1 = PatternsFrequency_w_LCC[PatternsFrequency_w_LCC['Sequences' ].isin(Overlap)]
Overlap_DF2 = PatternsFrequency_w_SMP[PatternsFrequency_w_SMP['Sequences' ].isin(Overlap)]

word_cloud_dict1= Overlap_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= Overlap_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

#BOTTOM 50
Overlap = list(set(LCCpatterns_wg_bot50).intersection(set(SMPpatterns_wg_bot50)))


#Visualization LCC vs. APR
#TOP 50
Overlap = list(set(LCCpatterns_wg_top50).intersection(set(APRpatterns_wg_top50)))
Overlap_DF1 = PatternsFrequency_w_LCC[PatternsFrequency_w_LCC['Sequences' ].isin(Overlap)]
Overlap_DF2 = PatternsFrequency_w_APR[PatternsFrequency_w_APR['Sequences' ].isin(Overlap)]

word_cloud_dict1= Overlap_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= Overlap_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

#BOTTOM 50
Overlap = list(set(LCCpatterns_wg_bot50).intersection(set(APRpatterns_wg_bot50)))

#Visualization SMP vs. APR
#TOP 50
Overlap = list(set(SMPpatterns_wg_top50).intersection(set(APRpatterns_wg_top50)))
Overlap_DF1 = PatternsFrequency_w_APR[PatternsFrequency_w_APR['Sequences' ].isin(Overlap)]
Overlap_DF2 = PatternsFrequency_w_SMP[PatternsFrequency_w_SMP['Sequences' ].isin(Overlap)]

word_cloud_dict1= Overlap_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= Overlap_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

#BOTTOM 50
Overlap = list(set(SMPpatterns_wg_bot50).intersection(set(APRpatterns_wg_bot50)))


# OVERLAP between positional group within ALGO
                    #   LCCSPM

Overlap = list(set(LCCpatterns_hk).intersection(set(LCCpatterns_wg)))
Overlap_DF1 = PatternsFrequency_h_LCC[PatternsFrequency_h_LCC['Sequences' ].isin(Overlap)]
Overlap_DF2 = PatternsFrequency_w_LCC[PatternsFrequency_w_LCC['Sequences' ].isin(Overlap)]

word_cloud_dict1= Overlap_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= Overlap_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

LCC_hk_only = [pat for pat in LCCpatterns_hk if pat not in LCCpatterns_wg]
LCC_wg_only = [pat for pat in LCCpatterns_wg if pat not in LCCpatterns_hk]

'eef' in 'eefee'


                    #   SMP

Overlap = list(set(SMPpatterns_hk).intersection(set(SMPpatterns_wg)))
Overlap_DF1 = PatternsFrequency_h_SMP[PatternsFrequency_h_SMP['Sequences' ].isin(Overlap)]
Overlap_DF2 = PatternsFrequency_w_SMP[PatternsFrequency_w_SMP['Sequences' ].isin(Overlap)]

word_cloud_dict1= Overlap_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= Overlap_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

SMP_hk_only = [pat for pat in SMPpatterns_hk if pat not in SMPpatterns_wg]
SMP_wg_only = [pat for pat in SMPpatterns_wg if pat not in SMPpatterns_hk]

             #   APR

Overlap = list(set(APRpatterns_hk).intersection(set(APRpatterns_wg)))
Overlap_DF1 = PatternsFrequency_h_APR[PatternsFrequency_h_APR['Sequences' ].isin(Overlap)]
Overlap_DF2 = PatternsFrequency_w_APR[PatternsFrequency_w_APR['Sequences' ].isin(Overlap)]

word_cloud_dict1= Overlap_DF1.set_index('Sequences')['AbsoluteSupport'].to_dict()
word_cloud_dict2= Overlap_DF2.set_index('Sequences')['AbsoluteSupport'].to_dict()
wordcloud1 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict1)
wordcloud2 = WordCloud(background_color = 'white', width = 2000, height = 1000).generate_from_frequencies(word_cloud_dict2)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#plt.savefig('FIFA_APR.png', bbox_inches='tight')
plt.close()

APR_hk_only = [pat for pat in APRpatterns_hk if pat not in APRpatterns_wg]
APR_wg_only = [pat for pat in APRpatterns_wg if pat not in APRpatterns_hk]
