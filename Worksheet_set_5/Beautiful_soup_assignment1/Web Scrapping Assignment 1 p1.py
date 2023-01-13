#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# 1. Write a python program to display all the header tags from wikipedia.org

# In[3]:


#scrapping source code
page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[4]:


#contents of the page 

soup = BeautifulSoup(page.content)
soup


# In[5]:


#Now scrapping all the header tags 

all_headlines = []

for i in soup.find_all('span',class_='mw-headline'):
    all_headlines.append(i.text)
    
all_headlines


# 4. Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) 
# from https://presidentofindia.nic.in/former-presidents.htm

# In[6]:


page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[7]:


soup = BeautifulSoup(page.content)
soup


# In[8]:


#scrap data 

president = soup.find_all('div',class_='presidentListing')
president


# In[9]:


#parse data

name = []
for nam in president:
    name.append(nam.get_text())


# In[10]:


name


# In[11]:


name_list=[]
term_list=[]
for data in president:
    name = data.find("h3").text.strip()
    name_list.append(name.split('(')[0][:-1])
    term = data.find("p").text.strip()
    term_list.append(term.split(':')[1][1:])


# In[12]:


import pandas as pd
pd.DataFrame({'Name':name_list,'Tenure':term_list})


# In[ ]:





# 2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.

# In[4]:


import pandas as pd 
import requests
from bs4 import BeautifulSoup


# In[5]:


page = requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page


# In[6]:


soup = BeautifulSoup(page.content)
soup


# In[7]:


movie_name = []
rating = []
year = []


# In[8]:


movie_data = soup.findAll('div',class_='undefined LatestNews-isHomePage LatestNews-isIntlHomepage')
movie_data


# In[18]:


for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)
    
for store in movie_data:
    rate = store.find('div',class_='inline-block ratings-imdb-rating').text.replace('\n','')
    rating.append(rate)
    
for store in movie_data:
    release = store.h3.find('span',class_='lister-item-year text-muted unbold').text.replace('(','').replace(')','')
    year.append(release)


# In[19]:


df = pd.DataFrame({'Movie Name':movie_name,'Year Of Release':year,'Ratings':rating})
df


# In[ ]:





# 3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame

# In[20]:


page = requests.get('https://www.imdb.com/list/ls009997493/')
page


# In[21]:


soup = BeautifulSoup(page.content)
soup


# In[22]:


movie_data = soup.findAll('div',class_='lister-item mode-detail')
movie_data


# In[23]:


movie_name= []
year= []
rating = []


# In[24]:


for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)
    
for store in movie_data:
    release = store.find('span',class_='lister-item-year text-muted unbold').text.replace('(','').replace(')','')
    year.append(release)
    
for store in movie_data:
    rate = store.find('div',class_='ipl-rating-star small').text.replace('\n','')
    rating.append(rate)


# In[26]:


df = pd.DataFrame({'Movie Name':movie_name,'Year Of Release':year,'Ratings':rating})
df


# In[ ]:




