#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Morph.csv")
sb.set_style('darkgrid')
df = dfM.melt(id_vars=['profile'], 
              value_vars=['plate_phill', 'plate_pacif', 'plate_maria', 'plate_carol'],
              var_name='Plates', value_name='Mean')
#print(df.head)
sb.stripplot(x='Plates', y='Mean', hue = 'profile', palette='PRGn', data=df, jitter=True)
plt.title('Strip plots for the mean depth values: Mariana Trench bathymetry', fontsize=10, fontfamily='serif')
plt.legend(bbox_to_anchor=(1.14, .8), loc=1, borderaxespad=-4., ncol=2, 
           markerscale=.5, fancybox=True, shadow=True, mode='expand', title='Bathymetric \nProfiles:',
          title_fontsize=8, labelspacing=.4);
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.80)
plt.show()


# In[ ]:




