import re
import csv
import sys

# Function to read DDL from a file


def read_ddl_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def convert_ddl_to_csv(ddl, output_filename):
    # CSV Header
    csv_data = [["fieldName", "dataType", "default", "other"]]

    # Extract field definitions from the DDL
    for line in ddl.split("\n"):
        formatted_line = re.split(r'\s{2,}', line.replace(',', ''))[1:]
        if re.match(r'^\).*', line):
            print("Encountered End of Table, exit")
            break
        if formatted_line:
            if re.match(r'primary key', formatted_line[0].lower().strip()):
                csv_data[-1] += formatted_line
            else:
                csv_data.append(formatted_line)
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
