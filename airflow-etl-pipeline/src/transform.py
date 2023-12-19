def transform(df):
    print("Starting transformation...")

    # Removing null values
    df = df.dropna()

    # Removing invalid salary
    df = df[df["salary"] > 0]

    # Added processed flag
    df["processed_flag"] = 1

    print(f"Transformed data: {len(df)} rows")
    return df