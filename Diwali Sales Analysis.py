#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[12]:


df = pd.read_csv(r'C:\Users\Harish Kate\Downloads\Diwali Sales Data.csv', encoding = 'unicode_escape')


# In[13]:


df.shape


# In[14]:


df.info


# In[16]:


df.head(10)


# In[17]:


df.info()


# In[21]:


df.drop(['Status', 'unnamed1'], axis=1, inplace= True)


# In[22]:


df.info()


# In[24]:


pd.isnull(df)


# In[25]:


pd.isnull(df).sum()


# In[26]:


df.shape


# In[29]:


df.dropna(inplace= True)
#drop NA values
#inplace = True (its used to save the command)


# In[30]:


df.shape


# In[31]:


df['Amount']= df['Amount'].astype('int')
#change data type


# In[32]:


df['Amount'].dtypes


# In[34]:


df.columns


# In[35]:


#chaneg column name
df.rename(columns={'Marital_Status':'Shaadi'})


# In[37]:


df.describe()
#describe() method returns description of the data in the dataframe (i.e. count, mean, std, etc)


# In[39]:


#use describe() for specific columsn
df[['Age', 'Orders', 'Amount']].describe()


# In[40]:


#Exploratory Data Analysis
#GENDER


# In[43]:


df.columns


# In[51]:


hk= sns.countplot(x = 'Gender',data = df)


# In[52]:


#female sales > Males


# In[57]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[69]:


sale_gender= df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x ='Gender', y= 'Amount', data= sale_gender)


# In[71]:


hk = sns.barplot(x ='Gender', y= 'Amount', data= sale_gender)

for bars in hk.containers:
    hk.bar_label(bars)


# In[61]:


#AGE


# In[62]:


df.columns


# In[64]:


hk= sns.countplot(x = 'Age Group',data = df,)


# In[66]:


hk= sns.countplot(x = 'Age Group',data = df,hue= 'Gender')


# In[67]:


hk= sns.countplot(x = 'Age Group',data = df,hue= 'Gender')

for bars in hk.containers:
    hk.bar_label(bars)


# In[72]:


#Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x= 'Age Group', y= 'Amount', data = sales_age)


# In[73]:


#state


# In[74]:


#total number of orders from top 10 states


# In[80]:


sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(data = sales_state, x= 'State', y= 'Orders')


# In[84]:


#total AMount from top 10 States

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,10)})
hk=sns.barplot(data = sales_state, x= 'State', y= 'Amount')

for bars in hk.containers:
    hk.bar_label(bars)


# In[85]:


#marital Status


# In[86]:


hk= sns.countplot(x = 'Marital_Status',data = df)

for bars in hk.containers:
    hk.bar_label(bars)


# In[87]:


sales_state = df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,10)})
hk=sns.barplot(data = sales_state, x= 'Marital_Status', y= 'Amount', hue= 'Gender')

for bars in hk.containers:
    hk.bar_label(bars)


# In[89]:


#*Occupation*


# In[90]:


sns.set(rc={'figure.figsize':(20,5)})
hk = sns.countplot(data =df, x ='Occupation')
for bars in hk.containers:
    hk.bar_label(bars)


# In[98]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x ='Occupation', y='Amount')


# In[99]:


df.columns


# In[100]:


#Product CAtegory


# In[104]:


sns.set(rc={'figure.figsize':(30,10)})
hk = sns.countplot(data =df, x ='Product_Category')
for bars in hk.containers:
    hk.bar_label(bars)


# In[109]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(30,10)})
sns.barplot(data =df, x ='Product_Category', y= 'Amount')


# In[114]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(30,10)})
sns.barplot(data =sales_state, x ='Product_ID', y= 'Orders')


# In[ ]:




