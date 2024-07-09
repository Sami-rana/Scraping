import csv


def split_recruiter_name(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['First Name', 'Last Name']
        with open(output_file, 'w', newline='', encoding='utf-8') as new_csvfile:
            writer = csv.DictWriter(new_csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                recruiter_name = row['Name']
                if recruiter_name:
                    parts = recruiter_name.split(maxsplit=1)
                    if len(parts) == 2:
                        first_name, last_name = parts
                    else:
                        first_name = parts[0]
                        last_name = ''
                else:
                    first_name = ''
                    last_name = ''
                row['First Name'] = first_name
                row['Last Name'] = last_name
                writer.writerow(row)


input_file = "data/08 - outputfile4800.csv"
output_file = 'output08.csv'
split_recruiter_name(input_file, output_file)
