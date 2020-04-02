import os
import pandas as pd

df = pd.DataFrame()
for path, _, files in os.walk('/home/wang/Projects'):
    # add a new record
    row = pd.DataFrame( [[ filename , path ] for filename in files ] )
    df = pd.concat( [ df, row ] , ignore_index = True )

print( df.describe() )