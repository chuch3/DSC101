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
    # Rent pricing in kl have some collumn that are still "object" type for example: monthly_rent, rooms, size. So, we needed them to be float. 
    #   Also, removing '"' in the facilities and addditional facilities
    #   Also, removing 'sq.ft.' in "size" collumn
    # Malaysia property for sale also has some collumn that need to be change to the right type like: list_price, unit_price, and also changing the format of 'area' and remove the m2 inside the column

# 2. Changing data type to the right format
Cols_to_convert_float_rent_pricing_KL = [
    "monthly_rent", "rooms", "size",
]