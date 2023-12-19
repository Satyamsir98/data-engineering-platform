import pandas as pd


def read_data(path, cloud):
    if cloud == "aws":
        print("Reading from S3 ")
    elif cloud == "azure":
        print("Reading from ADLS")
    else:
        print("Reading from local")

    df = pd.read_csv(path)
    print(f"Data loaded: {len(df)} rows")
    return df


def write_data(df, path, cloud):
    if cloud == "aws":
        print("Writing to S3 ")
    elif cloud == "azure":
        print("Writing to ADLS")
    else:
        print("Writing to local")

    df.to_csv(path, index=False)
    print(f"Data written to {path}")