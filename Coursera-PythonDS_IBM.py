
# coding: utf-8

# #Python Data science 
# #Assignment 1: Create a dataframe that contains the GDP data and display using the method head() and take a screen shot.

# In[2]:


import pandas as pd


# In[9]:


#import the input file 
GDP_WORLD = pd.read_csv("C:/Users/sanjukta/Desktop/DS IN PYTHON/GDP.csv")


# In[11]:


#check first few rows of the dataframe
GDP_WORLD.head()


# In[7]:


#Assignment 2: Create a dataframe that contains the unemployment data. Display the first five rows of the dataframe using the method head() and take a screen shot.


# In[13]:


#Unemployement rate data of India from 2004-05 to 2007-08
unemployment_urban = pd.read_excel("C:/Users/sanjukta/Desktop/DS IN PYTHON/Coursera-PythonData science by IBM/datafile.xls")


# In[14]:


#check first few rows of the data
unemployment_urban.head()


# In[20]:


#Assignment 3 : Display a dataframe where unemployment was greater than 8.5% . Take a screenshot 
#Dataframe that has Unemployment rate > 8.5% for SCheduled Castes in Urban area
SC_unemployment= unemployment_urban[['Category of States','States','Scheduled Castes - 2004-05','Scheduled Castes - 2007-08']]


# In[29]:


SC_unemployment1=SC_unemployment[(SC_unemployment['Scheduled Castes - 2004-05'] > 8.5)  | (SC_unemployment['Scheduled Castes - 2007-08'] > 8.5)] 


# In[30]:


SC_unemployment1.head()


# In[ ]:


#Assigment 4 : Us the function make_dashboard to make a dashboard, then take a screen shot.


# In[43]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[46]:


plt.hist(SC_unemployment1['Scheduled Castes - 2007-08'])


# In[39]:


#upload dashboard


import plotly.plotly as py
py.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python')

