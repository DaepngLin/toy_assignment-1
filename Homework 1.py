#!/usr/bin/env python
# coding: utf-8

# # Task 1

# In[1]:


import pandas as pd #first we'll need module pandas to work with the dataframes
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


fname = '311_service_requests_2020.csv'
url = 'https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/6ff6a6fd-3141-4440-a880-6f60a37fe789/download/tmpxbo51van.csv'
# alternative url
url = 'https://raw.githubusercontent.com/CUSP2021PUI/Data/main/311_service_requests_2020.csv'


# In[3]:


boston311 = pd.read_csv(url) #upload the data


# In[4]:


boston311.head()#preview the data


# In[5]:


boston311.neighborhood.unique()


# In[6]:


len(boston311.neighborhood.unique())


# In[7]:


boston311['neighborhood'].value_counts()


# In[8]:


boston311[['neighborhood','case_enquiry_id']].groupby(by=['neighborhood']).count().plot.bar()


# # Task 2

# In[9]:


year=2015; boro='brooklyn'


# In[10]:


fname=str(year)+'_'+boro+'.xls'


# In[11]:


url = 'https://www1.nyc.gov/assets/finance/downloads/pdf/rolling_sales/annualized-sales/'+str(year)+                                                                                       '/'+fname
# alternative URL
url = 'https://github.com/CUSP2021PUI/Data/blob/main/RollingSale/'+fname+'?raw=true'


# In[12]:


re_sales = pd.read_excel(url)


# In[13]:


re_sales.head()


# In[14]:


import urllib
dataDir='' 
urllib.request.urlretrieve(url,dataDir+fname)


# In[15]:


re_sales = pd.read_excel(dataDir+fname,skiprows=4)


# In[16]:


re_sales.head()


# In[17]:


re_sales.columns


# In[18]:


a=re_sales[['ZIP CODE\n','SALE PRICE\n','LAND SQUARE FEET\n']].groupby(by=['ZIP CODE\n']).sum()


# In[19]:


a['price_per_square_feet']=a['SALE PRICE\n']/a['LAND SQUARE FEET\n']


# In[20]:


a.columns


# In[21]:


a.head()


# In[22]:


print(a)


# In[23]:


a=a.drop(a[a['LAND SQUARE FEET\n']==0].index)


# In[24]:


a.describe()


# In[25]:


a.plot.bar(y='price_per_square_feet')


# In[26]:


print(a)


# # Task3

# In[1]:


import geopandas as gpd
url = 'https://data.cityofnewyork.us/api/geospatial/2cav-chmn?method=export&format=GeoJSON'
# alternative URL
url = 'https://raw.githubusercontent.com/CUSP2021PUI/Data/main/Street%20Pavement%20Rating.geojson'
rating = gpd.read_file(url)


# In[2]:


rating.head() #lets preview the data


# In[3]:


rating.iloc[:,:-1].describe()


# In[4]:


rating['length'] = rating['length'].astype(int)
rating['length'].describe()


# In[5]:


rating['rating_word'].value_counts()


# In[6]:


rating.plot(column=None, figsize=(10,10)) 


# In[7]:


rating1=rating[['rating_word','geometry','length']]


# In[8]:


rating1_1=rating1[rating.notnull()]


# In[9]:


Poor=rating1_1.loc[(rating1_1['rating_word']=='POOR')]


# In[10]:


Poor.head()


# In[11]:


Poor.plot(column='rating_word',cmap='Spectral',figsize=(10,10),legend=True)


# # Task4(a)

# In[28]:


import pandas as pd #first we'll need module pandas to work with the dataframes
get_ipython().run_line_magic('matplotlib', 'inline')
url = 'https://raw.githubusercontent.com/nychealth/coronavirus-data/7953c97d1e58bbed9934ea04affb12ca74d9c0fb/data-by-modzcta.csv'
# alternative url
url = 'https://raw.githubusercontent.com/CUSP2021PUI/Data/main/COVID19.csv'
df = pd.read_csv(url)


# In[29]:


df.head()


# In[30]:


df.BOROUGH_GROUP.unique()


# In[31]:


df[['BOROUGH_GROUP','COVID_CASE_COUNT']].groupby(by=['BOROUGH_GROUP']).sum()


# In[32]:


df[['BOROUGH_GROUP','COVID_CASE_COUNT']].groupby(by=['BOROUGH_GROUP']).sum().plot.bar()


# # Task4(b)

# In[33]:


df['COVID_CASE_COUNT'].sum()


# In[34]:


a=df[['BOROUGH_GROUP','COVID_CASE_COUNT']].groupby(by=['BOROUGH_GROUP']).sum()


# In[44]:


a['Percentage']=a['COVID_CASE_COUNT']/223855


# In[47]:


b=a['Percentage'].map(lambda x:format(x,'.2%'))


# In[48]:


print(b)


# In[58]:


a.plot.bar(y='Percentage')


# # Task4c

# In[60]:


a=df[['BOROUGH_GROUP','COVID_CASE_COUNT','TOTAL_COVID_TESTS']].groupby(by=['BOROUGH_GROUP']).sum()


# In[63]:


a['Postive_case_percentage']=a['COVID_CASE_COUNT']/a['TOTAL_COVID_TESTS']


# In[64]:


b=a['Postive_case_percentage'].map(lambda x:format(x,'.2%'))


# In[65]:


print(b)


# In[66]:


a['Postive_case_percentage']=100*a['COVID_CASE_COUNT']/a['TOTAL_COVID_TESTS']#percentage value


# In[68]:


a.plot.bar(y='Postive_case_percentage')


# In[ ]:




