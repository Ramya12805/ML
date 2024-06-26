import pandas as pd
import seaborn as sns

data=pd.read_csv('top-5000-youtube-channels.csv')

# 1. Display All Rows Except the Last 5 rows Using Head Method
data.head(-5)

# 2. Display All Rows Except the First 5 Rows Using Tail Method
data.tail(-5)

# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
data.shape()
print("Number of rows ",data.shape[0])
print("Number of columns ",data.shape[1])

# 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
data.info()

# 5. Get Overall Statistics About The Dataframe
pd.options.display.float_format='{:.2f}'.format
data.describe()
data.describe(include='all')

# 6. Data Cleaning  (Replace '--'  to NaN)
import numpy as np
data.replace('--',np.nan,regex=True)

# 7. Check Null Values In The Dataset
data.isnull()
sns.heatmap(data.isnull())
data.isnull().sum()
per_missing=data.isnull().sum()*100/len(data)

data.dropna(axis=0,inplace=True) # dropping rows which contain missing values , for column axizs=1
sns.heatmap(data.isnull())

# 8. Data Cleaning [ Rank Column ]
data['Rank']=data['Rank'].str[0:-2] # removed "st,th,rd" from the end of the ranks
data['Rank']=data['Rank'].str.replace(',','').astype('int')  #replace comma with null space and converting the rank into integer
data.dtypes #check whether the rank column got chnaged into integer  

# 9. Data Cleaning [ Video Uploads & Subscribers ]
data['Video Uploads']= data['Video Uploads'].astype('int')
data['Subscribers']=data['Subscribers'].astype('int')
data.dtypes

# 10. Data Cleaning [ Grade Column ]
data['Grade'].unique()
data['Grade']=data['Grade'].map({'A++ ':5,'A+ ':4,'A ':3,'A- ':2,'B+ ':1})
data.dtypes

# 11. Find Average Views For Each Channel
data['Video views'] = pd.to_numeric(data['Video views'], errors='coerce')
data['Video Uploads'] = pd.to_numeric(data['Video Uploads'], errors='coerce')
data['Avg_views']=data['Video views']/data['Video Uploads']
data.head() 

# 12. Find Out Top Five Channels With Maximum Number of Video Uploads
data.sort_values(by='Video Uploads',ascending=False) #descending order
data.head()
#or
data.sort_values(by='Video Uploads',ascending=False).head()
#or
data.sort_values(by='Video Uploads')
data.tail()
# 13. Find Correlation Matrix
data.corr()

# 14.  Which Grade Has A Maximum Number of Video Uploads?
sns.barplot(x='Grade',y='Video Uploads',data=data)

# 15.Which Grade Has The Highest Average Views?
sns.barplot(x='Grade',y='Avg_views',data=data)

# 16.  Which Grade Has The Highest Number of Subscribers? 
sns.barplot(x='Grade',y='Subscribers',data=data)

# 17. Which Grade Has The Highest Video Views? 
sns.barplot(x='Grade',y='Video views',data=data)
