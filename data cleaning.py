'''Python assignment
Data Cleaning
all 5 problems combined '''

import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']},dtype=int)
df['FlightNumber']=df['FlightNumber'].fillna(0)
print("The given Dataframe: \n",df)

# FILLING IN THE MISSING VALUE
# convert flight number into list
lis=df['FlightNumber'].values.tolist()
'''for i in range(0, len(lis)): 
    lis[i] = int(lis[i]) 
print(lis)'''
#fill in the missing value in the column
for i in range(1, len(lis)): 
    lis[i] = lis[i-1]+10
print(lis)
df['FlightNumber']=lis
print("The Dataframe after filling the missing data: \n", df)

# SPLITTING THE FROM_TO COLUMN AND STORING IN SEPERATE DATAFRAME
df2=pd.DataFrame(df.From_To.str.split("_",expand=True).values, columns=['From','To'])
print("The temporary Dataframe with From and To column :\n", df2)
#df_temp=pd.DataFrame(df['From_To'].to_list(),columns=['From','To'])
#df_temp=pd.DataFrame(df['To'].to_list(),columns=['To'])

#CAPITALIZE THE FIRST LETTER
df2.From=df2.From.str.capitalize()
df2.To=df2.To.str.capitalize()
print("The temporary Dataframe after Capitilization :\n", df2)

#DROPPING THE FROM_TO COLUMN AND COMBING THE TEMPORARY DATAFRAME WITH ORIGINAL
df=pd.concat([df,df2],axis=1,sort=False)
df=df.drop(['From_To'],axis=1)
print("The Dataframe after dropping From_To column and combining temporary Dataframe : \n", df)

#COPY THE RECENTDELAYS COLUMN AS SERIES
#df[['delay1','delay2','delay3']] = pd.DataFrame(df.RecentDelays.tolist(), index= df.index)
df3=df.RecentDelays.apply(pd.Series)
df3.columns=['delay_1','delay_2','delay_3']
df=pd.concat([df,df3],axis=1,sort=False)
df=df.drop(['RecentDelays'],axis=1)
print("The final Dataframe with seperated Delay columns \n", df)
