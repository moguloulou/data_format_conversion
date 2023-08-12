import binascii
import datetime
import os

def utf8_to_hex(utf8_str):
    return utf8_str.encode("utf-8").hex().upper()

def hex_to_utf8(hex_str):
    return bytes.fromhex(hex_str).decode("utf-8")

def hex_to_binary(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)

def binary_to_hex(binary_str):
    return hex(int(binary_str, 2))[2:].upper()

def binary_to_decimal(binary_str):
    return str(int(binary_str, 2))

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input == 'QUIT':
            print("Terminating the program.")
            exit()
        elif user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please choose from:", valid_options)

def is_valid_binary(input_str):
    return all(c in "01" for c in input_str)

def is_valid_decimal(input_str):
    return input_str.isdigit()

def is_valid_utf8(input_str):
    try:
        input_str.encode("utf-8").decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False

def is_valid_hex(input_str):
    return all(c in "0123456789ABCDEFabcdef" for c in input_str)

def convert_data(input_data, input_format, output_format):
    if input_format == "UTF8" and output_format == "HEX":
        if not is_valid_utf8(input_data):
            return "Invalid input: Not a valid UTF-8 string"
        return utf8_to_hex(input_data)
    elif input_format == "HEX" and output_format == "UTF8":
        if not is_valid_hex(input_data):
            return "Invalid input: Not a valid hexadecimal string"
        return hex_to_utf8(input_data)
    elif input_format == output_format:
        return input_data  # No conversion needed
    else:
        if input_format == "HEX":
            if not is_valid_hex(input_data):
                return "Invalid input: Not a valid hexadecimal string"
            input_data = int(input_data, 16)
        elif input_format == "BINARY":
            if not is_valid_binary(input_data):
                return "Invalid input: Not a valid binary string"
            input_data = int(input_data, 2)
        elif input_format == "DECIMAL":
            if not is_valid_decimal(input_data):
                return "Invalid input: Not a valid decimal number"
            input_data = int(input_data)
        if output_format == "HEX":
            return hex(input_data)[2:].upper()
        elif output_format == "BINARY":
            return bin(input_data)[2:].zfill(8)
        elif output_format == "DECIMAL":
            return str(input_data)
        else:
            return "Unsupported conversion"

def main():
    valid_formats = ['HEX', 'BINARY', 'DECIMAL', 'UTF8']

    while True:
        if 'choice' in locals():
            change_formats = input("Do you want to change input/output formats (Y/N)? ").upper()
            if change_formats == 'Y':
                input_format = get_valid_input("Enter input format (HEX, BINARY, DECIMAL, UTF8):", valid_formats)
                output_format = get_valid_input("Enter output format (HEX, BINARY, DECIMAL, UTF8): ", valid_formats)
        else:
            input_format = get_valid_input("Enter input format (HEX, BINARY, DECIMAL, UTF8): ", valid_formats)
            output_format = get_valid_input("Enter output format (HEX, BINARY, DECIMAL, UTF8): ", valid_formats)

        data_source = input("Enter file name in single quotes ('') for file input or data(separated by spaces) to convert: ")

        try:
            if data_source.startswith("'") and data_source.endswith("'"):
                file_name = data_source[1:-1]
                if not os.path.isfile(file_name):
                    print(f"File '{file_name}' not found.")
                    continue
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                converted_lines = []
                for line in lines:
                    converted_line = convert_data(line.strip(), input_format, output_format)
                    if "Invalid input" in converted_line:
                        print(converted_line)
                    else:
                        converted_lines.append(converted_line)
                if converted_lines:
                    print("Converted data:")
                    for converted_line in converted_lines:
                        print(converted_line)
                    output_file_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_output.txt"
                    try:
                        with open(output_file_name, 'w') as output_file:
                            output_file.write("\n".join(converted_lines))
                        print(f"Data written to '{output_file_name}'.")
                    except IOError:
                        print(f"Warning: Unable to write to '{output_file_name}'. You might not have write access to the disk.")
            else:
                if data_source.upper() == "QUIT":
                    print("Terminating the program.")
                    exit()
                data_list = data_source.split()
                converted_data = []
                for data_item in data_list:
                    converted_item = convert_data(data_item, input_format, output_format)
                    if "Invalid input" in converted_item:
                        print(converted_item)
                    else:
                        converted_data.append(converted_item)
                if converted_data:
                    print("Converted data:")
                    for converted_item in converted_data:
                        print(converted_item)
        except FileNotFoundError:
            print(f"File '{data_source}' not found.")
            continue

        choice = input("Do you want to continue (Y/N)? ").upper()
        if choice != 'Y':
            break

if __name__ == "__main__":
    main()