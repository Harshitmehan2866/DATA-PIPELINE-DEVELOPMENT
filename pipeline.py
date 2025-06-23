import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Step 1: Extract
def extract_data(file_path):
    print("Extracting data...")
    df = pd.read_csv(file_path)
    return df

# Step 2: Transform
def transform_data(df):
    print("Transforming data...")

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    # Scale the data
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df_imputed), columns=df.columns)

    return df_scaled

# Step 3: Load
def load_data(df, output_file):
    print("Loading data...")
    df.to_csv(output_file, index=False)
    print(f"Saved to {output_file}")

# Main pipeline
def run_pipeline():
    input_file = "data.csv"
    output_file = "processed_data.csv"

    df = extract_data(input_file)
    df_transformed = transform_data(df)
    load_data(df_transformed, output_file)

if __name__ == "__main__":
    run_pipeline()