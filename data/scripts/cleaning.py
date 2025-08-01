import pandas as pd
from pandas.errors import ParserError
from pathlib import Path

def clean_ufo_data(raw_csv_path: Path, clean_csv_path: Path):
    """
    Reads the raw UFO sightings CSV, filters to US-only records with valid latitude/longitude,
    and writes the cleaned CSV to the specified path.
    """
    # Load the raw data
    try:
        df = pd.read_csv(raw_csv_path, engine='python', on_bad_lines='skip')
    except ParserError:
        # Fallback: skip malformed lines
        df = pd.read_csv(raw_csv_path, engine='python', on_bad_lines='skip')

    # Normalize and filter country codes to US
    df['country'] = df['country'].str.lower()
    df_us = df[df['country'] == 'us']

    # Drop rows missing latitude or longitude
    df_us = df_us.dropna(subset=['latitude', 'longitude'])

    # Ensure the destination directory exists
    clean_csv_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the cleaned data
    df_us.to_csv(clean_csv_path, index=False)
    print(f"Cleaned data written to {clean_csv_path} ({len(df_us)} rows)")


if __name__ == "__main__":
    raw_path = Path("data/raw/complete.csv")
    clean_path = Path("data/clean/complete_clean.csv")
    clean_ufo_data(raw_path, clean_path)
