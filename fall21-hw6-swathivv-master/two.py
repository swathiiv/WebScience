import pandas as pd

#read the files in pandas dataframe
file1= pd.read_csv("D1.csv")
file2 = pd.read_csv("D2.csv")
file3 = pd.read_csv("D3.csv")

def compareThisB(lowerCase,upperCase):
    #create an empty final dataframe 
    number = 0
    column_name = ["Domain"]
    final = pd.DataFrame(columns = column_name)
    for index, row in upperCase.iterrows():
        #find a match(es) and store as a dataframe
        #set Uppercases domain to lowercase so that it can propermatch
        temp = lowerCase[lowerCase['Domain'] == row['Domain'].lower()]
        #check if data frame is empty
        if(len(temp) == 0):
            pass
        else:
            final.at[number,"Domain"] = temp['Domain'].iloc[0]
            number +=1
    return final

"""
   Q2 Part a compare D1 and D2
"""
a_final= compareThisB(file1,file2)

"""
   Q2 Part b compare D2 and D3
"""
b_final = compareThisB(file2,file3)
"""
   Q2 Part c compare D1 and D3
"""
c_final = compareThisB(file1,file3)

"""
   Q2 Part d compare a_final  and D3
"""
d_final = compareThisB(a_final,file3)


#convert to csv files
a_final.to_csv("a_final.csv", index = False, header=True)
b_final.to_csv("b_final.csv", index = False, header=True)
c_final.to_csv("c_final.csv", index = False, header=True)
d_final.to_csv("d_final.csv", index = False, header=True)
