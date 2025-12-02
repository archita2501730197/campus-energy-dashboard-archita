import pandas as pd
from pathlib import Path

def load_all_csv(data_dir='../data'):
    path = Path(data_dir)
    files = path.glob('*.csv')
    all_data = []

    for file in files:
        try:
            df = pd.read_csv(file, on_bad_lines='skip')

            if 'building' not in df.columns:
                df['building'] = file.stem 

            if 'month' not in df.columns:
                df['month'] = pd.to_datetime(df['timestamp']).dt.month

            all_data.append(df)

        except FileNotFoundError:
            print(f"File not found: {file}")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        print("All CSV files loaded successfully!")
        return combined_df
    else:
        print("No data files found!")
        return pd.DataFrame()

if __name__ == "__main__":
    df = load_all_csv()
    print(df.head())
