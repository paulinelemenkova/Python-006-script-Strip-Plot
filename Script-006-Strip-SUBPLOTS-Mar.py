#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

sb.set_style('darkgrid')
sb.set_context('paper')

os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Morph.csv")

# define 4 data frames for 4 subplots
df1 = dfM.melt(id_vars=['profile'],
               value_vars=['plate_phill', 'plate_pacif', 'plate_maria', 'plate_carol'],
               var_name='Plates', value_name='sedim_thick')
df2 = dfM.melt(id_vars=['profile'],
               value_vars=['plate_phill', 'plate_pacif', 'plate_maria', 'plate_carol'],
               var_name='Plates', value_name='slope_angle')
df3 = dfM.melt(id_vars=['profile'],
               value_vars=['plate_phill', 'plate_pacif', 'plate_maria', 'plate_carol'],
               var_name='Plates', value_name='Mean')
df4 = dfM.melt(id_vars=['profile'],
               value_vars=['plate_phill', 'plate_pacif', 'plate_maria', 'plate_carol'],
               var_name='Plates', value_name='Min')

# define figure
fig = plt.figure(figsize=(10.0, 6.0), dpi=300)
fig.suptitle('Strip plots for geological parameters, Mariana Trench',
             fontsize=10, fontweight='bold', x=0.5, y=0.99)

# subplot 1
ax = fig.add_subplot(221)
sb.stripplot(x='Plates', y='sedim_thick', hue = 'profile',
             palette='RdGy', data=df1, jitter=True
             )
plt.title('sediment thickness', fontsize=10, fontfamily='serif')
plt.legend(bbox_to_anchor=(1.2, .7), loc=1, borderaxespad=-4., ncol=2,
           markerscale=.4, fancybox=False, shadow=False, mode='expand',
           title='profiles:', title_fontsize=8, labelspacing=.2
           )
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.80)

# subplot 2
ax = fig.add_subplot(222)
sb.stripplot(x='Plates', y='slope_angle', hue = 'profile',
             palette='PiYG', data=df2, jitter=True
             )
plt.title('slope angle degree', fontsize=10, fontfamily='serif')
plt.legend(bbox_to_anchor=(1.2, .7), loc=1, borderaxespad=-4., ncol=2,
           markerscale=.4, fancybox=False, shadow=False, mode='expand',
           title='profiles:', title_fontsize=8, labelspacing=.2
           )
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.80)

# subplot 3
ax = fig.add_subplot(223)
sb.stripplot(x='Plates', y='Mean', hue = 'profile',
             palette='PRGn', data=df3, jitter=True
             )
plt.title('mean depth values', fontsize=10, fontfamily='serif')
plt.legend(bbox_to_anchor=(1.2, .7), loc=1, borderaxespad=-4., ncol=2,
           markerscale=.4, fancybox=False, shadow=False, mode='expand',
           title='profiles:', title_fontsize=8, labelspacing=.2
           )

plt.subplots_adjust(bottom=0.15,top=0.85, right=0.80)

# subplot 4
ax = fig.add_subplot(224)
sb.stripplot(x='Plates', y='Min', hue = 'profile',
             palette='RdYlGn', data=df4, jitter=True)
plt.title('max depth values', fontsize=10, fontfamily='serif')
plt.legend(bbox_to_anchor=(1.2, .7), loc=1, borderaxespad=-4.,
           ncol=2, markerscale=.4, fancybox=False, shadow=False, mode='expand',
           title='profiles:', title_fontsize=8, labelspacing=.2
           )
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.80)

# visualizing and saving figure
plt.tight_layout()
fig.savefig('plot_Strip.png', dpi=300)
plt.show()
