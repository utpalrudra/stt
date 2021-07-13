import os
from glob import glob
import pandas as pd

paths=glob("dataset/clips/*.wav")
#print(paths)

filename = []
filesize = []

#get the file size in bytes
for path in paths:
    f=open(path,"r")
    fileSize=os.path.getsize(path) 
    #print(fileSize)
    filesize.append(fileSize)
    string = path.rsplit('/')[-1]
    filename.append(string)
    

df = pd.DataFrame()

df['wav_filename'] = filename
df['wav_filesize'] = filesize

df.to_csv('/media/utpal/Software/dataset/clips/file.csv', index=False)