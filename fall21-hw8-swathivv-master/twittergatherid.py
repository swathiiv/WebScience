#!/usr/local/bin/python3
from twarc import Twarc2, expansions
from tweetparser import setup_api, user_stat
import pandas as pd
import numpy as np
def  twitter_account(types,api= setup_api("/config") ):
    
    #Get twitter friends screen_name of the parse account, as one arrayList
    public_tweets = twarc.user_lookup(api.friends_ids, id = types)
    count= 1
    resultList =[] # store the final result of screen names
    for user in public_tweets.pages():
        #print(user)
        #print(user.dtypes())
        #Transverse the list of followers ids
        for i in user:
            #check if requirement is met
            if(user_stat(api,i) ==True):
                if( i not in resultList):   
                    #instead of the user id get the user name
                    user_sc = api.get_user(i)
                    print("{}:{}".format(count,user_sc.screen_name))
                    resultList.append(user_sc.screen_name)
                    count += 1                    
            #Get maximum 30 file accounts screen_names
            if(count >= 30):
                break
    print(resultList)

    #build text file and save file in q1 directory
    filename =  'one/' + types + '.txt'
    with open(filename, 'w') as filehandle:
        for listitem in resultList:
            filehandle.write('%s\n' % listitem)
    return resultList
"""
Tech= @WIRED
Sport= @WNBA
politics = @POTUS45
music = @future_of_music



"""
#Get all screen_names with that fulfils 10,000 followers and have 5000 tweets and verified
twitter_account("WIRED")
twitter_account("WNBA")
twitter_account("POTUS45")
twitter_account("future_of_music")


"""
Bring all result from the files in to One text file 
accounts.txt
"""
#get the list of the created files
column_name= ["User_screen_names"]
final = pd.DataFrame(columns= column_name)
fileList = ["one/WIRED.txt","one/WNBA.txt","one/POTUS45.txt","one/future_of_music.txt"]
df = pd.DataFrame()


for t in fileList:
    frame = pd.read_csv(t,header=None)
    frame.columns = column_name
    for ind in frame.index:
        final.loc[len(final)] =[frame['User_screen_names'][ind]]
        

# dropping duplicate values
final.User_screen_names.drop_duplicates(inplace=True)  

#confirm that there are all unique values 
print(final.User_screen_names.nunique())

# Number of rows to drop
n = 14
  
# Dropping last n rows using drop
final.drop(final.tail(n).index,
        inplace = True)
#print(final.User_screen_names.nunique())
numpy_array = final.to_numpy()
#print as a text file 
np.savetxt(r'accounts.txt', numpy_array,fmt="%s")
