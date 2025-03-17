import pandas as pd
import plotly.express as px

if __name__ == '__main__':
    # read data
    df = pd.read_csv('data.csv')

    # convert date column to type datetime
    df['print_date'] = pd.to_datetime(df['print_date'])

    # plot the graph
    fig = px.scatter(df,
                     x='print_date',
                     y='solving_seconds',
                     color='solving_seconds',
                     template='plotly_dark',
                     trendline='rolling', trendline_options=dict(window=40),
                     trendline_color_override='goldenrod',
                     title='Aju NYT Mini Solve Times from 2022-08-20 to 2025-03-10'
                     )
    
    fig.write_html('index.html')