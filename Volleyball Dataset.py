#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[4]:


df = pd.read_csv(r"C:\Users\Ashwin Kumar\Downloads\archive (1)\VNL2023.csv")
df.head()


# In[5]:


df.shape


# In[6]:


df.describe()


# In[7]:


df.isna().sum()


# In[8]:


df.duplicated().sum()


# In[9]:


## checking the corelation between the columns
numeric_cols = df.select_dtypes(include=['int','float']).columns
corr_matrix = df[numeric_cols].corr()


# In[10]:


corr_matrix


# In[11]:


## to check the co-relation matrix we can create a heatmap
plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',linewidths=5)
plt.title('corelation matric heatmap')
plt.show()


# In[12]:


position_counts = df['Position'].value_counts()


# In[13]:


position_counts


# In[14]:


plt.pie(position_counts,labels=position_counts.index,autopct='%1.1f%%',startangle=90)
plt.title('distribution of positions')
plt.show()


# In[17]:


# group by country and avg attack for each county
avg_attack_by_country=df.groupby('Country')['Attack'].mean()


# In[19]:


avg_attack_by_country.sort_values(ascending=False)


# In[20]:


avg_attack_by_country.sort_values(ascending=False).head(5).plot(kind = 'bar')
plt.title('average attack by country')
plt.xlabel('country')
plt.ylabel('avg attack')
plt.show()


# In[22]:


df.columns


# In[ ]:





# In[23]:


avg_block_by_country=df.groupby('Country')['Block'].mean()


# In[24]:


avg_block_by_country.sort_values(ascending=False)


# In[25]:


avg_block_by_country.sort_values(ascending=False).head(5).plot(kind = 'bar')
plt.title('average block by country')
plt.xlabel('country')
plt.ylabel('avg block')
plt.show()


# In[37]:


## grouping the data by age and calculate avg serve for each age group
avg_serve_by_age=df.groupby('Age')['Serve'].mean()


# In[40]:


avg_serve_by_age.sort_values(ascending=False).plot(kind='bar')
plt.title('avg serve by each age group')
plt.xlabel('age')
plt.ylabel('avg serve')
plt.show


# In[48]:


## grouping the data by country and positions each athletes play
df.groupby(['Country','Position'])['Attack'].max().reset_index().sort_values(ascending=False , by= 'Attack').tail(20)


# In[51]:


#grouping by country and total dig for each country
dig_by_country= df.groupby('Country')['Dig'].sum().sort_values(ascending= False)


# In[59]:


plt.scatter(df['Block'],df['Recieve'])
plt.title('Scatter plot : Block vs Receive')
plt.xlabel('Block')
plt.ylabel('Recieve')
plt.show()


# In[56]:


df.columns


# In[55]:


df.rename(columns={'Receive':'Recieve'},inplace=True)


# In[60]:


# box plot for distribution of serve
sns.boxplot(x=df['Serve'])
plt.title('Box Plot : Distribution of Serve Values')
plt.xlabel('Serve')
plt.show()


# In[61]:


plt.hist(df['Age'], bins=20,color='orange', edgecolor ='black')
plt.title('dist of age')
plt.xlabel('age')
plt.ylabel('freq')
plt.show()


# In[62]:


avg_attack_by_position = df.groupby('Position')['Attack'].mean()


# In[66]:


avg_attack_by_position.plot(kind = 'bar', color='black')
plt.title('avg attack by position')
plt.xlabel('position')
plt.ylabel('avg attack')
plt.show()


# In[68]:


serve_trend_by_age = df.groupby('Age')['Serve'].mean()
serve_trend_by_age.plot(kind='line', linestyle = '-', color = 'orange')
plt.title('serve trend over age group')
plt.xlabel('avg serve')
plt.ylabel('age')
plt.show


# In[74]:


total_attack_block_by_country = df.groupby('Country')[['Attack','Block']].sum()


# In[80]:


total_attack_block_by_country.sort_values(ascending=False,by='Attack').plot(kind='bar',stacked = True, colormap = 'viridis')
plt.title('total attack and block by country')
plt.xlabel('country')
plt.ylabel('total value')
plt.show


# In[84]:


total_attack_block_by_country.sort_values(ascending=False, by='Attack')


# In[ ]:




