import pandas as pd
exam_result = { "name":["ak","vr","kar","rah","mor"], "score":[23,22,50,34,57],"no_of_attempts":[3,1,2,4,2],"qualify":[False,False,True,False,True]}

label = {"inputs":["a","b","c","d","e"]}
df = pd.DataFrame(exam_result,index=label["inputs"])

# inputs
print("inputs=")
for key,value in label.items():
    print(value,end=" ")

# first 4 rows of the dataframe
print("\n")
print(df.head(4))

# print name nd qualify from dataframe
print("\n")
print("Name and qualify from the dataframe")
print(df[["name","qualify"]])

# number of scrore in between 25-30
print("\n")
print("Number of score in between 20- 35 and the sum of attempts by each students")
print("Index \t no_of_attempts")
print(df[(df['score']>=20)&(df['score']<35)]['no_of_attempts'])