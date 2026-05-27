#import libraries
import pandas as pd
#import dataset
df = pd.read_csv(r'C:\Users\user\Desktop\credit_data.csv')
print(df)

#to desplay info of the dataset
df.info()
# change columns names to lowercase
def change_columm_name(col):
    return col.lower()
#change headers to lowercase
df.columns = [col.lower() for col in df.columns]
# to renamecolumns =  column headers
df = df.rename(columns={
    "age": "age",
    "gender": "gender",
    "income": "income",
    "credit score": "credit_score",
    "credit history length": "credit_history_length",
    "number of existing loans": "number_existing_loans",
    "loan amount": "loan_amount",
    "loan tenure": "loan_tenure",
    "existing customer": "existing_customer",
    "state": "state",
    "city": "city",
    "ltv ratio": "ltv_ratio",
    "employment profile": "employment_profile",
    "profile score": "profile_score",
    "occupation": "occupation"
})
print(df.columns)
# to find null values
null_values = df.isna().sum()
print(null_values)
# to replace null values
df['occupation'] = df['occupation'].fillna('Unknown')
# to print range
print(df[7860:7870])
#to find duplicates
duplicate = df.duplicated()
print(duplicate)
#to remove duplicates
df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)
# to view the dataset
df.describe()
# to do sum basic arithmetics/ analysis such as sum,average,mean,max and min
age_sum =  df['age'].sum()
print(age_sum)
#using graphs to visualized
import matplotlib.pyplot as plt
sum_value = df[['age', 'income']].sum()
print(sum_value)
plt.bar(sum_value.index, sum_value.values, color='blue')
plt.xlabel('columns')
plt.ylabel('sum')
plt.title('sum of each column')
plt.show()







