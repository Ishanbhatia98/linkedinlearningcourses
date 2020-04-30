import pandas as pd
from numpy import nan

def merge_csv(filenames, outputfile):
    #concatening files
    combined = pd.concat([pd.read_csv(f) for f in filenames],sort=True)
    
    #replacing NaN with empty string
    combined = combined.replace(nan,'', regex=True)
    
    #saving to output file
    combined.to_csv(outputfile, index=False, encoding='utf-8-sig')
    print(f'The csv\'s have been merged to {outputfile}')

n = int(input('Enter number of files to be merged: '))
filenames=[]

print('Enter path to files:')

for _ in range(n):
    filenames.append(input())

outputfile = input('Enter name of the output file: ')

merge_csv(filenames, outputfile)

