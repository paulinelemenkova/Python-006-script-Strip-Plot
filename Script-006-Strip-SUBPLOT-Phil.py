#!/usr/bin/env python
# coding: utf-8
#
import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-GeomorphPhil.csv")
sb.set_style('darkgrid')
#
df1 = dfM.melt(id_vars=['profile'], 
              value_vars=['geol_c', 'geol_p', 'geol_vb', 'geol_a', 'geol_smi', 'geol_pb', 'geol_m'],
              var_name='Geology', value_name='Nr. of observation points')
df2 = dfM.melt(id_vars=['profile'], 
              value_vars=['plate_phil', 'plate_sunda'],
              var_name='Plates', value_name='Nr. of observation points')
#  
fig = plt.figure(figsize=(10.0, 4.0), dpi=300)
fig.suptitle('Strip plot of sample distribution for geological parameters, Philippine archipelago',
            fontsize=10, fontweight='bold', x=0.5, y=0.99)
#
# subplot 1
ax = fig.add_subplot(121)
sb.stripplot(x='Geology', y='Nr. of observation points', 
             hue = 'profile', palette='tab20b', data=df1, jitter=True)
plt.title('Geology and lithology', fontsize=10, fontfamily='serif')
plt.legend(title='Profiles', title_fontsize=8, bbox_to_anchor=(1.01, 0.01, 0.15, 0.99), 
           loc="upper right", ncol=1, mode="expand", borderaxespad=0., fontsize=7,
           markerscale=.4, labelspacing=.2)
plt.xlabel('Lithology rock type and geology', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(7), ('C', 'P', 'Vb', 'A', 'Smi', 'Pb', 'M'))
plt.annotate('A', xy=(0.03, .9), xycoords="axes fraction", fontsize=14,
          bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.80)
#
# subplot 2
ax = fig.add_subplot(122)
sb.stripplot(x='Plates', y='Nr. of observation points', 
             hue = 'profile', palette='tab20', data=df2, jitter=True)
plt.title('Sunda Plate and Philippine Plate', fontsize=10, fontfamily='serif')
plt.legend(title='Profiles', title_fontsize=8, bbox_to_anchor=(1.01, 0.01, 0.15, 0.99), loc="upper right",
           ncol=1, mode="expand", borderaxespad=0., fontsize=7,
           markerscale=.4, labelspacing=.2)
plt.xlabel('Tectonic Plates', fontsize=10, fontfamily='sans-serif')
plt.xticks(np.arange(2), ('Philippine Plate', 'Sunda Plate'))
plt.annotate('B', xy=(0.03, .9), xycoords="axes fraction", fontsize=14,
          bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.80)
#
plt.tight_layout()
fig.savefig('plot_StripPhil.png', dpi=300)
plt.show()
