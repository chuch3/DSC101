import pandas as pd
import numpy as np

# Main Dataset
rent_pricing_KL = pd.read_csv('data/RPK-RAW.csv')
# Secondary Dataset
malaysia_property_for_sale = pd.read_csv('data/MPFS-RAW.csv')

# 1. Check data type
print(rent_pricing_KL.dtypes)
print("================================")
print(malaysia_property_for_sale.dtypes)
print("================================")

# 2. Changing data type to the right format

# Specified the column that need to be converted
Cols_to_convert_float_rent_pricing_KL = [
    "monthly_rent", "rooms", "size"
]
Cols_to_remove_punctuation_rent_pricing_KL = [
    "facilities", "additional_facilities"
]

Cols_to_convert_float_malaysia_property_for_sale = [
    "list_price", "unit_price", "area"
]

Cols_to_remove_punctuation_malaysia_property_for_sale = [
    "location", "list_price"
]

# Loop cleaning the Cols_to_convert_float_rent_pricing_KL
for col in Cols_to_convert_float_rent_pricing_KL:
    rent_pricing_KL[col] = (
        rent_pricing_KL[col]
        .astype(str)    # Convert type into string
        .str.strip()    # Remove extra spaces
        .str.replace(r"[^\d.]", "", regex=True)
        .replace('', np.nan)
        .str.replace(r"\.{2,}", ".", regex=True)
        .astype(float)  # Convert to float
    )

# Loop cleaning the Cols_to_remove_punctuation_rent_pricing_KL
for col in Cols_to_remove_punctuation_rent_pricing_KL:
    rent_pricing_KL[col] = (
        rent_pricing_KL[col]
        .astype(str)
        .str.strip()
        .str.replace('"', "")  # Remove " in facilities
    )

# Loop cleaning the Cols_to_convert_float_malaysia_property_for_sale
for col in Cols_to_convert_float_malaysia_property_for_sale:
    malaysia_property_for_sale[col] = (
        malaysia_property_for_sale[col]
        .astype(str)    # Convert type into string
        .str.strip()    # Remove extra spaces
        .str.replace(r"[^\d.]", "", regex=True)
        .replace('', np.nan)
        .str.replace(r"\.{2,}", ".", regex=True)
        .astype(float)  # Convert to float
    )

# Loop cleaning the Cols_to_remove_punctuation_malaysia_property_for_sale
for col in Cols_to_remove_punctuation_malaysia_property_for_sale:
    malaysia_property_for_sale[col] = (
        malaysia_property_for_sale[col]
        .astype(str)
        .str.strip()
        .str.replace('"', "")  # Remove " in location and list_price
        .str.replace('RM', '') # Remove 'RM' if present
        .str.replace(r"/m2", "")  # Remove '/m2' if present
    )

# Save to the new file
rent_pricing_KL.to_csv("data/RPK-Cleaned.csv", index=False)
malaysia_property_for_sale.to_csv("data/MPFS-Cleaned.csv", index=False)

print(rent_pricing_KL.head())
print(malaysia_property_for_sale.head())