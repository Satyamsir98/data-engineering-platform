from src.engine import run_engine

df = run_engine()

print("\nFinal Output:\n")
print(df)

df.to_csv("output/result.csv", index=False)