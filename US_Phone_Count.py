import pandas as pd


def count_phone_numbers(csv_file, phone_column):
    df = pd.read_csv(csv_file)
    filtered_numbers = df[df[phone_column].astype(str).str.startswith('+1')]
    count = filtered_numbers.shape[0]

    return count


csv_file = 'cleaned_file_324.3.csv'
phone_column = 'Phone'
count = count_phone_numbers(csv_file, phone_column)
print(f'Number of phone numbers starting with +1: {count}')
