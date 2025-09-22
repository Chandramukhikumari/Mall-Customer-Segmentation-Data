import pandas as pd
#  Load the dataset  
df = pd.read_csv(r"C:\Users\91707\Desktop\data analyst\Mall_Customers.csv")

#  Inspect the raw data
print("\nFirst 5 rows")
print(df.head())
print("\n Info ")
print(df.info())
print("\nMissing values")
print(df.isnull().sum())
print(f"\nDuplicates: {df.duplicated().sum()}")

#  Remove duplicates
df.drop_duplicates(inplace=True)

#  Standardize column names (lowercase + underscores)
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

#  Handle missing values
for col in df.columns:
    if df[col].dtype in ["int64", "float64"]:
        df[col].fillna(df[col].median(), inplace=True)
    else:
        if not df[col].mode().empty:
            df[col].fillna(df[col].mode()[0], inplace=True)

#  Fix inconsistent formats
# Gender → category (standardize text)
if "gender" in df.columns:
    df["gender"] = (
        df["gender"]
        .astype(str)
        .str.strip()
        .str.title()
        .astype("category")
    )

# Ensure numeric columns are correct
for col in ["age", "annual_income_(k$)", "spending_score_(1-100)"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove impossible values (optional)
if "age" in df.columns:
    df = df[(df["age"] > 0) & (df["age"] < 120)]

#  Final check
print("\n--- Cleaned dataset info ---")
print(df.info())
print(df.head())

#  Save the cleaned dataset
df.to_csv(
    r"C:\Users\91707\Desktop\data analyst\cleaned_Mall_Customers.csv",
    index=False
)

print("\n Cleaned dataset saved to 'cleaned_Mall_Customers.csv'")
