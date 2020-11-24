import numpy as np
import pandas as pd
import altair as alt
from yahoo_fin.stock_info import get_data

def visualize_djia():
    """ Visualize DJIA return"""
    
    djia = get_data("DJI", start_date='2020-01-01', end_date='2020-11-01')
    
    rt = djia['close'].apply(lambda x: np.log(x)).diff().fillna(0)
    
    source = rt.rename_axis('date').reset_index()
    
    chart = alt.Chart(source).mark_line().encode(
        x='date:T',
        y='close:Q'
    )
    return chart.properties(title="DJI Return", width=500)

if __name__ == '__main__':
    
    ts_chart = visualize_djia()
    ts_chart.save('djia.html')