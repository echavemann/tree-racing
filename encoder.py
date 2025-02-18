import pandas as pd
import argparse

def encode_labels(input_csv, output_csv):
    df = pd.read_csv(input_csv, header=None)
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = df[column].astype('category').cat.codes
    df.to_csv(output_csv, index=False)
    print(f"Label encoding complete. Encoded CSV saved to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert all categorical labels to integers in a CSV file.")
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("output_csv", help="Path to save the encoded CSV file")
    
    args = parser.parse_args()
    encode_labels(args.input_csv, args.output_csv)
