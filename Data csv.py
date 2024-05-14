import pandas as pd 
import numpy as np
import plotly.express as px
df = pd.read_csv(r"c:\Users\ijo\Downloads\Data (1).csv")
df['date'] = pd.to_datetime(df['date'])
#Time Series Analysis
fig1 = px.scatter(df, x='date', y='total_price', title= 'Total Price Over Time')
fig1.show()
#Anomaly Detection
df['total_price_zscore'] = (df['total_price'] - df['total_price'].mean()) / df['total_price'].std()
anomaly_threshold = 3
df['anomaly'] = np.where(np.abs(df['total_price_zscore']) > anomaly_threshold, True, False)
#Visualize Anomalies
anomalies = df[df['anomaly']]
fig2 = px.scatter(anomalies, x='date', y='total_price', color='anomaly', title='Anomalies Detection (Z-score)')
fig2.show()
#Visualize Clusters
fig3 = px.scatter(df, x='total_price', y='quantity', color='cluster', title='Clusters of Transaction Patterns')
fig3.show()
