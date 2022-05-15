import pandas as pd
import numpy as np
#read the files in pandas dataframe
file1= pd.read_csv("D1.csv")
file2 = pd.read_csv("D2.csv")

#sort them in order
file1 = file1.sort_values(by='# Citations in our Alternative Narrative Tweets',ascending=False)
file2 = file2.sort_values(by='Tweet count', ascending=False)

search = file1.copy()

#get only 10 items
file1 = file1.head(10)
file2 = file2.head(10)


#drop unwanted columns
file1.drop(['Primary Orientation (Determined through Content Analysis)', 'How Cited in Alternative Narrative of Shooting Events'],axis= 1,inplace=True)
file2.drop(['URL count'],axis =1, inplace=True)


#rename columns
file1.rename(columns={"# Citations in our Alternative Narrative Tweets":"Tweets","Media Type (Determined through Content Analysis)":"Website Type"},inplace=True)
file2.rename(columns={"Tweet count":"Tweet"},inplace=True)

#swap order for first d1
columns_swap = ["Domain","Tweets","Website Type"]
file1 = file1.reindex(columns=columns_swap)



#add new columns to the data with NAN values
file1['status']= np.nan
file2['Website Type']= np.nan
file2['status']= np.nan


#change column types to string
file2['Website Type'] = file2['Website Type'].astype(str)
file2['status'] = file2['status'].astype(str)

numCount = 0
temp =""
 #Match domains in top 10 D2 dataframe with D1 to obtain Website Media Type
for index, row in file2.iterrows():
    #find a match(es) and store as a dataframe
    temp = search[search['Domain'].str.contains(row['Domain'])]
    #check if data frame is empty
    if(len(temp) == 0):
        #assign NaN value
        final = np.nan
    else:
        #assigne Media Type to final value
        final = temp['Media Type (Determined through Content Analysis)'].iloc[0]
    #insert into file2 dataframe
    file2.at[index,"Website Type"] = final

file1.to_csv("D1_new.csv", index = False, header=True)
file2.to_csv("D2_new.csv", index = False, header=True)


