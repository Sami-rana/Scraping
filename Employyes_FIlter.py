import pandas as pd
import os


def filter_employees(csv_file, output_file):
    if not os.path.isfile(csv_file):
        print(f"File not found: {csv_file}")
        return
    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return
    if 'Number of Employees' not in df.columns:
        print("Column 'Number of Employees' not found in the CSV file")
        return
    filtered_df = df[df['Number of Employees'] <= 900]
    try:
        filtered_df.to_csv(output_file, index=False)
        print(f"Filtered data has been saved to {output_file}")
    except Exception as e:
        print(f"Error writing to the CSV file: {e}")


input_csv = r'C:\Users\junai\PycharmProjects\Assessment\cleaned_file_08.csv'
output_csv = r'C:\Users\junai\PycharmProjects\Assessment\output_08.csv'

filter_employees(input_csv, output_csv)
