import pandas as pd

# Load dataset
df = pd.read_csv("dataset/cardekho_dataset.csv")

print("BEFORE CLEANING")
print("Shape:", df.shape)

# Remove unnecessary column
if "Unnamed: 0" in df.columns:
    df = df.drop("Unnamed: 0", axis=1)

# Check data types
print("\nDATA TYPES")
print(df.dtypes)

# Check first five records
print("\nCLEANED DATASET")
print(df.head())

# Save cleaned dataset
df.to_csv("dataset/cleaned_cars.csv", index=False)

print("\nAFTER CLEANING")
print("Shape:", df.shape)
print("\nCleaned dataset saved successfully!")