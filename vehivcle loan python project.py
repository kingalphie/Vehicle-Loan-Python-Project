
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model  import LogisticRegression
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

#import dataset
df1 = pd.read_csv(r'C:\Users\user\Desktop\credit_data.csv')
print(df1)
df1.info()
# Make a copy of the original dataframe
df1 = df1.copy()
#Data Cleaning
# change columns names to lowercase
def change_column_name(col):
    return col.lower()
header = []
for col in df1.columns:
    new_header = header.append(col.lower())
df1.columns = header
print(df1.head())
# Rename selected column names
df1 = df1.rename(columns={
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
print(df1.columns)
#Data Exploration
# to find null values
null_values = df1.isna().sum()
print(null_values)
# Get the percentage of null values in the columns
# Because of the small size of the dataset
# I will fill the missing values with mean or the mode for string data type

sum_null = df1.isnull().sum()
percentage_null = round(sum_null / len(df1) * 100, 2)
print(percentage_null)
# to replace null value
df1['occupation'] = df1['occupation'].fillna('Unknown')
# to print range
print(df1[7860:7870])
#to find duplicates
duplicate = df1.duplicated()
print(duplicate)
#to remove duplicates
df1_no_duplicates = df1.drop_duplicates()
print(df1_no_duplicates)
# to view the dataset
df1.describe()
print(df1.dtypes)
#Correcting the dataframe to lower case before mapping #
# Convert all values in the 'gender' column to lowercase
df1['gender'] = df1['gender'].str.lower()

# Define the mapping dictionary
gender_mapping = {"male": 1, "female": 0}

# Apply the mapping
df1['gender'] = df1['gender'].map(gender_mapping)

print("\nDataFrame after mapping 'gender':\n", df1)
# Convert all values in the 'existing_customer' column to lowercase
df1['existing_customer'] = df1['existing_customer'].str.lower()

# Display the updated DataFrame
print(df1)
# Define the mapping dictionary
existing_customer_mapping = {"yes": 1, "no": 0}

# Apply the mapping
df1['existing_customer'] = df1['existing_customer'].map(existing_customer_mapping)

print("\nDataFrame after mapping 'existing_customer':\n", df1)
df1.head()
# Dropping specific columns
df1.drop(columns=['state', 'city', 'employment_profile', 'occupation'], inplace=True)
df1.head()
# Checking for null values
df1.isna().sum()
# Calculate the median for the specified columns
median_values = {
    'gender': df1['gender'].median()}
# Fill NaN values in the specified columns with their median
df1.fillna(median_values, inplace=True)

# so we might consider loan_amount as a feature that will determine loan eligibility
df1.corr()["loan_amount"].sort_values(ascending= False)

# the dataframe.describe has indicated that there might be extreme values in those columns,
# we can still explore this further
#this used to see the distribution1
numerical_cols = df1.select_dtypes(include=['int64','float']).columns
df1[numerical_cols].hist(figsize=(12, 8))
plt.tight_layout()
plt.show

skewed_cols = ["loan_amount ", "income", "age ", "credit_score",
               "number_existing_loans", "profile_score", "existing_customer", "loan_tenure"]
sns.heatmap(data=df1.corr(), cmap="viridis", annot=True);

# Checking for outliers in the dataset (ALWAYS USe this code to resolve ur outlier issues)
def outliers_func():
    outliers_cols = []

    for col in df1.select_dtypes("int"):
        q1 = df1[col].quantile(.25)
        q3 = df1[col].quantile(.75)
        iqr = q3 - q1
        lower_out = (df1[col] < (q1 - (1.5 * iqr))).sum()
        upper_out = (df1[col] > (q3 + (1.5 * iqr))).sum()

        if lower_out > 0 or upper_out > 0:
            outliers_cols.append(col)

    return outliers_cols
# calling the outliers function
outlier_columns = outliers_func()
# Visualizing the boxplot for the columns with outliers

plt.figure(figsize=(16,12))
for index, col in enumerate(outlier_columns):
    plt.subplot(2,5, index+1)
    sns.boxplot(df1[col])
plt.tight_layout()
plt.show()
# to see the final outputsc
df1.duplicated()
df1.head()
df1.info()
df1.profile_score
df1.head()

