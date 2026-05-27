import pandas as pd
#create a sample data
data = {
    'Name': ['Alice', 'John', 'Mark', 'Tobi', 'Kate'],
    'Math': [85, 78, 88, 92, 69],
    'English': [89, 57, 75, 90, 81],
    'Science': [ 92, 72, 89, 83, 65]
}
print(data)
#create a DataFrame
df = pd.DataFrame(data)
print(df)

#data exploration
#display the first three rows
print(df.head(3))
#check the data structure
print(df.columns)
#dataset shape
print(df.shape)
#perform a basic statistics on the dataset
print(df.describe())
#data types
print(df.dtypes)
#perfom basic arithmetics
# average score per subject
print(df['Math'].mean())
print(df[['Math', 'English','Science']].mean())
#sum of each subject
print(df[['Math', 'English','Science']].sum())
# minimum and maximum score for each subject
# the peron with the highest score in english
most_englsih_score = df[df['English']==df['English'].max()]
print('Person with the highest English score')
print(most_englsih_score)
# the peron with the highest score in Math
import matplotlib.pyplot as plt
#visualize using bar chart
plt.bar(df['Name'], df['Math'], color='skyblue')
plt.title('Total score per student')
plt.xlabel('Student Name')
plt.ylabel('Total Score')
plt.show()
