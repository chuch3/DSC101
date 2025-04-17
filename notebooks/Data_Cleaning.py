import pandas as pd
import numpy as np

# Main Dataset
rent_pricing_KL = pd.read_csv('data/mudah-apartment-kl-selangor.csv')
# Secondary Dataset
malaysia_property_for_sale = pd.read_csv('data/malaysia_property_for_sale.csv')

# 1. Check data type
print(rent_pricing_KL.dtypes)
print("================================")
print(malaysia_property_for_sale.dtypes)
