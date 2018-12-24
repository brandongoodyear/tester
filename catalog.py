# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:44:36 2018

@author: Brandon Goodyear
"""

import pandas as pd

mnames=['Movies','TV','Books']
catalog=pd.read_excel('catalog2.xlsx','Sheet1',name=mnames)

movies=catalog['Movies']
movies=movies.str.lower()
movies=movies.sort_values()
a=[]
for i in movies:
    a.append(i)
    
cat1=pd.DataFrame(movies,columns=['Movies'])

tv=catalog['TV']
tv=tv.dropna()
tv=tv.str.lower()
tv=tv.sort_values()
cat2=pd.DataFrame(tv,columns=['TV'])
b=[]

for j in tv:
    b.append(j)
        
books=catalog['Books']
books=books.dropna()
books=books.str.lower()
books=books.sort_values()
c=[]
for k in books:
    c.append(k)

catpd=pd.DataFrame({'movies':movies, 'tv':tv, 'books':books})

catpd=catpd.fillna('')
#why is this df not taking in my values for movies,tv,and books? it only reads the xl

catfill=catalog.fillna('')

catfill=catfill.sort_index(by=['Movies'])
#so i can easily sort by movies but i want to sort each column
#sort_values(by=['abbrev'])
cat12=cat1.join(cat2,how='outer',sort=False)
cat123=pd.concat([cat1,cat2],join='outer',sort=False)

cas=pd.DataFrame({'Movies':a,
                 'TV':b,
                 'Books':c})