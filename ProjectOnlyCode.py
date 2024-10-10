#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#1.>
data=pd.read_excel("Online Retail.xlsx")
print(data.head())


# In[3]:


data=pd.read_excel("Online Retail.xlsx")
print(data.tail())


# In[4]:


#2.>
print(data.count())


# In[5]:


#detecting missing values
print(data.isnull().sum())


# In[6]:


#Remove rows with missing values
data_clean=data.dropna()


# In[7]:


#
print(data.count())


# In[8]:


#drops columns with any missing values
data_clean=data.dropna(axis=1)


# In[9]:


print(data.count())


# In[10]:


#3.>
summary=data.describe()
print(summary)


# In[11]:


#Columns :-Quantity,UnitPrice,InnvoiceNo,CustomerID
#Calculate mean for Quantity column
Mean_Quantity=data["Quantity"].mean()
print(Mean_Quantity)
#calculate mean for unitprice column
Mean_UnitPrice=data["UnitPrice"].mean()
print(Mean_UnitPrice)


# In[12]:


#Calculate median for quantity
Median_Quantity=data["Quantity"].median()
print(Median_Quantity)
#Calculate median for unitprice
Median_UnitPrice=data["UnitPrice"].median()
print(Median_UnitPrice)


# In[13]:


#Calculate mode for quantity
Mode_Quantity=data["Quantity"].mode().iloc[0]
print(Mode_Quantity)
#Calculate mode for unit price
Mode_UnitPrice=data["UnitPrice"].mode().iloc[0]
print(Mode_UnitPrice)


# In[14]:


#Calculate range for Quantity columns
Range_Quantity=data["Quantity"].max()-data["Quantity"].min()
print(Range_Quantity)
#Calculate range for unit price
Range_UnitPrice=data["UnitPrice"].max()-data["UnitPrice"].min()
print(Range_UnitPrice)


# In[15]:


#calculate variance for quantity columns
Variance_Quantity=data["Quantity"].var()
print(Variance_Quantity)
#calculate variance for unit price
Variance_UnitPrice=data["UnitPrice"].var()
print(Variance_UnitPrice)


# In[16]:


#calculate standard deviation for quantity
Sd_Quantity=data["Quantity"].std()
print(Sd_Quantity)
#calculate sd for unit price
Sd_UnitPrice=data["UnitPrice"].std()
print(Sd_UnitPrice)


# In[17]:


#Calculate quartile for quantity columns
q1=data["Quantity"].quantile(0.25)
q2=data["Quantity"].quantile(0.50)
q3=data["Quantity"].quantile(0.75)

#calculating the interquartile range
iqr=q3-q1
print(iqr)


# In[18]:


#4.>
"""Histogram:

Quantity:To visualize the distrubution of the quantity of items ordered.
UnitPrice:To visualize the distribution of unit prices."""

#Histogram for quantities
plt.hist(data['Quantity'],bins=30,color='red')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.title('Distribution of quantity')
plt.show()

#Histogram for Unit Price
plt.hist(data['UnitPrice'],bins=50,color='green')
plt.xlabel('UnitPrice')
plt.ylabel('Frequency')
plt.title('Distrubution of unit price')
plt.show()


# In[19]:


"""Bar Plot:

Country:To visualize the number for transactions from different countries."""
#Bar plot for Country
country_counts=data['Country'].value_counts()
plt.figure(figsize=(10,6))
country_counts.plot(kind='bar',color='blue')
plt.xlabel('Coutry')
plt.ylabel('Number of transactions')
plt.title('Number of Transactions by country')
plt.xticks(rotation=45)
plt.show


# In[20]:


"""Scatter plot:

Quantity vs Unit Price: To visualize the relationship between the quantity and the unit price"""
plt.scatter(data["Quantity"],data["UnitPrice"],color='red',alpha=0.5)
plt.xlabel("Quantity")
plt.ylabel("UnitPrice")
plt.title("Quantity vs Unit Price")
plt.show()


# In[21]:


#5.>
#Extract month and day of the week
data['Month']=data['InvoiceDate'].dt.month
data['DayOfWeek']=data['InvoiceDate'].dt.dayofweek

#Calculate monthly sales
Monthly_Sales=data.groupby('Month')['Quantity'].sum()

#Identify the busiest month
Busiest_Month=Monthly_Sales.idxmax()

#Calculate sales by day of the week
Daily_Sales=data.groupby('DayOfWeek')['Quantity'].sum()

#Identify the busiest day of the week.lets take 0 as monday and 6 as sunday
Busiest_DayOfWeek=Daily_Sales.idxmax()

#print the result we found!
print("Busiest Month:",Busiest_Month)
print("Busiest Day of the week :",Busiest_DayOfWeek)


# In[22]:


#6.>
print(data.head())


# In[23]:


#Finding the top selling products
TSPs=data.groupby('Description')['Quantity'].sum().sort_values(ascending=False)
TSP=TSPs.idxmax()
#Print the top selling products
print("Top selling products :")
print(TSPs)
print("Top selling product :")
print(TSP)

#Find the top selling countries
TSC=data.groupby('Description')['Country'].sum().sort_values(ascending=False)
#Print the top selling countries
print("Top selling countries :")
print(TSC.head(5))


# In[24]:


#7.>

#create box plots for quantity and unitprice
plt.figure(figsize=(12,6))
sns.boxplot(data['Quantity'])
plt.title('Box plot for quantity')
plt.show()

plt.figure(figsize=(12,6))
sns.boxplot(data['UnitPrice'])
plt.title('Box plot for Unit Price')
plt.show


# In[25]:


#Calculate the IQR for the quantity
Q1=data['Quantity'].quantile(0.25)
Q3=data['Quantity'].quantile(0.75)
IQR=Q3-Q1

#Define the lower and upper bounds to identify outliers for quantity
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

#Identify outliers in quantity
OQ=data[(data['Quantity']<lower_bound) | (data['Quantity']>upper_bound)]

#Calculate the IQR for unit price
Q1=data['UnitPrice'].quantile(0.25)
Q3=data['UnitPrice'].quantile(0.75)
IQR=Q3-Q1

#Define the lower and upper bounds to identify the outliers of unit price
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

#Identify outliers in unitprice
OUP=data[(data['UnitPrice']<lower_bound) | (data['UnitPrice']>upper_bound)]

#print the outliers
print(f"Outliers in Quantity : {OQ}")
print(f"Outliers in UnitPrice : {OUP}")


# In[26]:


#8.>
print(">>>Conclusion<<<")
print("Using Python for Exploratory data analysis makes easy to find mean,median and mode also with the help of pandas library..\nIt becomes very easy to visualize the data in different types of graphs such as histograms,scatterplots in bar plots")
print("Standard deviation and variations can also be performed as pandas libraray has enriched with built in functions for data analysis")
print(">>>Summary<<<")
print("As i have followed the task gien as per it is :\nFirstly we have checked for any missing values and removed the missing values.\nBy analyzing the sales trends over time we have come to know about busiest month and days of the week which was in months -November and in Days of the weekk it was 3-Wednesday")


# In[ ]:




