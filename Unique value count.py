import csv


def count_unique_first_names(csv_file):
    unique_first_names = {}
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_name = row.get('Email')
            if first_name:
                unique_first_names[first_name] = unique_first_names.get(first_name, 0) + 1
    return len(unique_first_names)


csv_file = 'unique_output_08.csv'
unique_count = count_unique_first_names(csv_file)
print("Unique 'Emails Or Company' count:", unique_count)


# # import csv
# #
# #
# # def count_unique_values(input_file):
# #     unique_values = set()
# #
# #     with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
# #         reader = csv.reader(csvfile)
# #         next(reader)  # Skip header row if exists
# #
# #         for row in reader:
# #             # Assuming the first column is the column you want to check
# #             value = row[0]
# #             unique_values.add(value)
# #
# #     return len(unique_values)
# #
# #
# # input_file = 'unique_output400.csv'
# # unique_count = count_unique_values(input_file)
# # print("Unique first names count:", unique_count)


# import csv
#
# class DataProcessor:
#     def __init__(self, input_file):
#         self.input_file = input_file
#
#     def split_names(self):
#         output_rows = []
#         with open(self.input_file, 'r', newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile)
#             fieldnames = reader.fieldnames + ['First Name', 'Last Name']
#
#             for row in reader:
#                 recruiter_name = row['Name']
#                 # Check if recruiter name is not empty
#                 if recruiter_name:
#                     # Split the recruiter name into first name and last name
#                     parts = recruiter_name.split(maxsplit=1)  # Split at the first space
#                     if len(parts) == 2:
#                         first_name, last_name = parts
#                     else:
#                         first_name = parts[0]
#                         last_name = ''  # Set last name as empty if no space found
#                 else:
#                     first_name = ''
#                     last_name = ''
#                 # Update the row with first name and last name
#                 row['First Name'] = first_name
#                 row['Last Name'] = last_name
#                 output_rows.append(row)
#
#         return output_rows
#
#     def remove_duplicates(self, rows, output_file):
#         unique_first_names = set()
#         unique_rows = []
#
#         for row in rows:
#             email = row.get('Email')
#             if email:  # Check if email is not empty
#                 unique_first_names.add(email)
#                 unique_rows.append(row)
#
#         # Write unique rows to a new CSV file
#         with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
#             fieldnames = rows[0].keys()  # Assuming all rows have the same keys
#             writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(unique_rows)
#
#         return output_file
#
#     def count_unique_values(self, field):
#         unique_values = set()
#         with open(self.input_file, 'r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 value = row.get(field)
#                 if value:
#                     unique_values.add(value)
#         return len(unique_values)
#
#
# # Example usage:
# input_file = "data/378 - Find-Jobs-Table-(17-May-2024)-Default-View-export-1715937577455.csv"
# output_file = "cleaned_output Final_18.csv"
# data_processor = DataProcessor(input_file)
#
# # Split names
# split_rows = data_processor.split_names()
# print("Names split successfully.")
#
# # Remove rows with empty email and write to new file
# unique_file = data_processor.remove_duplicates(split_rows, output_file)
# print("Rows with empty emails removed and saved to:", unique_file)
#
# # Count unique values
# unique_count = data_processor.count_unique_values('Company')
# print("Unique companies count:", unique_count)
