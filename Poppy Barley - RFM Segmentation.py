# Step 0: Load, filter, clean, and aggregate the data at the customer level
import matplotlib as plt
import numpy as np
import pandas as pd
df = pd.read_excel (r'/Users/changtran/Downloads/Poppy Barley Dataset (REVISED).xlsx')

#Step 1: Create RFM Features for each customers
df_RFM = df.groupby('Cus_ID')['Orders','Tot Avg Sales']
df_RFM.columns = ['Frequency', 'Monetary']
df_RFM.head()
print(df.head())

#Step 2: To automate the segmentation we will use 80% quantile for Recency and Monetary
# We will use the 80% quantile for each feature
quantiles = df_RFM.quantile(q=[0.8])
print(quantiles)

