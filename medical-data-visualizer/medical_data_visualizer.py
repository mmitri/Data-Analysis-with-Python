import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df['weight']/(df['height']*0.01)**2)>25).astype(int)

# 3
#df.iloc[0:, 7:13] selects only the last six columns
columns_to_normalize = ['cholesterol','gluc']
for column in columns_to_normalize:
    df.loc[df[column] == 1, column] = 0
    df.loc[df[column] > 1, column] = 1

def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])
    #6
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio','variable','value'],as_index=False).count()
    # 7
    fig = sns.catplot(data=df_cat, x = "variable", y = "total", col = "cardio", kind = "bar", hue = "value").figure
    # 8
    fig.savefig('catplot.png')
    return fig

# 9
def draw_heat_map():
    # 10
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    # 11
    corr = df_heat.corr(method="pearson")
    # 12
    mask = np.triu(corr)
    # 13
    fig, ax = plt.subplots(figsize=(12,12))
    sns.heatmap(corr, annot=True, fmt='.1f', center=0.08, cbar_kws = {"shrink":0.5}, mask=mask, linewidths=1, square=True)
    # 14
    fig.savefig('heatmap.png')
    return fig
