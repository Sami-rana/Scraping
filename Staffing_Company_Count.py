import pandas as pd


def process_csv(file_path, column_name, search_word, output_file):
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip')
        matching_rows = df[df[column_name].str.contains(search_word, case=False, na=False)]
        count = matching_rows.shape[0]
        df_cleaned = df[~df[column_name].str.contains(search_word, case=False, na=False)]
        df_cleaned.to_csv(output_file, index=False)

        return count
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


file_path = 'output08.csv'
column_name = 'Industry'

# When Company Enrich by Apollo then use these Keywords """ staffing & recruiting """ Tp Remove Staffing from Raw File
# And When Company Enrich by other Service then use these keywords """ Staffing and Recruiting """

search_word = 'Staffing and Recruiting'
output_file = 'cleaned_file_08.csv'

count = process_csv(file_path, column_name, search_word, output_file)
print(f'Number of rows containing "{search_word}": {count}')


