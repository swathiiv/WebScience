import pandas as pd
from twarc.client2 import Twarc2
import matplotlib.pyplot as plt
import itertools

def auth():#authorization 
    bearer_token="AAAAAAAAAAAAAAAAAAAAAJ2AUAEAAAAALRZWrij70cG9YMLEBV1l2uq7aPY%3Ddacuw3kcsTgmfyCnftWr8tM98XNOGof3lnxuXCh6W9c6Rlp0CJ"
    tw = Twarc2(bearer_token=bearer_token)
    return tw
def plot_data(df,fwfing):
    plt.rcParams['figure.figsize'] =40,25
    plt.rcParams['font.size'] = 17;
    plt.plot(df.USER,df.FRIENDCOUNT, label="FriendCount",marker='o')
    plt.grid(True)
    plt.xticks(rotation=90)
    plt.xlabel(xlabel = "friends", fontsize=20)
    plt.ylabel(ylabel= "no. of friends", fontsize=20)
    plt.legend(loc=6,fontsize=25);
    plt.gca().invert_xaxis()
    return plt.show()
def df_replacement(df):
    df = df.sort_values(by="FRIENDCOUNT")
    #create a list of new users
    newUser= []
    try:
        for x  in range(len(df)):
            c = str(x)
            newUser.append(c)
        # replace this new list to the column user in the dataframe
        df.USER = newUser
    except Exception as p:
        print(p)
    return df
def get_number_of_followers(id,i):
    #get user 
    user = auth().followers(id)
    try:
        if i == 0:
            fwers_flowing = user.followers_count
    except Exception as p:
        print(p)
    return user.screen_name,fwers_flowing
def getUserFollowers(screen_name):
   users = []
   followersC = []
    #followers
   
   p= auth().user_lookup(users=n,usernames=True)
   c =1
   for ps in p:
       #parse in 0 to get the followers count
       us, count = get_number_of_followers(ps,0)
       users.append(us)
       followersC.append(count)
       c=c +1
       if(c > 179):
           break;
   
   prod = pd.DataFrame(list(zip(users,followersC)))
   prod.columns = ["USER", "FRIENDCOUNT"]
   #sort and replace the names symbol fn
   prod = df_replacement(prod)
   return prod
screen_name = "iAchieveODU"
try:
   
   f = getUserFollowers(screen_name)
   #print the mean, std and median
   print("The mean is {}".format(f.FRIENDCOUNT.mean()))
   print("The std deviation is {}".format(f.FRIENDCOUNT.std()))
   print("The median is {}".format(f.FRIENDCOUNT.median()))
   #print as a csv file
   f.to_csv("followers.csv",index=False)
   #plot the graph
   plot_data(f,0)
