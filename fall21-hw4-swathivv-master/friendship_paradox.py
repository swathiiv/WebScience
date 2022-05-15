import matplotlib.pyplot as plt
import pandas as pd
f = "HW4-friend-count.csv"
df = pd.read_csv(f,index_col=False, encoding='utf-8')
#remove extra spaces from columns
df.columns =[col.strip() for col in df.columns]
df = df.sort_values(by="FRIENDCOUNT")

#create a list of new users
newuser= []
for x  in range(98):
    c =  str(x)
    newuser.append(c)
# replace this new list to the column user in the df
df.USER = newuser
print('The mean is',df.FRIENDCOUNT.mean())
print('The std deviation is',df.FRIENDCOUNT.std())
print('The median is',df.FRIENDCOUNT.median())
#plot the values
plt.rcParams['figure.figsize'] =20,40
plt.rcParams['font.size'] = 12;
plt.plot(df.USER,df.FRIENDCOUNT,marker='o')
plt.grid(True)
plt.xlabel(xlabel = "friends", fontsize=20)
plt.ylabel(ylabel= "no. of friends", fontsize=20)
plt.legend(loc=6,fontsize=25);
plt.gca().invert_xaxis()
plt.show()
