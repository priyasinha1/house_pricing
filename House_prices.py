#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[12]:


df = pd.read_csv('house_train.csv')
test_df = pd.read_csv('house_test.csv')


# In[13]:


df.head()


# In[14]:


df.shape
df.isnull().sum()


# In[11]:


sns.heatmap(df.isnull(),yticklabels = False,cmap='viridis')


# In[15]:


test_df.isnull().sum()


# In[17]:


df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].mean())


# In[18]:


df.drop(['Alley'],axis = 1,inplace = True)


# In[19]:


df['BsmtCond'] = df['BsmtCond'].fillna(df['BsmtCond'].mode()[0])
df['BsmtQual'] = df['BsmtQual'].fillna(df['BsmtQual'].mode()[0])


# In[20]:


df['FireplaceQu'] = df['FireplaceQu'].fillna(df['FireplaceQu'].mode()[0])
df['GarageType'] = df['GarageType'].fillna(df['GarageType'].mode()[0])


# In[21]:


df.drop(['GarageYrBlt'],axis = 1, inplace = True)


# In[22]:


df['GarageFinish'] = df['GarageFinish'].fillna(df['GarageFinish'].mode()[0])
df['GarageQual'] = df['GarageQual'].fillna(df['GarageQual'].mode()[0])
df['GarageCond'] = df['GarageCond'].fillna(df['GarageCond'].mode()[0])


# In[23]:


df.drop(['PoolQC',"Fence",'MiscFeature'],axis=1,inplace = True)


# In[24]:


df.shape


# In[25]:


df.drop(["Id"],axis=1,inplace = True)


# In[26]:


df.isnull().sum()


# In[27]:


df['MasVnrType'] = df['MasVnrType'].fillna(df['MasVnrType'].mode()[0])
df['MasVnrArea'] = df['MasVnrArea'].fillna(df['MasVnrArea'].mode()[0])


# In[31]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='coolwarm')


# In[29]:


df['BsmtFinType2'] = df['BsmtFinType2'].fillna(df['BsmtFinType2'].mode()[0])


# In[30]:


df.dropna(inplace=True)


# In[32]:


df.shape


# In[33]:


df.head()


# In[36]:


columns=['MSZoning','Street','LotShape','LandContour','Utilities','LotConfig','LandSlope','Neighborhood','Condition2','BldgType','Condition1','HouseStyle','SaleType','SaleCondition','ExterCond','ExterQual','Foudation','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmlFinType2','RoofStyle','RoofMatl','Exterior1st','Exterior2nd','MasVnrType','Heating','HeatingQC','CentralAir','Electrical','KitchenQual','Functional','FireplaceQu','GarageType','GarageFinish','GarageQual','GarageCond','PavedDrive']


# In[37]:


len(columns)


# In[40]:


def category_multcols(multcolumns):
    df_final = final_df
    i = 0
    for fields in multcolumns:
        print(fields)
        df1 = pd.get_dummies(final_df[fields],drop_first=True)
        final_df.drop([fields],axis=1,inplace=True)
        
        if i==0:
            df_final=df1.copy()
        else:
            df_final = pd.concat([df_final,df1],axis=1)
        i=i+1
        
        df_final=pd.concat([final_df,df_final],asix=1)
        return df_final


# In[41]:


main_df=df.copy()


# In[43]:


test_df.loc[:,test_df.isnull().any()].head()




