# import pandas as pd
#
# # Read the CSV file
# input_file = 'Find-Jobs-Table-(26-June-2024)-Default-View-export-1719410109709.csv'
# output_file = 'output5000.csv'  # Replace with your desired output file name
#
# # Load the CSV file into a DataFrame
# df = pd.read_csv(input_file)
#
# # Remove rows where the "Email" column is empty
# df = df.dropna(subset=['Email'])
#
# # Save the updated DataFrame to a new CSV file
# df.to_csv(output_file, index=False)
#
# print(f'Updated CSV file saved as {output_file}')


# # //////////////////////////////// For Email Columns \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#
# import pandas as pd
#
# input_file = '4000.csv'
# output_file = 'Email4000.csv'
#
# df = pd.read_csv(input_file)
# columns_to_check = ['Contactemail', 'Email - Emails']
#
#
# def get_phone(row):
#     for col in columns_to_check:
#         if pd.notna(row[col]):
#             return row[col]
#     return None
#
#
# df['Email'] = df.apply(get_phone, axis=1)
# df = df.dropna(subset=['Email'])
# df.to_csv(output_file, index=False)
# print(f'Updated CSV file saved as {output_file}')

