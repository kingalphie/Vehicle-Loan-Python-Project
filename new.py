import pandas as pd
#sample data
data = {
    'Name': ['Alice', 'John', 'Mark','Tobi','Kate'],
    'Math': [85, 78, 88, 92, 69],
    'English': [89, 56, 75,90, 81],
    'Science': [92, 76, 89, 83,65]
}
print(data)
#create a dataframe
df = pd.DataFrame(data)
print(df)
#data exploration
#display first 3 rows
print(df.head(3))
#check the structure
print(df.columns)
#dataset shape
print(df.shape)
#basic statistics
print(df.describe())
#data types
print(df.dtypes)
#average score per subject
print(df['Math'].mean())
print(df['English'].mean())
print(df[['Math','English','Science']]. mean())
#total score per subject
print(df[['Math','English','Science']]. sum())
#max and min score
print(df[['Math','English', 'Science']].max())
print(df[['Math','English', 'Science']].min())
#the person with the highest english score
most_english_score = df[df['English'] == df['English'].max()]
print('Person with the highest English Score:')
print(most_english_score)
#import matplotlib
import matplotlib.pyplot as plt
#visualize using bar chart
plt.bar(df['Name'],df['Math'],color = 'skyblue')
plt.title('Total scores per Student')
plt.xlabel('Student Name')
plt.ylabel('Total score')
plt.show()







#the person with the lowest english score
least_english_score = df[df['English'] == df['English'].min()]
print('Person with the highest Enlgish Score:')
print(least_english_score)
#total score
Total = df[['Math','English', 'Science']].sum()
print(Total)
#bar chart plot

import matplotlib.pyplot as plt

plt.bar(df['Name'],df['Math'],color = 'skyblue')
plt.title('Total scores per Student')
plt.xlabel('Student Name')
plt.ylabel('Total score')
plt.show()










