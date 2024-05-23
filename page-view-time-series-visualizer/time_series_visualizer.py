import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import calendar
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=["date"], index_col="date")

# Clean data
df = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(df.index, df['value'])
    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019') 
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month_name()]).mean().value.unstack()
    df_bar = df_bar[list(calendar.month_name)[1:]]
    df_bar.columns.name = "Months"
    # Draw bar plot
    fig = df_bar.plot(figsize=(12,6), kind="bar", ylabel="Average Page Views", xlabel="Years").get_figure()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month'] = pd.Categorical(df_box['month'], 
                    categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
                    ordered=True)
    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
    axs[0] = sns.boxplot(data=df_box, x="year", y="value", ax=axs[0], hue="year", legend=False)
    axs[0].set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)') 
    axs[1] = sns.boxplot(data=df_box, x="month", y="value", ax=axs[1], hue="month", legend=False)
    axs[1].set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)') 
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
