import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/diesel_data.csv')

# 1. Convert DATE to datetime objects
df['DATE'] = pd.to_datetime(df['DATE'])

# 2. Calculate Actual Fuel Efficiency (KM/Litre)
# Note: Ensure we handle division by zero if DIESEL is 0
df['CALCULATED_EFFICIENCY'] = df['GPS_READING'] / df['DIESEL']
df.loc[df['DIESEL'] == 0, 'CALCULATED_EFFICIENCY'] = 0

# 3. Aggregate data by Asset Type
efficiency_by_asset = df.groupby('ASSEST_TYPE')['CALCULATED_EFFICIENCY'].mean().sort_values()

# 4. Plotting
efficiency_by_asset.plot(kind='barh', title='Avg Fuel Efficiency by Asset Type')
plt.xlabel('KM/Litre')
plt.show()
