import csv


def remove_duplicates(csv_file):
    unique_first_names = set()
    unique_rows = []

    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_name = row.get('Email')
            if first_name and first_name not in unique_first_names:
                unique_first_names.add(first_name)
                unique_rows.append(row)

    output_file = 'unique_' + csv_file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_rows)

    return output_file


# Example usage:
csv_file = 'output_08.csv'
unique_file = remove_duplicates(csv_file)
print("Unique rows saved to:", unique_file)


# import csv
#
#
# def remove_duplicates(csv_file):
#     unique_rows = set()
#
#     # Read header row separately
#     with open(csv_file, 'r', newline='', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         header = next(reader)  # Read header row and store it
#
#         # Read remaining rows and store unique ones
#         for row in reader:
#             row_tuple = tuple(row)
#             unique_rows.add(row_tuple)
#
#     # Write unique rows to a new CSV file
#     output_file = 'unique_' + csv_file
#     with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
#         writer = csv.writer(outfile)
#         writer.writerow(header)  # Write header row
#         writer.writerows(unique_rows)
#
#     return output_file
#
#
# # Example usage:
# csv_file = 'output325.csv'
# unique_file = remove_duplicates(csv_file)
# print("Unique rows saved to:", unique_file)
