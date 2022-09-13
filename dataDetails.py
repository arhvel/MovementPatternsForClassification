print('Hello Victor')

import glob
import pandas as pd

sensorFolders =  sorted([i for i in glob.glob('*')])


collection = []
summation = 0
for folder in sensorFolders:
    name = folder+'/*'
    sensorFiles =  (glob.glob(name))
    
    for file in sensorFiles:  
        filename = file
        data = pd.read_csv(file)
        collection.append(len(data))
        summation += len(data)

average = summation/len(collection)
