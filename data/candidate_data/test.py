import pandas as pd

_CYBER_TEST = "cybersecurity_attacks.csv"
_INTRUSION_TEST = "cybersecurity_intrusion_data.csv"

def main() -> None:
    df = pd.read_csv(_INTRUSION_TEST)

    print(df.info(), "\n")
    print(df.describe(), "\n")
    print(df.isnull().sum(), "\n")



if __name__ == "__main__":
    main()



