#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:04:47 2021

@author: adeyem01
"""

import glob
import pandas as pd
from itertools import chain

import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

hookers = pd.read_csv("all_hookersList.csv")
h_id = list(hookers['id'])

# Read all patterns from all fixtures player, and append the unique patterns to a placeholder
Analysed_h = []
Analysed_w = []
LCCpatterns = []
sensorFolders =  sorted([i for i in glob.glob('.../GameLevel_sResultMatrix_LCCspm_Mpatterns/*')])
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

# Jaccard Similarity Score Definition
def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(set(list1)) + len(set(list2))) - intersection
    return float(intersection)/ union

# Compute Jaccard Similarity
LCC_SMP = jaccard(LCCpatterns_unique, SMPpatterns_unique)
LCC_APR = jaccard(LCCpatterns_unique, APRpatterns_unique)
SMP_APR = jaccard(SMPpatterns_unique, APRpatterns_unique)

# Compute Jaccard Difference and collate results into csv
JaccardScores =[]
LCC__SMP = ('LCC_SMP',LCC_SMP, 1-LCC_SMP)
LCC__APR = ('LCC_APR',LCC_APR, 1-LCC_APR)
SMP__APR = ('SMP_APR',SMP_APR, 1- SMP_APR)

JaccardScores.append(LCC__SMP)
JaccardScores.append(LCC__APR)
JaccardScores.append(SMP__APR)

ResultFrame = pd.DataFrame(JaccardScores, columns = ['Method', 'Jaccard_Sim', 'Jaccard_Diff'])

#ResultFrame.to_csv('JaccardScoresforPatternsPerAlgo.csv', index = False)


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
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
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
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
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
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
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
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
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
plt.close()

plt.figure(figsize=(9,5))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
plt.close()

#BOTTOM 50
Overlap = list(set(SMPpatterns_wg_bot50).intersection(set(APRpatterns_wg_bot50)))