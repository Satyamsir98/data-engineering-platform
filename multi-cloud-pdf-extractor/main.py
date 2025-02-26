from src.pdf_extractor import run

df = run()

print("\nFinal Extracted Data:\n")
print(df)

df.to_csv("output/extracted.csv", index=False)