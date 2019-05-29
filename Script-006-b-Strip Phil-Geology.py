#!/usr/bin/env python
# coding: utf-8

# In[24]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-GeomorphPhil.csv")
sb.set_style('darkgrid')

df = dfM.melt(id_vars=['profile'], 
              value_vars=['geol_c', 'geol_p', 'geol_vb', 'geol_a', 'geol_smi', 'geol_pb', 'geol_m'],
              var_name='Geology', value_name='Nr. of observation points')
#print(df.head)
sb.stripplot(x='Geology', y='Nr. of observation points', hue = 'profile', palette='tab20b', data=df, jitter=True)
plt.title('Geology and lithology across the Philippine archipelago: \na comparative strip plot for samples distribution', fontsize=10, fontfamily='serif')
plt.legend(title='Profiles', title_fontsize=8, bbox_to_anchor=(1.01, 0.01, 0.15, 0.99), 
           loc="upper right", ncol=1, mode="expand", borderaxespad=0., fontsize=7,
           markerscale=.4, labelspacing=.2)
plt.xlabel('Lithology rock type and geology', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(7), ('C', 'P', 'Vb', 'A', 'Smi', 'Pb', 'M'))
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.80)
plt.annotate('B', xy=(0.03, .9), xycoords="axes fraction", fontsize=18,
          bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
plt.show()


# In[ ]:




