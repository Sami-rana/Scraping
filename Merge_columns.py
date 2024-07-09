import pandas as pd

# File paths
input_file = 'data/4800.csv'
output_file = 'outputfile4800.csv'

df = pd.read_csv(input_file)
email_columns = ['Contactemail', 'Email - Emails']
phone_columns = ['Phone', 'Contact Phone', 'Company Phone']
name_columns = ['Contact Full Name', 'Name', 'Recruiter Name']


def get_value(row, columns):
    for col in columns:
        if pd.notna(row[col]):
            return row[col]
    return None


df['Email'] = df.apply(lambda row: get_value(row, email_columns), axis=1)
df = df.dropna(subset=['Email'])

df['Phone1'] = df.apply(lambda row: get_value(row, phone_columns), axis=1)
df = df.dropna(subset=['Phone1'])

df['Full Name'] = df.apply(lambda row: get_value(row, name_columns), axis=1)
df = df.dropna(subset=['Full Name'])

df.to_csv(output_file, index=False)
print(f'Updated CSV file saved as {output_file}')

