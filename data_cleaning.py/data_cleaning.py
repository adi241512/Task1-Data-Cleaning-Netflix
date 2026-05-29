import pandas as pd

df = pd.read_csv("dataset/netflix1.csv")

print("Rows before cleaning:", len(df))

duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)
import pandas as pd

# Load dataset
df = pd.read_csv("dataset/netflix1.csv")

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Standardize text columns
text_columns = ["type", "title", "director", "country", "rating"]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# Convert date column
if "date_added" in df.columns:
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Save cleaned dataset
df.to_csv("output/cleaned_netflix.csv", index=False)

print("Cleaning completed successfully!")
print("Cleaned file saved in output folder.")
df = df.drop_duplicates()

print("Rows after removing duplicates:", len(df))