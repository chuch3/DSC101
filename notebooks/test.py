""" Data analysis and ML stack modules """

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set(style="whitegrid")

_DATA_FILE_NAME: str = "cybersecurity_intrusion_data.csv"
_DATA_DIR_NAME:  str = "data"
_DATA_FILE_PATH: str = os.path.realpath(
        os.path.os.path.join("..", _DATA_DIR_NAME, _DATA_FILE_NAME)
)

def main():
    df = pd.read_csv(_DATA_FILE_PATH)


if __name__ == "__main__":
    main()
