import re
import csv
import sys

# Function to read DDL from a file


def read_ddl_file(filename):
    with open(filename, 'r') as file:
        return file.read()


# Regular expression to parse each line of the DDL
ddl_regex = re.compile(r'\s*(\w+)\s+([a-zA-Z0-9\(\)\s]+)(.*),?')

# Function to clean up the "other" details, removing trailing commas


def clean_other(other):
    # Remove trailing commas and unnecessary whitespace/newlines
    return other.strip().rstrip(',')


def remove_whitespace(text):
    return re.sub(r'\s+', '', text)

# Function to convert DDL to CSV


def convert_ddl_to_csv(ddl, output_filename):
    # CSV Header
    csv_data = [["fieldName", "dataType", "other"]]

    # Extract field definitions from the DDL
    for line in ddl.split("\n"):
        match = ddl_regex.match(line)
        if match:
            # Remove whitespace from fieldName
            field_name = remove_whitespace(match.group(1))
            # Remove whitespace from dataType
            data_type = remove_whitespace(match.group(2))
            # Remove whitespace from "other" field
            other = remove_whitespace(clean_other(match.group(3)))
            csv_data.append([field_name, data_type, other])
    # Write to CSV file
    with open(output_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print(f"CSV file has been generated: {output_filename}")


# Main function
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_ddl.py <input_filename> <output_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Read DDL from the input file
    ddl_content = read_ddl_file(input_filename)

    # Convert DDL to CSV
    convert_ddl_to_csv(ddl_content, output_filename)
