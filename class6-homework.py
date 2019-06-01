#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D


breast_cancer_df = pd.read_csv('breast-cancer/wdbc.data',
                 sep=',',
                 header=0)

# Adding data set headers to the data frame (I only need 11 columns 2 to 12 columns out of the 32)
breast_cancer_df.columns = ['ID_number', 'Diagnosis', 'Radius', 'Texture','Perimeter', 'Area', 'Smoothness',
                            'Compactness', 'Concavity', 'Concave_Points', 'Symmetry','Fractal_Dimension', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32']


# redefining the data set header to only display 11 columns

breast_cancer = breast_cancer_df.drop(['ID_number', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                                       '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'], axis=1)


os.makedirs('plots/matplotlib_multiple_plot_axes', exist_ok=True)
os.makedirs('plots/seaborn_pairplot', exist_ok=True)
os.makedirs('plots/matplotlib_3D_plots', exist_ok=True)



# seaborn-pairplot
breast_cancer['encoded_diagnosis'] = breast_cancer['Diagnosis'].map({'B': 0, 'M': 1})
sns.pairplot(breast_cancer, hue='encoded_diagnosis', diag_kind='hist')
plt.savefig('plots/seaborn_pairplot/cancer_pairplot.png')

pd.set_option('display.max_columns', None)

plt.clf()


plt.style.use("ggplot")

# scatter with 4 features
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.grid(axis='y', alpha=0.5)
axes.scatter(breast_cancer_df['Radius'], breast_cancer_df['Texture'])
axes.scatter(breast_cancer_df['Radius'], breast_cancer_df['Perimeter'])
axes.scatter(breast_cancer_df['Radius'], breast_cancer_df['Smoothness'])
axes.scatter(breast_cancer_df['Radius'], breast_cancer_df['Area'])
axes.set_title(f'Radius comparisons')
axes.set_ylabel(f'Texture/ Perimeter/ Smoothness/ Area')
axes.set_xlabel(f'Radius')
axes.legend()
plt.savefig(f'plots/matplotlib_multiple_plot_axes/radius_texture_smoothness_scatter.png', dpi=300)


plt.close()


# Multifeature with size,colours,shapes

fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.grid(axis='y', alpha=0.5)
axes.scatter(breast_cancer_df['Radius'], breast_cancer_df['Texture'], s=(breast_cancer_df['Perimeter'] * breast_cancer_df['Smoothness']) * 1,
             label=f'Radius to Texture', color='green', marker='x', edgecolors='w', alpha=0.7)
axes.scatter(breast_cancer_df['Radius'], breast_cancer_df['Perimeter'], s=(breast_cancer_df['Radius'] * breast_cancer_df['Perimeter']) / 64,
             label=f'Radius to Perimeter', color='orange', marker='s', edgecolors='w', alpha=0.7)
axes.scatter(breast_cancer_df['Radius'], breast_cancer_df['Smoothness'], s=(breast_cancer_df['Radius'] * breast_cancer_df['Smoothness']) * 32, label=f'Radius to Smoothness', color='purple',
             marker='^', edgecolors='w', alpha=0.7)
axes.set_title(f'Radius Comparisons')
axes.set_ylabel(f'Texture/ Perimeter/ Smoothness/ Area')
axes.set_xlabel(f'Radius')
axes.legend()
plt.savefig(f'plots/matplotlib_multiple_plot_axes/radius_texture_multifeature_scatter.png', dpi=300)


# 3D plot

malign = breast_cancer[breast_cancer['Diagnosis'] == 'M']
benign = breast_cancer[breast_cancer['Diagnosis'] == 'B']
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1, projection='3d')
line1 = axes.scatter(malign['Radius'], malign['Perimeter'], malign['Area'])
line2 = axes.scatter(benign['Radius'], benign['Perimeter'], benign['Area'])
axes.legend((line1, line2), ('Malignant', 'Benign'))
axes.set_xlabel('Radius')
axes.set_ylabel('Perimeter')
axes.set_zlabel('Area')
plt.savefig('plots/matplotlib_3D_plots/cancer_diagnosis_scatter_3d.png')

plt.close()